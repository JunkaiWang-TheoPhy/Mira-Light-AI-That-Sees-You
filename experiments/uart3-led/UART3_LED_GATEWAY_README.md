# UART3 LED Gateway

This gateway forwards LED/touch protocol traffic between Mac mini and the lower controller through RDK X5 `uart3`.

Only one process can hold `/dev/ttyS3` at a time.
Before starting this gateway, stop `listen_uart3_led.py` and any other UART3 test script.

Default network settings:

- host: `0.0.0.0`
- port: `9528`

Default UART settings:

- device: `/dev/ttyS3`
- baudrate: `115200`
- line ending: `\n`

## Start On RDK X5

Real UART forwarding:

```bash
python3 /home/sunrise/Desktop/uart3_led_gateway.py
```

Validation only, without writing to UART:

```bash
python3 /home/sunrise/Desktop/uart3_led_gateway.py --dry-run
```

If you want to suppress binary UART frames:

```bash
python3 /home/sunrise/Desktop/uart3_led_gateway.py --no-binary
```

## Send From Mac mini

Use a long TCP connection so Mac mini can both send commands and receive touch events.

Interactive test:

```bash
nc <RDK_X5_IP> 9528
```

Then type one command per line:

```text
ALL,255,255,255,255
ONE,0,0,0,255,0,200
BRI,50
OFF
THR,300
HELP
```

## Network Messages Returned To Mac mini

Command accepted:

```text
OK,ALL,255,255,255,255,20
```

Command rejected:

```text
ERR,unsupported LED command: ...
```

Touch events:

```text
EVENT,TOUCH,PRESS,208
EVENT,TOUCH,HOLD,203
EVENT,TOUCH,RELEASE,215
```

Lower-controller text messages:

```text
ACK,OK ALL 255,255,255,255
READY,*Ready. Binary protocol active (UART2 + USB Serial).
TEXT,some other text
```

Binary UART frames:

```text
BINARY,7e ff 00 03 01 00 ff 53
```
