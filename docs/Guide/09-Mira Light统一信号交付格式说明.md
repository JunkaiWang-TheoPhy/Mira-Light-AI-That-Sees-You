# Unified Signal Delivery Format

Updated: 2026-04-09

## 文档目的

这份文档把 `Mira Light` 当前对外和对设备相关的三类信号统一收口成一份正式说明：

1. `9527` 原始 TCP 总线舵机帧
2. `40` 灯 `pixelSignals`
3. 头部电容 `headCapacitive`

它要解决的是一个现实问题：

- `9527` 原始舵机帧已经有单独文档
- `40` 灯和电容信息分散在 mock 排练、导演台和代码里
- 调用方容易误以为这些信号都走同一种协议

统一结论是：

- 四关节底层运动信号可以走 raw TCP 舵机帧
- `40` 灯 `pixelSignals` 和 `headCapacitive` 不走 `9527` raw TCP 帧
- `40` 灯和电容当前通过 HTTP 设备接口 / bridge 接口表达

## 一句话结论

```text
上层调用方
-> bridge HTTP / 导演台 HTTP
-> runtime
-> 四关节动作最终可下沉为 9527 raw TCP 舵机帧
-> 灯效与电容仍通过 HTTP 设备状态面表达
```

也就是说：

- `#003P1500T1000!` 这类帧只负责舵机运动
- `pixelSignals` 和 `headCapacitive` 由 `/led`、`/sensors`、`/status` 这些 HTTP 结构携带

## 信号总表

| 信号类别 | 当前格式 | 承载层 | 是否走 9527 raw TCP |
| --- | --- | --- | --- |
| 四关节目标动作 | `#IDPWWWWTTTT!` / `{...}` | raw TCP transport | 是 |
| 四关节语义控制 | JSON：`mode + servo1~servo4` | bridge / HTTP device | 否 |
| 40 灯逐像素信号 | JSON：`pixels` / `pixelSignals` | HTTP device / mock / status | 否 |
| 头部电容 | JSON：`headCapacitive: 0|1` | HTTP device / mock / bridge | 否 |
| 汇总设备状态 | JSON：`servos + sensors + led` | HTTP device / bridge | 否 |

## 1. 9527 原始 TCP 舵机帧

### 1.1 目标地址

当前联调目标：

```text
tcp://192.168.31.10:9527
```

### 1.2 单舵机控制帧

格式：

```text
#000P1500T1000!
```

严格规则：

- `ID` 范围：`000-254`
- `ID` 必须始终是 `3` 位，不足补 `0`
- `PWM` 范围：`0500-2500`
- `PWM` 必须始终是 `4` 位，不足补 `0`
- `TIME` 范围：`0000-9999`
- `TIME` 必须始终是 `4` 位，不足补 `0`

### 1.3 多舵机控制帧

格式：

```text
{#000P1602T1000!#001P2500T0000!#002P1500T1000!}
```

规则：

- 当同时下发 `2` 条或以上单舵机帧时，整条命令必须包在 `{}` 里
- 花括号内部只能是若干条合法单帧直接拼接

## 2. 设备 HTTP / Bridge HTTP 语义面

raw TCP 舵机帧只解决“怎么动四个关节”。

完整设备面还包括：

- 40 灯状态
- 电容状态
- 动作列表 / 动作播放状态
- 汇总状态读取

这些信息当前统一通过 HTTP JSON 表达。

### 2.1 统一口径

- `/status`：正式统一读取面，只读 `servos + sensors + led`
- 灯光写入：统一发 `pixels`
- 灯光读取：统一看 `pixelSignals`
- `headCapacitive`：只接受 `0 | 1`
- `/health`：只做健康检查和快照，不拿它当正式状态面

## 3. 对这个仓库的意义

这份文档最重要的作用不是“再讲一份协议”，而是把当前仓库里最容易混淆的三件事拆开：

- 舵机怎么下发
- 40 灯怎么表达
- 电容状态怎么读写

这样 mock 排练、bridge 联调、现场控制三边就能统一口径。
