# Mira Light: AI That Sees You

`#RedHackathon` `#小红书黑客松巅峰赛`

[English](./README.en.md)

**有些关心，不需要开口。**

Mira Light 是一个围绕四自由度智能灯构建的具身化 AI 交互项目。它尝试把
“看见你、理解你、回应你”从屏幕中的聊天框带到真实空间里，通过姿态、方向、
灯光与节奏表达一种低打扰但可感知的陪伴。

这个仓库不是单一功能 demo，也不是一组零散脚本。它是面向演示、排练与交付
的发布版主仓，覆盖从视觉输入到场景编排、从本地 bridge 到导演台、从 mock
排练到真机联调的完整链路。

## 项目定位

Mira Light 面向现场 Expo、导演式演示和技术交付场景，核心目标不是证明
“灯可以动”，而是证明：

```text
AI 可以先注意到你的出现
-> 解释你的位置与互动语境
-> 再用动作和灯光做出合适回应
```

仓库当前围绕这条链路组织：

```text
camera input
-> vision event extraction
-> scene selection
-> bridge / safety layer
-> ESP32 lamp motion + light response
-> optional embodied memory writeback
```

## Demo 核心体验

在展位前，Mira Light 希望让观众在几秒钟内理解一件事：这不是随机播放动作的
台灯，而是一个会先看见你、再回应你的实体系统。

典型交互包括：

- 你靠近，它醒来
- 你停下，它观察你
- 你移动，它跟随你
- 你互动，它表现亲近、开心或提醒
- 你离开，它目送你并回到休息状态

当前代表性场景见：

- [docs/mira-light-booth-scene-table.md](./docs/mira-light-booth-scene-table.md)
- [docs/mira-light-scene-implementation-index.md](./docs/mira-light-scene-implementation-index.md)
- [docs/release-scene-bundles.md](./docs/release-scene-bundles.md)

## 当前能力范围

仓库当前已具备以下发布级能力：

- 单摄像头输入与结构化视觉事件提取
- 基于 scene 的动作编排，而不是直接输出原始舵机角度
- 四关节 ESP32 台灯动作与灯光执行
- 本地 bridge、导演台 console、receiver 与统一启动契约
- mock 设备、dry-run、离线 rehearsal 与真机切换路径
- 预录主持词、本地音频 cue 与 `say` 回退路径
- 控制安全层，对 pose、绝对控制与相对 `nudge` 做 clamp / reject
- 可选的 embodied memory 回写能力

当前覆盖的核心场景包括：

- `wake_up`
- `curious_observe`
- `touch_affection`
- `cute_probe`
- `daydream`
- `standup_reminder`
- `track_target`
- `celebrate`
- `farewell`
- `sleep`

其中 `track_target` 当前仍以排练用 surrogate choreography 为主，尚未完全收敛为
最终视觉闭环。相关说明见：

- [docs/mira-light-pdf2-engineering-handoff.md](./docs/mira-light-pdf2-engineering-handoff.md)
- [docs/mira-light-pdf2-implementation-audit.md](./docs/mira-light-pdf2-implementation-audit.md)

## 动作与实现真值

如果你要判断“当前动作应该以什么为准”，建议按下面顺序阅读：

1. [docs/source-pdfs/Mira Light 展位交互方案2.pdf](./docs/source-pdfs/Mira%20Light%20展位交互方案2.pdf)
2. [docs/source-pdfs/ESP32 智能台灯.pdf](./docs/source-pdfs/ESP32%20智能台灯.pdf)
3. [scripts/scenes.py](./scripts/scenes.py)
4. [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
5. [docs/mira-light-scene-implementation-index.md](./docs/mira-light-scene-implementation-index.md)
6. [docs/mira-light-pdf2-implementation-audit.md](./docs/mira-light-pdf2-implementation-audit.md)

当前程序层统一按四个舵机关节实现：

- `servo1`：底座转向
- `servo2`：下臂抬升
- `servo3`：前段关节 / 中间关节抬升与前探
- `servo4`：灯头俯仰 / 微表情

## 仓库结构

```text
.
├── README.md
├── README.en.md
├── assets/                      音频 cue 与演示素材
├── config/                      profile、scene bundles 与事件 schema
├── deploy/                      repo manifest 与环境模板
├── docs/                        发布文档、runbook、handoff 与源 PDF
├── scripts/                     runtime、scene、receiver、console、诊断与启动脚本
├── tests/                       轻量验证脚本
├── tools/mira_light_bridge/     本地 bridge 与 OpenClaw 插件
└── web/                         导演台与场景展示页面
```

几个最重要的入口文件：

- [scripts/scenes.py](./scripts/scenes.py)
- [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
- [scripts/vision_runtime_bridge.py](./scripts/vision_runtime_bridge.py)
- [scripts/track_target_event_extractor.py](./scripts/track_target_event_extractor.py)
- [tools/mira_light_bridge/README.md](./tools/mira_light_bridge/README.md)
- [docs/release-startup-contract.md](./docs/release-startup-contract.md)

## 快速开始

### 环境要求

- Python `3.10+`
- 本地可用 `curl`

### 一键安装

```bash
cd Mira-Light-AI-That-Sees-You
bash scripts/setup_local_env.sh
```

或者：

```bash
npm run bootstrap
```

### 最快的本地演示路径

如果你想先走最稳的 mock 路径：

```bash
bash scripts/setup_local_env.sh
bash scripts/start_mock_console.sh
```

如果你想按 release 约定启动完整本地栈：

```bash
bash scripts/run_preflight_release.sh offline
bash scripts/start_local_stack.sh
```

常用命令：

```bash
npm run bootstrap
npm run preflight
npm start
npm run doctor
npm run smoke:http
npm run rehearsal:offline
npm run demo:live-follow
```

导演台默认入口：

```text
http://127.0.0.1:8765/
```

如果使用真机，先设置灯地址：

```bash
export MIRA_LIGHT_LAMP_BASE_URL=http://172.20.10.3
```

如果暂时不碰真机：

```bash
export MIRA_LIGHT_DRY_RUN=1
```

## 当前启动契约

发布版当前统一采用：

```text
browser
-> director console
-> local bridge
-> lamp runtime target
```

这意味着：

- console 不直接访问灯
- bridge 负责统一 API、runtime 状态和安全裁决
- `MIRA_LIGHT_LAMP_BASE_URL` 与 `MIRA_LIGHT_DRY_RUN` 属于 bridge runtime
- receiver 是独立链路，不与导演台启动契约混在一起

详细说明见：

- [docs/release-startup-contract.md](./docs/release-startup-contract.md)
- [docs/release-control-safety-and-openclaw-rollback.md](./docs/release-control-safety-and-openclaw-rollback.md)

## Scene Bundle 与交付模式

为了把“最小可演版本”和“完整展位版本”分开，当前发布版提供 scene bundle：

- `minimal`
- `booth_core`
- `booth_extended`
- `sensor_demos`

例如：

```bash
MIRA_LIGHT_SCENE_BUNDLE=booth_core bash scripts/start_local_stack.sh
```

说明文档：

- [docs/release-scene-bundles.md](./docs/release-scene-bundles.md)

## 推荐阅读顺序

如果你第一次接手这个仓库，建议按下面顺序读：

1. [docs/getting-started.md](./docs/getting-started.md)
2. [docs/release-preflight-runbook.md](./docs/release-preflight-runbook.md)
3. [docs/release-startup-contract.md](./docs/release-startup-contract.md)
4. [docs/release-scene-bundles.md](./docs/release-scene-bundles.md)
5. [docs/mira-light-pdf2-engineering-handoff.md](./docs/mira-light-pdf2-engineering-handoff.md)
6. [docs/mira-light-scene-implementation-index.md](./docs/mira-light-scene-implementation-index.md)
7. [docs/Guide/README.md](./docs/Guide/README.md)

完整文档入口：

- [docs/README.md](./docs/README.md)

## 当前边界

这个仓库当前应被理解为：

- 一个可运行的 Mira Light 发布版仓库
- 一个围绕展位演示、排练和交付组织的本地系统
- 一个强调 bridge、安全层、scene bundle 与 mock-to-live 切换的 release surface

它当前不应被误读为：

- 已经完成所有感知闭环的最终硬件产品
- 只靠单个脚本即可理解的简单 demo
- 仅仅是“台灯动作素材合集”

## 相关入口

- [README.en.md](./README.en.md)
- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [CHANGELOG.md](./CHANGELOG.md)
- [deploy/README.md](./deploy/README.md)
- [tools/mira_light_bridge/README.md](./tools/mira_light_bridge/README.md)
