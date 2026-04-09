#!/usr/bin/env python3

import sys

from servo_uart_protocol import build_servo_command, send_packet


SERVO_ID = 0
P = 1.5
I = 0.0
D = 0.01


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <angle>")
        return 1

    angle = float(sys.argv[1])
    packet = build_servo_command(SERVO_ID, P, I, D, angle)

    print(f"Send: {packet}")
    sent = send_packet(packet)
    print(f"Sent bytes: {sent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
