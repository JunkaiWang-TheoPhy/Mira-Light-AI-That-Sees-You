#!/usr/bin/env python3

import argparse
import os
import time

import serial


DEFAULT_DEVICE = "/dev/ttyS3"
DEFAULT_BAUDRATE = 115200
DEFAULT_PAYLOAD = "AA55"
DEFAULT_INTERVAL = 1.0
DEFAULT_TIMEOUT = 1.0


def parse_args():
    parser = argparse.ArgumentParser(
        description="RDK X5 secondary UART (uart3) loopback test"
    )
    parser.add_argument("--device", default=DEFAULT_DEVICE, help="UART device path")
    parser.add_argument(
        "--baudrate",
        type=int,
        default=DEFAULT_BAUDRATE,
        help="UART baudrate",
    )
    parser.add_argument(
        "--payload",
        default=DEFAULT_PAYLOAD,
        help="ASCII payload sent every round",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=DEFAULT_INTERVAL,
        help="Delay between rounds in seconds",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help="Read timeout in seconds",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=0,
        help="Number of rounds, 0 means infinite",
    )
    return parser.parse_args()


def print_banner(args):
    print("RDK X5 uart3 loopback test")
    print(f"Device   : {args.device}")
    print(f"Baudrate : {args.baudrate}")
    print(f"Payload  : {args.payload}")
    print("")
    print("Wiring for RDK X5 40PIN:")
    print("  pin 3  <-> pin 5")
    print("")
    print("Pinmux note:")
    print("  On RDK X5, uart3 and i2c5 share the same 40PIN pins.")
    print("  pin 3 = I2C5_SDA / UART3_TXD")
    print("  pin 5 = I2C5_SCL / UART3_RXD")
    print("  Before testing, switch pinmux to uart3 and reboot.")
    print("")


def run_loopback(args):
    payload = args.payload.encode("utf-8")

    if not os.path.exists(args.device):
        print(f"UART device not found: {args.device}")
        return 1

    try:
        ser = serial.Serial(args.device, args.baudrate, timeout=args.timeout)
    except Exception as exc:
        print(f"Open serial failed: {exc}")
        return 1

    print(ser)
    print("Starting loopback now! Press CTRL+C to exit")

    try:
        round_index = 0
        while args.count == 0 or round_index < args.count:
            round_index += 1
            ser.reset_input_buffer()

            sent = ser.write(payload)
            ser.flush()
            received = ser.read(sent)

            sent_text = payload.decode("utf-8", errors="replace")
            recv_text = received.decode("utf-8", errors="replace")
            ok = received == payload

            print(f"[{round_index}] Send: {sent_text}")
            print(f"[{round_index}] Recv: {recv_text}")
            print(f"[{round_index}] Match: {'PASS' if ok else 'FAIL'}")

            if not ok:
                print(f"[{round_index}] Sent hex: {payload.hex(' ')}")
                print(f"[{round_index}] Recv hex: {received.hex(' ')}")

            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nStopped by user")
    finally:
        ser.close()

    return 0


def main():
    args = parse_args()
    print_banner(args)
    return run_loopback(args)


if __name__ == "__main__":
    raise SystemExit(main())
