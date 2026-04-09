#!/usr/bin/env python3

from dataclasses import dataclass
import re
from typing import Iterable, List


ID_MIN = 0
ID_MAX = 254
PWM_MIN = 500
PWM_MAX = 2500
TIME_MIN = 0
TIME_MAX = 9999

_FRAME_RE = re.compile(r"#(?P<servo_id>\d{3})P(?P<pwm>\d{4})T(?P<time_ms>\d{4})!")


@dataclass(frozen=True)
class ServoMove:
    servo_id: int
    pwm: int
    time_ms: int

    def encode(self) -> str:
        _validate_servo_id(self.servo_id)
        _validate_pwm(self.pwm)
        _validate_time_ms(self.time_ms)
        return f"#{self.servo_id:03d}P{self.pwm:04d}T{self.time_ms:04d}!"


def _validate_servo_id(servo_id: int) -> None:
    if not ID_MIN <= servo_id <= ID_MAX:
        raise ValueError(f"servo_id out of range: {servo_id}")


def _validate_pwm(pwm: int) -> None:
    if not PWM_MIN <= pwm <= PWM_MAX:
        raise ValueError(f"pwm out of range: {pwm}")


def _validate_time_ms(time_ms: int) -> None:
    if not TIME_MIN <= time_ms <= TIME_MAX:
        raise ValueError(f"time_ms out of range: {time_ms}")


def build_servo_packet(servo_id: int, pwm: int, time_ms: int) -> str:
    return ServoMove(servo_id, pwm, time_ms).encode()


def build_multi_servo_packet(moves: Iterable[ServoMove]) -> str:
    move_list = list(moves)
    if len(move_list) < 2:
        raise ValueError("multi-servo packet requires at least 2 moves")
    return "{" + "".join(move.encode() for move in move_list) + "}"


def parse_servo_packet(packet: str) -> List[ServoMove]:
    text = packet.strip()
    if not text:
        raise ValueError("empty packet")

    if text.startswith("{") or text.endswith("}"):
        return _parse_group_packet(text)
    return [_parse_single_frame(text)]


def normalize_servo_packet(packet: str) -> str:
    moves = parse_servo_packet(packet)
    if len(moves) == 1:
        return moves[0].encode()
    return build_multi_servo_packet(moves)


def _parse_group_packet(packet: str) -> List[ServoMove]:
    if not (packet.startswith("{") and packet.endswith("}")):
        raise ValueError(f"invalid grouped packet: {packet}")

    body = packet[1:-1]
    if not body:
        raise ValueError("empty grouped packet")

    moves: List[ServoMove] = []
    index = 0
    while index < len(body):
        match = _FRAME_RE.match(body, index)
        if match is None:
            raise ValueError(f"invalid grouped packet: {packet}")

        moves.append(_match_to_move(match))
        index = match.end()

    if len(moves) < 2:
        raise ValueError("grouped packet requires at least 2 servo frames")
    return moves


def _parse_single_frame(frame: str) -> ServoMove:
    match = _FRAME_RE.fullmatch(frame)
    if match is None:
        raise ValueError(f"invalid servo frame: {frame}")
    return _match_to_move(match)


def _match_to_move(match: re.Match[str]) -> ServoMove:
    move = ServoMove(
        servo_id=int(match.group("servo_id")),
        pwm=int(match.group("pwm")),
        time_ms=int(match.group("time_ms")),
    )
    # Range validation happens in encode().
    move.encode()
    return move
