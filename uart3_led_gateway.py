#!/usr/bin/env python3

import argparse
from datetime import datetime
import socketserver
import threading
import time

import serial

from uart3_led_protocol import (
    AckMessage,
    BAUDRATE,
    DEFAULT_LINE_ENDING,
    LINE_ENDINGS,
    ReadyMessage,
    TouchEvent,
    UART_DEVICE,
    UnknownMessage,
    normalize_outgoing_command,
    parse_incoming_message,
    split_uart_chunk,
)


DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 9528
DEFAULT_IDLE_TIMEOUT = 0.2


def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


class SerialBridge:
    def __init__(
        self,
        uart_device: str,
        baudrate: int,
        line_ending: str,
        idle_timeout: float,
        dry_run: bool,
    ) -> None:
        self.uart_device = uart_device
        self.baudrate = baudrate
        self.line_ending = LINE_ENDINGS[line_ending].encode("utf-8")
        self.idle_timeout = idle_timeout
        self.dry_run = dry_run
        self.write_lock = threading.Lock()
        self.stop_event = threading.Event()
        self.reader_thread = None
        self.ser = None

        if not self.dry_run:
            self._open_serial()

    def _open_serial(self) -> None:
        if self.ser is not None and self.ser.is_open:
            return
        self.ser = serial.Serial(self.uart_device, self.baudrate, timeout=0.2)

    def start_reader(self, callback) -> None:
        if self.dry_run:
            return
        self.reader_thread = threading.Thread(
            target=self._reader_loop,
            args=(callback,),
            daemon=True,
        )
        self.reader_thread.start()

    def send(self, command: str) -> int:
        payload = command.encode("utf-8") + self.line_ending
        if self.dry_run:
            return len(payload)

        with self.write_lock:
            self._open_serial()
            sent = self.ser.write(payload)
            self.ser.flush()
            return sent

    def _reader_loop(self, callback) -> None:
        buffer = bytearray()
        last_rx_time = 0.0

        while not self.stop_event.is_set():
            chunk = self.ser.read(self.ser.in_waiting or 1)
            if not chunk:
                if buffer and (time.monotonic() - last_rx_time) > self.idle_timeout:
                    callback(bytes(buffer))
                    buffer.clear()
                continue

            last_rx_time = time.monotonic()
            buffer.extend(chunk)

            while True:
                line_end = -1
                marker_len = 0
                for marker in (b"\r\n", b"\n", b"\r"):
                    idx = buffer.find(marker)
                    if idx != -1:
                        line_end = idx
                        marker_len = len(marker)
                        break

                if line_end == -1:
                    break

                raw = bytes(buffer[:line_end])
                del buffer[: line_end + marker_len]
                callback(raw)

        if buffer:
            callback(bytes(buffer))

    def close(self) -> None:
        self.stop_event.set()
        if self.reader_thread is not None:
            self.reader_thread.join(timeout=1.0)
        if self.ser is not None and self.ser.is_open:
            self.ser.close()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(self, server_address, handler_cls, bridge, emit_binary: bool):
        super().__init__(server_address, handler_cls)
        self.bridge = bridge
        self.emit_binary = emit_binary
        self.clients = set()
        self.clients_lock = threading.Lock()

    def register_client(self, client) -> None:
        with self.clients_lock:
            self.clients.add(client)

    def unregister_client(self, client) -> None:
        with self.clients_lock:
            self.clients.discard(client)

    def broadcast(self, line: str) -> None:
        with self.clients_lock:
            clients = list(self.clients)

        stale = []
        for client in clients:
            try:
                client.send_line(line)
            except OSError:
                stale.append(client)

        if stale:
            with self.clients_lock:
                for client in stale:
                    self.clients.discard(client)

    def handle_uart_bytes(self, raw_bytes: bytes) -> None:
        for line in render_uart_messages(raw_bytes, emit_binary=self.emit_binary):
            print(f"{_now()} uart rx: {line}")
            self.broadcast(line)


class GatewayRequestHandler(socketserver.StreamRequestHandler):
    def setup(self) -> None:
        super().setup()
        self.write_lock = threading.Lock()

    def handle(self) -> None:
        client_host, client_port = self.client_address
        self.server.register_client(self)  # type: ignore[attr-defined]
        print(f"{_now()} client connected: {client_host}:{client_port}")

        try:
            while True:
                raw = self.rfile.readline()
                if not raw:
                    break

                text = raw.decode("utf-8", errors="replace").strip()
                if not text:
                    continue

                print(f"{_now()} net rx: {text}")

                try:
                    normalized = normalize_outgoing_command(text)
                    sent = self.server.bridge.send(normalized)  # type: ignore[attr-defined]
                except Exception as exc:
                    response = f"ERR,{exc}"
                    self.send_line(response)
                    print(f"{_now()} net tx: {response}")
                    continue

                response = f"OK,{normalized},{sent}"
                self.send_line(response)
                print(f"{_now()} uart tx: {normalized}")
                print(f"{_now()} net tx: {response}")
        finally:
            self.server.unregister_client(self)  # type: ignore[attr-defined]
            print(f"{_now()} client disconnected: {client_host}:{client_port}")

    def send_line(self, line: str) -> None:
        with self.write_lock:
            self.wfile.write((line + "\n").encode("utf-8"))
            self.wfile.flush()


def render_uart_messages(raw_bytes: bytes, emit_binary: bool):
    for part_type, part_bytes in split_uart_chunk(raw_bytes):
        if part_type == "binary":
            if emit_binary:
                yield f"BINARY,{part_bytes.hex(' ')}"
            continue

        text = part_bytes.decode("utf-8", errors="replace").strip()
        if not text:
            continue

        parsed = parse_incoming_message(text)
        if isinstance(parsed, TouchEvent):
            if parsed.value is None:
                yield f"EVENT,TOUCH,{parsed.name}"
            else:
                yield f"EVENT,TOUCH,{parsed.name},{parsed.value}"
        elif isinstance(parsed, AckMessage):
            yield f"ACK,{parsed.text}"
        elif isinstance(parsed, ReadyMessage):
            yield f"READY,{parsed.text}"
        elif isinstance(parsed, UnknownMessage):
            yield f"TEXT,{parsed.text}"


def parse_args():
    parser = argparse.ArgumentParser(
        description="RDK X5 TCP gateway for UART3 LED/touch protocol"
    )
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--uart-device", default=UART_DEVICE)
    parser.add_argument("--baudrate", type=int, default=BAUDRATE)
    parser.add_argument(
        "--line-ending",
        choices=sorted(LINE_ENDINGS),
        default=DEFAULT_LINE_ENDING,
        help="UART line ending appended after each command",
    )
    parser.add_argument(
        "--idle-timeout",
        type=float,
        default=DEFAULT_IDLE_TIMEOUT,
        help="Flush UART RX buffer when idle for this many seconds",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate commands and reply OK/ERR without writing to UART3",
    )
    parser.add_argument(
        "--no-binary",
        action="store_true",
        help="Do not forward binary UART frames to network clients",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    bridge = SerialBridge(
        uart_device=args.uart_device,
        baudrate=args.baudrate,
        line_ending=args.line_ending,
        idle_timeout=args.idle_timeout,
        dry_run=args.dry_run,
    )

    with ThreadedTCPServer(
        (args.host, args.port),
        GatewayRequestHandler,
        bridge=bridge,
        emit_binary=not args.no_binary,
    ) as server:
        bridge.start_reader(server.handle_uart_bytes)
        print(
            f"{_now()} gateway listen on {args.host}:{args.port} "
            f"(dry_run={args.dry_run}, uart={args.uart_device}, baudrate={args.baudrate}, "
            f"line_ending={args.line_ending}, emit_binary={not args.no_binary})"
        )
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print(f"\n{_now()} gateway stopped")
        finally:
            bridge.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
