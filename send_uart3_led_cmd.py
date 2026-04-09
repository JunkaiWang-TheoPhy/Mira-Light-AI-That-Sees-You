#!/usr/bin/env python3

import argparse

from uart3_led_protocol import (
    AckMessage,
    BAUDRATE,
    DEFAULT_LINE_ENDING,
    ReadyMessage,
    UART_DEVICE,
    UnknownMessage,
    TouchEvent,
    build_all_command,
    build_bri_command,
    build_help_command,
    build_off_command,
    build_one_command,
    build_thr_command,
    parse_incoming_message,
    send_command,
)


def parse_args():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--device", default=UART_DEVICE, help="UART device path")
    common.add_argument("--baudrate", type=int, default=BAUDRATE, help="UART baudrate")
    common.add_argument(
        "--line-ending",
        choices=("none", "lf", "crlf"),
        default=DEFAULT_LINE_ENDING,
        help="Line ending appended after the command",
    )
    common.add_argument(
        "--read-reply",
        action="store_true",
        help="Read and print any data returned by the lower controller",
    )
    common.add_argument(
        "--reply-timeout",
        type=float,
        default=0.2,
        help="Reply wait time in seconds when --read-reply is enabled",
    )

    parser = argparse.ArgumentParser(
        description="Send LED/touch commands over RDK X5 uart3 (/dev/ttyS3)",
        parents=[common],
    )

    subparsers = parser.add_subparsers(dest="command_type", required=True)

    parser_all = subparsers.add_parser("all", help="Send ALL,R,G,B,BRI", parents=[common])
    parser_all.add_argument("r", type=int)
    parser_all.add_argument("g", type=int)
    parser_all.add_argument("b", type=int)
    parser_all.add_argument("bri", type=int)

    parser_one = subparsers.add_parser(
        "one",
        help="Send ONE,grp,idx,R,G,B,BRI",
        parents=[common],
    )
    parser_one.add_argument("grp", type=int, help="0=outer ring, 1=inner ring")
    parser_one.add_argument("idx", type=int, help="0-23 for grp0, 0-15 for grp1")
    parser_one.add_argument("r", type=int)
    parser_one.add_argument("g", type=int)
    parser_one.add_argument("b", type=int)
    parser_one.add_argument("bri", type=int)

    parser_bri = subparsers.add_parser("bri", help="Send BRI,val", parents=[common])
    parser_bri.add_argument("value", type=int)

    subparsers.add_parser("off", help="Send OFF", parents=[common])

    parser_thr = subparsers.add_parser("thr", help="Send THR,val", parents=[common])
    parser_thr.add_argument("value", type=int)

    subparsers.add_parser("helpcmd", help="Send HELP", parents=[common])

    return parser.parse_args()


def build_command(args) -> str:
    if args.command_type == "all":
        return build_all_command(args.r, args.g, args.b, args.bri)
    if args.command_type == "one":
        return build_one_command(args.grp, args.idx, args.r, args.g, args.b, args.bri)
    if args.command_type == "bri":
        return build_bri_command(args.value)
    if args.command_type == "off":
        return build_off_command()
    if args.command_type == "thr":
        return build_thr_command(args.value)
    if args.command_type == "helpcmd":
        return build_help_command()
    raise ValueError(f"unsupported command type: {args.command_type}")


def main():
    args = parse_args()
    command = build_command(args)

    print(f"Device      : {args.device}")
    print(f"Baudrate    : {args.baudrate}")
    print(f"Line ending : {args.line_ending}")
    print(f"Send        : {command}")

    sent, reply = send_command(
        command=command,
        uart_device=args.device,
        baudrate=args.baudrate,
        line_ending=args.line_ending,
        read_reply=args.read_reply,
        reply_timeout=args.reply_timeout,
    )

    print(f"Sent bytes  : {sent}")
    if args.read_reply:
        if reply:
            text = reply.strip()
            print(f"Reply       : {text}")
            parsed = parse_incoming_message(text)
            if isinstance(parsed, TouchEvent):
                if parsed.value is None:
                    print(f"Reply type  : {parsed.name}")
                else:
                    print(f"Reply type  : {parsed.name} ({parsed.value})")
            elif isinstance(parsed, AckMessage):
                print("Reply type  : ack")
            elif isinstance(parsed, ReadyMessage):
                print("Reply type  : ready")
            elif isinstance(parsed, UnknownMessage):
                print("Reply type  : unknown text")
        else:
            print("Reply       : no data")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
