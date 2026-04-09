#!/usr/bin/env python3

import time

import serial

from servo_uart_protocol import BAUDRATE, UART_DEVICE, parse_packet


def main():
    print(f"Listen: {UART_DEVICE} @ {BAUDRATE}")
    print("Press Ctrl+C to stop")

    buffer = bytearray()
    last_rx_time = 0.0
    with serial.Serial(UART_DEVICE, BAUDRATE, timeout=0.2) as ser:
        while True:
            chunk = ser.read(ser.in_waiting or 1)
            if not chunk:
                if buffer and (time.monotonic() - last_rx_time) > 0.2:
                    text = bytes(buffer).decode("utf-8", errors="replace").strip()
                    buffer.clear()
                    if not text:
                        continue

                    print(f"Raw   : {text}")
                    try:
                        parsed = parse_packet(text)
                        print(f"Parsed: {parsed}")
                    except ValueError as exc:
                        print(f"Parsed: {exc}")
                continue

            last_rx_time = time.monotonic()
            buffer.extend(chunk)
            while True:
                newline_index = -1
                for marker in (b"\r\n", b"\n", b"\r"):
                    marker_index = buffer.find(marker)
                    if marker_index != -1:
                        newline_index = marker_index
                        marker_bytes = len(marker)
                        break

                if newline_index == -1:
                    break

                raw = bytes(buffer[:newline_index])
                del buffer[: newline_index + marker_bytes]

                text = raw.decode("utf-8", errors="replace").strip()
                if not text:
                    continue

                print(f"Raw   : {text}")
                try:
                    parsed = parse_packet(text)
                    print(f"Parsed: {parsed}")
                except ValueError as exc:
                    print(f"Parsed: {exc}")


if __name__ == "__main__":
    main()
