# UART1 Servo Sender

This script sends bus-servo commands over RDK X5 `uart1`.

Default UART settings:

- device: `/dev/ttyS1`
- baudrate: `115200`
- line ending: `\n`

## Wiring

- RDK X5 `pin 8` (`UART1_TXD`) -> servo controller `RX`
- RDK X5 `pin 10` (`UART1_RXD`) <- servo controller `TX` if needed
- RDK X5 `GND` -> servo controller `GND`

## Example Commands

Send one full raw packet:

```bash
python3 experiments/bus-servo/send_uart1_servo_cmd.py raw "#003P1500T1000!"
```

Send one generated packet:

```bash
python3 experiments/bus-servo/send_uart1_servo_cmd.py single 3 1500 1000
```

Send one multi-servo packet:

```bash
python3 experiments/bus-servo/send_uart1_servo_cmd.py raw "{#001P2000T1000!#003P0833T2000!}"
```

If your lower controller does not want a line ending, append:

```bash
--line-ending none
```
