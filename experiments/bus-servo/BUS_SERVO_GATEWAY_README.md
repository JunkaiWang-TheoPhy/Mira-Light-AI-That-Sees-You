# Bus Servo Gateway

## Files

- `bus_servo_protocol.py`: build and validate `#000P1500T1000!` packets
- `bus_servo_gateway.py`: TCP gateway running on RDK X5

## Packet Examples

- Single servo: `#003P1500T1000!`
- Multi servo: `{#001P2000T1000!#003P0833T2000!}`

## Start Gateway On RDK X5

Dry-run mode only validates packets from Mac mini and replies `OK` or `ERR`.

```bash
python3 experiments/bus-servo/bus_servo_gateway.py --dry-run
```

When the lower controller is ready, switch to UART forwarding:

```bash
python3 experiments/bus-servo/bus_servo_gateway.py --uart-device /dev/ttyS1 --baudrate 115200
```

If the lower controller requires a line ending on UART, add:

```bash
python3 experiments/bus-servo/bus_servo_gateway.py --uart-device /dev/ttyS1 --baudrate 115200 --line-ending lf
```

## Send From Mac mini

Send one single-servo command:

```bash
printf '#003P1500T1000!\n' | nc <RDK_X5_IP> 9527
```

Send one multi-servo command:

```bash
printf '{#001P2000T1000!#003P0833T2000!}\n' | nc <RDK_X5_IP> 9527
```

Successful replies look like:

```text
OK,#003P1500T1000!,16
OK,{#001P2000T1000!#003P0833T2000!},36
```

Invalid packets return:

```text
ERR,<reason>
```
