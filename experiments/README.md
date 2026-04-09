# RDK X5 Hardware Experiments

This directory collects the older UART, bus-servo, GPIO/PWM, and camera
prototype scripts that were previously stored at the repository root.

They are intentionally kept outside the main release runtime because they serve
different purposes from the current `scripts/`, `tools/`, and `web/` paths:

- quick hardware bring-up
- protocol probing
- board-level loopback tests
- one-off transport experiments
- lower-level debugging on RDK X5

These files are still useful, but they are not part of the main release entry
surface for Mira Light.

## Layout

```text
experiments/
├── README.md
├── bus-servo/
├── uart3-led/
├── legacy-servo-uart/
├── camera-prototypes/
├── gpio-pwm/
└── integration-notes/
```

## Directory Guide

### `bus-servo/`

Text-frame tooling for the TCP-to-UART bus-servo path on RDK X5.

Key files:

- `bus_servo_protocol.py`
- `bus_servo_gateway.py`
- `send_uart1_servo_cmd.py`
- `BUS_SERVO_GATEWAY_README.md`
- `UART1_SERVO_README.md`

Use this area when you need to validate `#000P1500T1000!` style packets, UART1
forwarding, or the `9527` servo gateway path.

### `uart3-led/`

Text-protocol tooling for the LED and touch path on `uart3`.

Key files:

- `uart3_led_protocol.py`
- `uart3_led_gateway.py`
- `send_uart3_led_cmd.py`
- `listen_uart3_led.py`
- `test_uart3_loopback.py`

Use this area when you need to validate `ALL / ONE / BRI / OFF / THR / HELP`
commands, touch-event parsing, or the `9528` gateway path.

### `legacy-servo-uart/`

Older direct-UART command experiments for a different servo / LED packet family.

Key files:

- `servo_uart_protocol.py`
- `send_servo0.py`
- `send_servo0_clean.py`
- `test_recv_uart_packets.py`
- `test_send_servo_cmd.py`
- `test_send_led_speed_cmd.py`
- `test_send_led_thr_cmd.py`

This area is kept mainly for historical comparison and low-level debugging. It
is not the primary release path.

### `camera-prototypes/`

Early camera preview, sender, receiver, and RTSP test scripts.

Key files:

- `cam_preview.py`
- `cam_receiver.py`
- `cam_sender.py`
- `rtsp_server.py`

These scripts predate the more structured receiver / vision flow now used in
the release runtime.

### `gpio-pwm/`

Low-level GPIO and PWM experiments for direct pin control on RDK X5.

Key files:

- `simple_out.py`
- `simple_pwm.py`
- `servo_test.py`
- `testt.py`

Use this area only for board-level PWM / GPIO bring-up and manual hardware
validation.

### `integration-notes/`

Supporting notes that describe how these experiment paths were used during
earlier bring-up.

Key file:

- `MAC_MINI_DEVELOPER_GUIDE.md`

## How To Use These Files Safely

- Prefer the main release runtime under `scripts/` unless you are explicitly
  doing low-level hardware debugging.
- Treat these scripts as lab utilities, not as stable product interfaces.
- Avoid running multiple scripts against the same UART device at the same time.
- Expect device-specific assumptions such as `/dev/ttyS1`, `/dev/ttyS3`, RDK X5
  pinmux settings, or direct `sysfs` PWM access.

## Relation To The Main Repository

The release-oriented code paths still live in:

- `scripts/`
- `tools/mira_light_bridge/`
- `config/`
- `docs/`
- `web/`

Those directories define the current runtime, bridge, console, safety layer,
and demo-facing workflow.

This `experiments/` directory exists to keep the lower-level hardware lab files
available without leaving the repository root crowded or making these scripts
look like first-class runtime entrypoints.
