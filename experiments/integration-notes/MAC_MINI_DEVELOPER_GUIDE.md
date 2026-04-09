# Mac mini Developer Guide

## Overview

当前系统链路如下：

- `Mac mini`：大模型、策略、业务逻辑
- `RDK X5`：TCP <-> UART 网关
- `下位机`：舵机、灯光、触摸传感器

Mac mini **不要直接处理 UART**，只需要通过 TCP 连到 RDK X5：

- 舵机网关：`9527`
- 灯光/触摸网关：`9528`

两条链路互相独立，可以分别连接、分别发送。

## RDK X5 Side

联调前，先在 RDK X5 上启动对应网关。

### Servo Gateway

```bash
python3 experiments/bus-servo/bus_servo_gateway.py --uart-device /dev/ttyS1 --baudrate 115200
```

说明：

- UART：`/dev/ttyS1`
- TCP 端口：`9527`
- 默认不加行结束符

### LED/Touch Gateway

推荐先用不转发二进制帧的模式，Mac mini 侧更清爽：

```bash
python3 experiments/uart3-led/uart3_led_gateway.py --uart-device /dev/ttyS3 --baudrate 115200 --no-binary
```

说明：

- UART：`/dev/ttyS3`
- TCP 端口：`9528`
- 默认每条 UART 命令后自动补 `\n`

注意：

- `uart3_led_gateway.py` 启动后，不要再同时运行别的 `ttyS3` 脚本
- 一个 UART 设备同一时间只能被一个进程独占

## TCP Protocol

两条 TCP 链路都使用：

- 编码：`UTF-8`
- 分隔：**每行一条消息**
- 建议：Mac mini 使用**长连接**

也就是说：

- 发命令时，末尾加 `\n`
- 读回包时，按行读取

## Servo API

### Connection

- Host：`<RDK_X5_IP>`
- Port：`9527`

### Send Format

单舵机：

```text
#003P1500T1000!
```

多舵机：

```text
{#001P2000T1000!#003P0833T2000!}
```

字段说明：

- `#` 和 `!`：固定格式
- `ID`：`000-254`，必须 3 位
- `P`：`0500-2500`，必须 4 位
- `T`：`0000-9999`，必须 4 位，单位 ms

示例：

```text
#003P1500T1000!
{#001P2000T1000!#003P0833T2000!}
```

### Servo Network Response

发送成功：

```text
OK,#003P1500T1000!,16
```

含义：

- `OK`
- 规范化后的包
- 实际写入 UART 的字节数

发送失败：

```text
ERR,invalid servo frame: #3P1500T1000!
```

### Servo Notes

- 舵机网关当前只负责**下发**
- Mac mini 侧把 `OK` 视为“X5 已成功写入 UART”
- `OK` 不等于“下位机已经执行完成”

## LED/Touch API

### Connection

- Host：`<RDK_X5_IP>`
- Port：`9528`

### Send Format

支持以下命令。

全部灯：

```text
ALL,R,G,B,BRI
```

单个灯：

```text
ONE,grp,idx,R,G,B,BRI
```

全局亮度：

```text
BRI,val
```

关闭所有灯：

```text
OFF
```

触摸阈值：

```text
THR,val
```

帮助：

```text
HELP
```

示例：

```text
ALL,255,255,255,255
ONE,0,0,0,255,0,200
BRI,50
OFF
THR,300
HELP
```

字段约束：

- `R/G/B/BRI`：`0-255`
- `grp=0`：外圈，`idx 0-23`
- `grp=1`：内圈，`idx 0-15`
- `THR,val`：`val >= 0`

### LED/Touch Network Response

命令发送成功：

```text
OK,ALL,255,255,255,255,20
```

命令发送失败：

```text
ERR,unsupported LED command: ALL,255,255
```

### Async Events From Lower Controller

Mac mini 连接 `9528` 后，除了收到命令的 `OK/ERR`，还会持续收到下位机主动上报的事件。

触摸事件：

```text
EVENT,TOUCH,PRESS,208
EVENT,TOUCH,HOLD,221
EVENT,TOUCH,RELEASE,215
```

下位机文本应答：

```text
ACK,OK ALL 255,255,255,255
READY,*Ready. Binary protocol active (UART2 + USB Serial).
TEXT,...
```

如果 X5 启动时**没有**加 `--no-binary`，还可能收到：

```text
BINARY,7e 81 00 03 03 00 dd 5c
```

建议：

- 正常业务联调时，优先让 X5 用 `--no-binary`
- 这样 Mac mini 只处理文本事件就够了

### THR Behavior

`THR,val` 只是在下位机里设置触摸阈值，不是“开始接收”的开关。

设置后：

- 触摸事件会继续异步上报
- 同时仍然可以发送 `ALL`、`ONE`、`BRI`、`OFF`

也就是说，下面这种顺序是正常的：

```text
THR,300
ALL,255,255,255,255
ONE,0,0,0,255,0,200
BRI,50
OFF
```

## Recommended Mac mini Client Pattern

建议：

- 舵机：一个长连接到 `9527`
- 灯光/触摸：一个长连接到 `9528`
- 每条命令单独一行
- 单独线程或协程持续读回包

不要每发一条命令就新建一次 TCP 连接，长连接更稳。

## Python Example

下面是一个最小 Python 示例，适合 Mac mini 开发者直接接入。

```python
import socket
import threading


class LineClient:
    def __init__(self, host: str, port: int):
        self.sock = socket.create_connection((host, port))
        self.file = self.sock.makefile("rwb")

    def send_line(self, text: str) -> None:
        self.file.write((text + "\n").encode("utf-8"))
        self.file.flush()

    def read_loop(self, label: str) -> None:
        while True:
            line = self.file.readline()
            if not line:
                print(f"{label} disconnected")
                break
            print(f"{label} <= {line.decode('utf-8', errors='replace').rstrip()}")


RDK_X5_IP = "192.168.31.50"

servo = LineClient(RDK_X5_IP, 9527)
led = LineClient(RDK_X5_IP, 9528)

threading.Thread(target=servo.read_loop, args=("SERVO",), daemon=True).start()
threading.Thread(target=led.read_loop, args=("LED",), daemon=True).start()

servo.send_line("#003P1500T1000!")
servo.send_line("{#001P2000T1000!#003P0833T2000!}")

led.send_line("THR,300")
led.send_line("ALL,255,255,255,255")
led.send_line("ONE,0,0,0,255,0,200")
led.send_line("BRI,50")
led.send_line("OFF")

input("Press Enter to exit...\n")
```

## Testing With netcat

如果只想快速手测。

舵机：

```bash
printf '#003P1500T1000!\n' | nc <RDK_X5_IP> 9527
```

灯光：

```bash
printf 'ALL,255,255,255,255\n' | nc <RDK_X5_IP> 9528
```

如果想持续看灯光/触摸事件，更建议写 Python 长连接客户端，不建议长期依赖 `nc`。

## Common Issues

### 1. 连接上后立刻断开

如果使用：

```bash
printf '...\n' | nc <RDK_X5_IP> 9528
```

这是正常现象。因为 `nc` 发完就退出，所以 X5 日志会显示：

- `client connected`
- `client disconnected`

### 2. LED 网关没回事件

先确认：

- RDK X5 上跑的是 `uart3_led_gateway.py`
- 没有别的脚本占用 `/dev/ttyS3`
- 下位机确实在往 UART3 回传数据

### 3. 持续收到 `HOLD`

通常表示当前阈值设置下，传感器一直被判定为“按住”。

可以尝试：

- 调整 `THR,val`
- 重启下位机回到默认阈值

### 4. Servo 返回 `OK` 但舵机没动

说明：

- `Mac mini -> X5 TCP`
- `X5 -> UART1`

这两段大概率是通的。

需要再检查：

- 下位机是否真的接到 `UART1`
- 波特率是否一致
- 舵机协议本身是否正确

## Interface Summary

### Servo

- TCP: `9527`
- Send: raw bus-servo packet
- Receive: `OK,...` or `ERR,...`

### LED/Touch

- TCP: `9528`
- Send: `ALL/ONE/BRI/OFF/THR/HELP`
- Receive:
  - `OK,...`
  - `ERR,...`
  - `EVENT,TOUCH,...`
  - `ACK,...`
  - `READY,...`
  - optional `BINARY,...`
