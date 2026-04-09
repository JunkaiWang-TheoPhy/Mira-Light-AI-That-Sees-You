#!/usr/bin/env python3

import argparse
from datetime import datetime
import socketserver
import threading

import serial

from bus_servo_protocol import normalize_servo_packet


DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 9527
DEFAULT_UART_DEVICE = "/dev/ttyS1"
DEFAULT_BAUDRATE = 115200
LINE_ENDINGS = {
    "none": b"",
    "lf": b"\n",
    "crlf": b"\r\n",
}


class SerialForwarder:
    def __init__(
        self,
        uart_device: str,
        baudrate: int,
        line_ending: str,
        dry_run: bool,
    ) -> None:
        self.uart_device = uart_device
        self.baudrate = baudrate
        self.line_ending = LINE_ENDINGS[line_ending]
        self.dry_run = dry_run
        self.lock = threading.Lock()
        self.ser = None

        if not self.dry_run:
            self._open_serial()

    def _open_serial(self) -> None:
        if self.ser is not None and self.ser.is_open:
            return
        self.ser = serial.Serial(self.uart_device, self.baudrate, timeout=1)

    def send(self, packet: str) -> int:
        payload = packet.encode("ascii") + self.line_ending
        if self.dry_run:
            return len(payload)

        with self.lock:
            self._open_serial()
            sent = self.ser.write(payload)
            self.ser.flush()
            return sent

    def close(self) -> None:
        if self.ser is not None and self.ser.is_open:
            self.ser.close()


class GatewayRequestHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        client_host, client_port = self.client_address
        print(f"{_now()} client connected: {client_host}:{client_port}")

        while True:
            raw = self.rfile.readline()
            if not raw:
                break

            text = raw.decode("utf-8", errors="replace").strip()
            if not text:
                continue

            print(f"{_now()} net rx: {text}")

            try:
                normalized = normalize_servo_packet(text)
                sent = self.server.forwarder.send(normalized)  # type: ignore[attr-defined]
            except Exception as exc:
                response = f"ERR,{exc}\n"
                self.wfile.write(response.encode("utf-8"))
                self.wfile.flush()
                print(f"{_now()} net tx: {response.strip()}")
                continue

            response = f"OK,{normalized},{sent}\n"
            self.wfile.write(response.encode("utf-8"))
            self.wfile.flush()
            print(f"{_now()} uart tx: {normalized}")
            print(f"{_now()} net tx: {response.strip()}")

        print(f"{_now()} client disconnected: {client_host}:{client_port}")


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


def parse_args():
    parser = argparse.ArgumentParser(
        description="RDK X5 TCP gateway for bus-servo protocol packets"
    )
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--uart-device", default=DEFAULT_UART_DEVICE)
    parser.add_argument("--baudrate", type=int, default=DEFAULT_BAUDRATE)
    parser.add_argument(
        "--line-ending",
        choices=sorted(LINE_ENDINGS),
        default="none",
        help="UART line ending appended after each validated packet",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate packets and send OK/ERR without writing to UART",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    forwarder = SerialForwarder(
        uart_device=args.uart_device,
        baudrate=args.baudrate,
        line_ending=args.line_ending,
        dry_run=args.dry_run,
    )

    with ThreadedTCPServer((args.host, args.port), GatewayRequestHandler) as server:
        server.forwarder = forwarder  # type: ignore[attr-defined]
        print(
            f"{_now()} gateway listen on {args.host}:{args.port} "
            f"(dry_run={args.dry_run}, uart={args.uart_device}, baudrate={args.baudrate}, "
            f"line_ending={args.line_ending})"
        )
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print(f"\n{_now()} gateway stopped")
        finally:
            forwarder.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
