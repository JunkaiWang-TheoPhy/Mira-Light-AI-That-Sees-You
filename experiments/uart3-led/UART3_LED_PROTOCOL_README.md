# UART3 LED Protocol

This script family sends the LED/touch text protocol over RDK X5 `uart3`.

Default UART settings:

- device: `/dev/ttyS3`
- baudrate: `115200`
- line ending: `\n`

## Files

- `uart3_led_protocol.py`: protocol builder and UART sender
- `send_uart3_led_cmd.py`: command line sender
- `listen_uart3_led.py`: continuous uart3 receiver

## Wiring

Remove the loopback wire first.

- RDK X5 `pin 3` (`UART3_TXD`) -> lower controller `RX`
- RDK X5 `pin 5` (`UART3_RXD`) <- lower controller `TX`
- RDK X5 `GND` -> lower controller `GND`

`uart3` and `i2c5` share the same 40PIN pins, so keep `uart3=okay` and `i2c5=disabled`.

## Example Commands

All 40 LEDs white full brightness:

```bash
python3 experiments/uart3-led/send_uart3_led_cmd.py all 255 255 255 255
```

All LEDs red half brightness:

```bash
python3 experiments/uart3-led/send_uart3_led_cmd.py all 255 0 0 128
```

Outer ring LED 0 green:

```bash
python3 experiments/uart3-led/send_uart3_led_cmd.py one 0 0 0 255 0 200
```

Inner ring LED 5 purple:

```bash
python3 experiments/uart3-led/send_uart3_led_cmd.py one 1 5 255 0 255 255
```

Set global brightness:

```bash
python3 experiments/uart3-led/send_uart3_led_cmd.py bri 50
```

Turn all LEDs off:

```bash
python3 experiments/uart3-led/send_uart3_led_cmd.py off
```

Set touch threshold:

```bash
python3 experiments/uart3-led/send_uart3_led_cmd.py thr 300
```

Ask device to print help:

```bash
python3 experiments/uart3-led/send_uart3_led_cmd.py helpcmd --read-reply
```

Continuously listen to data returned by the lower controller:

```bash
python3 experiments/uart3-led/listen_uart3_led.py
```

If you also want to see raw bytes in hex:

```bash
python3 experiments/uart3-led/listen_uart3_led.py --hex
```

If the lower controller returns text, you can print it with:

```bash
python3 experiments/uart3-led/send_uart3_led_cmd.py all 255 255 255 255 --read-reply
```

If your lower controller does not need a line ending, append:

```bash
--line-ending none
```
