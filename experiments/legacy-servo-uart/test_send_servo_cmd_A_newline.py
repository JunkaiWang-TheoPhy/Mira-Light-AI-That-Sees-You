#!/usr/bin/env python3

import sys
import time

from servo_uart_protocol import build_servo_command, send_packet


SERVO_ID = 0
P = 10.0
I = 0.0
D = 0.0


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <angle>")
        return 1

    angle = float(sys.argv[1])
    packet = build_servo_command(SERVO_ID, P, I, D, angle)

    t0 = time.perf_counter()
    sent = send_packet(packet, line_ending="\n")
    t1 = time.perf_counter()

    print(f"Send: {packet}\\n")
    print(f"Sent bytes: {sent}")
    print(f"Local send time: {(t1 - t0) * 1000:.3f} ms")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
