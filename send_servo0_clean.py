#!/usr/bin/env python3

import serial


UART_DEVICE = "/dev/ttyS1"
BAUDRATE = 115200
COMMAND = "0,1.5,0.1,0.01,120"


def main():
    ser = serial.Serial(UART_DEVICE, BAUDRATE, timeout=1)
    try:
        print(f"Open: {UART_DEVICE} @ {BAUDRATE}")
        print(f"Send: {COMMAND}")
        sent = ser.write(COMMAND.encode("utf-8"))
        ser.flush()
        print(f"Sent bytes: {sent}")
    finally:
        ser.close()


if __name__ == "__main__":
    main()
