#!/usr/bin/env python3

import time

import serial

from servo_uart_protocol import BAUDRATE, UART_DEVICE, build_servo_command


SERVO_ID = 0
P = 1.5
I = 0.0
D = 0.01


def main():
    print(f"Open: {UART_DEVICE} @ {BAUDRATE}")
    print("Input angle and press Enter. Type q to quit.")

    with serial.Serial(UART_DEVICE, BAUDRATE, timeout=1) as ser:
        while True:
            raw = input("Angle> ").strip()
            if raw.lower() in {"q", "quit", "exit"}:
                break
            if not raw:
                continue

            try:
                angle = float(raw)
            except ValueError:
                print("Invalid angle")
                continue

            packet = build_servo_command(SERVO_ID, P, I, D, angle)
            t0 = time.perf_counter()
            sent = ser.write(packet.encode("utf-8"))
            ser.flush()
            t1 = time.perf_counter()

            print(f"Send: {packet}")
            print(f"Sent bytes: {sent}")
            print(f"Local send time: {(t1 - t0) * 1000:.3f} ms")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
