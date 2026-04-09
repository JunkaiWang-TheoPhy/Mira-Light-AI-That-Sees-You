#!/usr/bin/env python3

import argparse

import serial

from bus_servo_protocol import build_servo_packet, normalize_servo_packet


DEFAULT_DEVICE = "/dev/ttyS1"
DEFAULT_BAUDRATE = 115200
DEFAULT_LINE_ENDING = "lf"
LINE_ENDINGS = {
    "none": "",
    "lf": "\n",
    "crlf": "\r\n",
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Send bus-servo command over RDK X5 UART1 (/dev/ttyS1)"
    )
    parser.add_argument("--device", default=DEFAULT_DEVICE, help="UART device path")
    parser.add_argument("--baudrate", type=int, default=DEFAULT_BAUDRATE, help="UART baudrate")
    parser.add_argument(
        "--line-ending",
        choices=sorted(LINE_ENDINGS),
        default=DEFAULT_LINE_ENDING,
        help="Line ending appended after the command",
    )

    subparsers = parser.add_subparsers(dest="mode", required=True)

    parser_raw = subparsers.add_parser("raw", help="Send a full servo protocol packet")
    parser_raw.add_argument("packet", help="Example: #003P1500T1000! or {#001P2000T1000!#003P0833T2000!}")

    parser_single = subparsers.add_parser("single", help="Build and send one servo frame")
    parser_single.add_argument("servo_id", type=int, help="0-254")
    parser_single.add_argument("pwm", type=int, help="500-2500")
    parser_single.add_argument("time_ms", type=int, help="0-9999")

    return parser.parse_args()


def build_packet(args) -> str:
    if args.mode == "raw":
        return normalize_servo_packet(args.packet)
    if args.mode == "single":
        return build_servo_packet(args.servo_id, args.pwm, args.time_ms)
    raise ValueError(f"unsupported mode: {args.mode}")


def main():
    args = parse_args()
    packet = build_packet(args)
    payload = f"{packet}{LINE_ENDINGS[args.line_ending]}".encode("ascii")

    with serial.Serial(args.device, args.baudrate, timeout=1) as ser:
        sent = ser.write(payload)
        ser.flush()

    print(f"Device      : {args.device}")
    print(f"Baudrate    : {args.baudrate}")
    print(f"Line ending : {args.line_ending}")
    print(f"Send        : {packet}")
    print(f"Sent bytes  : {sent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
