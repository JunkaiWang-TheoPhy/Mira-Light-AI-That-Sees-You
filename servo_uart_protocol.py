#!/usr/bin/env python3

from dataclasses import dataclass

import serial


UART_DEVICE = "/dev/ttyS1"
BAUDRATE = 115200
LINE_ENDING = ""


@dataclass
class ServoCommand:
    servo_id: int
    p: float
    i: float
    d: float
    angle: float

    def encode(self) -> str:
        return f"S,{self.servo_id},{self.p},{self.i},{self.d},{self.angle}"


@dataclass
class LedSpeedCommand:
    speed: int

    def encode(self) -> str:
        return f"L,SPEED,{self.speed}"


@dataclass
class LedThresholdCommand:
    threshold: int

    def encode(self) -> str:
        return f"L,THR,{self.threshold}"


@dataclass
class TouchPressEvent:
    value: int


@dataclass
class TouchReleaseEvent:
    value: int


@dataclass
class TouchHoldEvent:
    value: int
    pink_percent: int
    beat_percent: int


@dataclass
class ServoAck:
    servo_id: int
    p: float
    i: float
    d: float
    angle: float


def build_servo_command(
    servo_id: int,
    p: float,
    i: float,
    d: float,
    angle: float,
) -> str:
    return ServoCommand(servo_id, p, i, d, angle).encode()


def build_led_speed_command(speed: int) -> str:
    return LedSpeedCommand(speed).encode()


def build_led_threshold_command(threshold: int) -> str:
    return LedThresholdCommand(threshold).encode()


def send_packet(
    packet: str,
    uart_device: str = UART_DEVICE,
    baudrate: int = BAUDRATE,
    line_ending: str = LINE_ENDING,
) -> int:
    payload = f"{packet}{line_ending}".encode("utf-8")
    with serial.Serial(uart_device, baudrate, timeout=1) as ser:
        sent = ser.write(payload)
        ser.flush()
        return sent


def parse_packet(packet: str):
    text = packet.strip()
    if not text:
        raise ValueError("empty packet")

    parts = text.split(",")
    if parts[:2] == ["EVT", "TOUCH_PRESS"] and len(parts) == 3:
        return TouchPressEvent(value=int(parts[2]))
    if parts[:2] == ["EVT", "TOUCH_RELEASE"] and len(parts) == 3:
        return TouchReleaseEvent(value=int(parts[2]))
    if parts[:2] == ["EVT", "TOUCH_HOLD"] and len(parts) == 5:
        return TouchHoldEvent(
            value=int(parts[2]),
            pink_percent=int(parts[3]),
            beat_percent=int(parts[4]),
        )
    if parts[:2] == ["OK", "S"] and len(parts) == 7:
        return ServoAck(
            servo_id=int(parts[2]),
            p=float(parts[3]),
            i=float(parts[4]),
            d=float(parts[5]),
            angle=float(parts[6]),
        )

    raise ValueError(f"unsupported packet: {text}")
