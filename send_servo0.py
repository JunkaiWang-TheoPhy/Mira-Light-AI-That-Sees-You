#!/usr/bin/env python3

import os
import signal
import sys
import time

import serial


DEFAULT_DEVICE = "/dev/ttyS1"
DEFAULT_BAUDRATE = 115200
SERVO_COMMAND = "0,1.5,0.1,0.01,120"
DEFAULT_LINE_ENDING = "lf"
LINE_ENDINGS = {
    "none": "",
    "lf": "\n",
    "crlf": "\r\n",
}


def signal_handler(sig, frame):
    sys.exit(0)


def main():
    print("RDK X5 UART servo sender")
    print("List of enabled UART:")
    os.system("ls /dev/tty[a-zA-Z]*")

    uart_dev = input(
        f"Please enter the serial device [{DEFAULT_DEVICE}]: "
    ).strip() or DEFAULT_DEVICE
    baudrate_text = input(
        f"Please enter the baud rate [{DEFAULT_BAUDRATE}]: "
    ).strip()
    baudrate = int(baudrate_text) if baudrate_text else DEFAULT_BAUDRATE
    command = input(
        f"Please enter the command [{SERVO_COMMAND}]: "
    ).strip() or SERVO_COMMAND
    line_ending_key = input(
        f"Please enter the line ending [lf/crlf/none] [{DEFAULT_LINE_ENDING}]: "
    ).strip().lower() or DEFAULT_LINE_ENDING
    if line_ending_key not in LINE_ENDINGS:
        print(f"unsupported line ending: {line_ending_key}")
        return 1

    payload = f"{command}{LINE_ENDINGS[line_ending_key]}"

    try:
        ser = serial.Serial(uart_dev, baudrate, timeout=0.3)
    except Exception as exc:
        print(f"open serial failed: {exc}")
        return 1

    print(f"Open: {ser.port} @ {ser.baudrate}")
    print(f"Send: {command}")
    print(f"Line ending: {line_ending_key}")

    ser.reset_input_buffer()
    ser.reset_output_buffer()

    write_num = ser.write(payload.encode("utf-8"))
    ser.flush()
    print(f"Sent bytes: {write_num}")

    time.sleep(0.3)
    waiting = ser.in_waiting
    if waiting:
        received_bytes = ser.read(waiting)
        received_text = received_bytes.decode("utf-8", errors="replace")
        print(f"Recv text: {received_text}")
        print(f"Recv hex : {received_bytes.hex(' ')}")
    else:
        print("Recv: no data")

    ser.close()
    return 0


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    raise SystemExit(main())
