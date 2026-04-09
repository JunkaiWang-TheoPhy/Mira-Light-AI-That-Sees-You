# Mira Light: AI That Sees You

`#RedHackathon` `#小红书黑客松巅峰赛`

[English](./README.en.md)

**Tagline**

An embodied AI companion that notices you before you ask.

**Highlights**

- `Embodied interaction`：让感知、判断与回应发生在真实空间里，而不只是在聊天框中
- `End-to-end system`：从 vision 到 runtime 到 bridge 到 console 的完整可运行链路
- `Extensible memory path`：支持把部分 scene/device outcome 写回云端 `memory-context`

---

## 中文

Mira Light 是一个具身化 AI 交互项目。它尝试把“看见你、理解你、回应你”从屏幕里的聊天框，带到真实空间中的一盏四自由度智能灯上。

它不是一个只会播放预设动作的台灯，也不是一个被动等待指令的语音助手。  
它的目标是让 AI 在空间中具备更明确的存在感：先注意到你的出现，再根据你的位置、移动和互动节奏做出合适的动作与灯光回应。

如果用一句更直接的话来概括：

> Mira Light 想做的，是一个会先看见你、再以刚刚好的方式回应你的桌面 AI 陪伴体。

## 一句话项目介绍

Mira Light 让 AI 从被动等待输入的聊天框，变成一个能够主动感知、理解互动语境，并通过灯光、方向、姿态与节奏表达回应的桌面陪伴体。

## 如果你站在我们的展位前，10 秒钟会发生什么

- 你靠近，它会醒来
- 你停下，它会看你
- 你移动，它会追随你
- 你互动，它会表达情绪
- 你离开，它会送别并回到休息状态

这时你感受到的重点，不是“它会动”，而是“它真的注意到了你”。

## 这个项目真正新在哪里

Mira Light 的价值，不在于“让一盏灯动起来”，而在于把 AI 的交互链路从：

```text
输入 -> 回答
```

推进成：

```text
看见你 -> 判断你当前的状态 -> 用动作和灯光回应你
```

这带来三件很不一样的事情：

- AI 不再只是等待你发出命令，而是先感知到你的出现
- AI 的回应不再局限于文字或语音，而是进入姿态、方向、节奏和光线
- 交互不再只发生在屏幕里，而是进入你所处的物理环境

所以这个项目真正成立的地方，不是单个功能点，而是它把“感知 -> 理解 -> 回应”做成了一条可以被观众当场感受到的具身体验链。

Mira Light 想证明的也不是“AI 可以控制硬件”，而是：

> 当 AI 先看见你，再以刚刚好的方式回应你，它就开始从工具变成陪伴体。

## 项目定位

这是一个完整、独立、可直接演示的 AI 硬件交互项目，面向 `小红书黑客松巅峰赛 2026` 的现场 Expo 与 Demo Day 场景。

它不是单点功能 demo，而是一条已经跑通的端到端链路：

```text
摄像头输入
-> 视觉事件提取
-> 行为 / 场景决策
-> 台灯动作与灯光表达
-> 可选的上下文与记忆回写
```

这份 README 也按“评委和协作者快速理解”的方式组织：

- 先说明项目是什么
- 再说明它为什么成立
- 然后说明它已经实现到什么程度
- 最后给出运行入口和代码结构

## Demo 想表达的，不是功能列表，而是一段关系

Mira Light 在展位上的演示，不是简单地播放一套预设动作，而是一条清晰的交互曲线：

1. 你出现，它醒来。
2. 你停下，它观察你。
3. 你移动，它持续跟随你。
4. 你互动，它表现出亲近、开心或提醒。
5. 你离开，它目送你，再慢慢回到安静状态。

这里最重要的不是动作本身，而是动作背后的判断感。  
观众需要在几秒钟内明白：它不是随机地动，而是在“看见你之后”才这样动。

## 为什么这个项目适合被快速理解

这个项目有一个很直接的优点：它的核心价值不需要长时间解释。

观众站到设备前，几秒钟内就能看到一条完整链路：

- 设备先感知到人的出现
- 行为不是随机播放，而是和人的位置、移动、互动相关
- 回应不是文字，而是方向、动作和光线

这让项目的第一层理解门槛很低。  
而在这层直观体验之下，又能进一步看到它并不是单一效果展示，而是一套完整系统：

- 有视觉输入
- 有事件抽取
- 有 scene 决策
- 有 bridge 和 runtime
- 有本地控制台
- 有测试、preflight 和可交付目录

所以它既适合现场展示，也经得起技术追问。

## 为什么它值得继续做

这个项目的延展性主要体现在三个方面。

### 交互方向

它把 AI 的交互重心从“等待输入”推进到“先注意到你，再回应你”。  
这意味着它天然适合继续探索桌面陪伴、环境交互和低打扰式主动提醒。

### 系统方向

它不是一个孤立硬件，而是一套可以继续扩展的链路：

- vision
- runtime
- bridge
- console
- memory writeback

这意味着后续既可以继续打磨现场体验，也可以继续往云端 companion、memory、proactive layer 方向扩展。

### 应用方向

它现在最适合的不是“替代某个既有产品”，而是作为一种新的交互原型：

- 桌面陪伴
- 儿童互动
- 老人关怀
- 空间装置
- 展陈与迎宾
- 环境型提醒系统

也就是说，它的价值不只在这次 demo，而在于它已经把一种具身 AI 的最小可运行形态做出来了。

## 当前已经实现的能力

为了让这个体验不是停留在概念层，我们已经把下面这条链路做成可运行系统：

- 通过 HTTP 接收 JPEG 图像流并本地预览
- 从单摄像头输入中提取结构化视觉事件
- 判断目标是否出现、位于左中右、处于靠近/远离/稳定状态
- 将视觉结果映射到 scene，而不是直接输出原始舵机角度
- 通过四自由度 ESP32 台灯执行动作与灯光反馈
- 提供本地 bridge、导演台 console、receiver、preflight、diagnostics 和测试
- 支持真实灯具、dry-run、mock 演练和本地完整栈启动
- 支持把部分场景/设备结果写入云端 `memory-context`

## 代表性场景

仓库当前覆盖的核心 scene 包括：

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

更完整的场景说明可以看：

- [docs/mira-light-booth-scene-table.md](./docs/mira-light-booth-scene-table.md)
- [docs/release-scene-bundles.md](./docs/release-scene-bundles.md)
- [scripts/scenes.py](./scripts/scenes.py)

## 系统架构

```text
camera input
-> vision event extraction
-> runtime scene selection
-> bridge / safety layer
-> ESP32 lamp motion + light response
-> optional embodied memory writeback
```

### 关键模块

- [docs/cam_receiver_new.py](./docs/cam_receiver_new.py)
  图像接收端，负责接收 JPEG 帧并本地预览

- [scripts/track_target_event_extractor.py](./scripts/track_target_event_extractor.py)
  把图像流转成结构化视觉事件

- [config/mira_light_vision_event.schema.json](./config/mira_light_vision_event.schema.json)
  视觉层和 runtime 之间的稳定事件契约

- [scripts/vision_runtime_bridge.py](./scripts/vision_runtime_bridge.py)
  把视觉事件映射成 scene 或 live tracking

- [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
  统一的运行时控制面

- [scripts/scenes.py](./scripts/scenes.py)
  scene、pose、primitive、情绪与动作编排定义

- [tools/mira_light_bridge/bridge_server.py](./tools/mira_light_bridge/bridge_server.py)
  本地 bridge 服务

- [tools/mira_light_bridge/embodied_memory_client.py](./tools/mira_light_bridge/embodied_memory_client.py)
  将选定事件写入云端 `memory-context`

## 快速开始

### 1. 一键安装

```bash
cd Mira-Light-AI-That-Sees-You
bash scripts/one_click_install.sh
```

或者：

```bash
npm run bootstrap
```

### 2. 先跑离线 preflight

```bash
bash scripts/run_preflight_release.sh offline
```

### 3. 如有真机，配置灯地址

```bash
export MIRA_LIGHT_LAMP_BASE_URL=http://172.20.10.3
```

### 4. 启动完整本地栈

```bash
bash scripts/start_local_stack.sh
```

### 5. 打开导演台

```text
http://127.0.0.1:8765/
```

### 6. 如果只想先做不碰真机的演练

```bash
export MIRA_LIGHT_DRY_RUN=1
bash scripts/start_local_stack.sh
```

## 与云端 Mira 的关系

这个仓库不只是设备控制栈，它也是第一版 `embodied memory producer`。

它可以把一部分高价值结果写入云端 `memory-context`，例如：

- scene success / failure
- selected device status
- selected warning / error events

推荐的 shared embodied writer id：

```text
mira-light-bridge
```

相关文件：

- [tools/mira_light_bridge/embodied_memory_client.py](./tools/mira_light_bridge/embodied_memory_client.py)
- [tools/mira_light_bridge/bridge_server.py](./tools/mira_light_bridge/bridge_server.py)
- [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
- [tests/test_embodied_memory.py](./tests/test_embodied_memory.py)

相关说明文档：

- [docs/mira-context-proactivity-architecture.md](./docs/mira-context-proactivity-architecture.md)
- [docs/mira-light-embodied-memory-integration-2026-04-09.md](./docs/mira-light-embodied-memory-integration-2026-04-09.md)

## 仓库结构

- `assets/`
  音频和演示静态素材

- `config/`
  profile、vision schema、scene bundle 配置

- `deploy/`
  部署和环境说明

- `docs/`
  架构、场景、runbook、handoff、integration 文档

- `fixtures/`
  视觉事件与测试 fixtures

- `scripts/`
  runtime、receiver、preflight、诊断、安装和演示脚本

- `tests/`
  Python 测试

- `tools/mira_light_bridge/`
  bridge 与 OpenClaw 插件

- `web/`
  导演台与场景演示前端

## 提交材料映射

按 Playbook，这个仓库可以直接作为 GitHub 提交入口。其余材料可以围绕本仓库补齐：

- GitHub 仓库：当前仓库
- 2 分钟以内 Demo 视频：`TBD`
- 小红书项目介绍笔记：`TBD`
- 项目 Slide：`TBD`
- 一句话项目介绍：已包含
- 一句话团队介绍：`TBD`

建议团队一句话介绍：

> 我们在做具身化 AI，让感知、情绪和动作在真实空间里形成闭环。

## 原创与 AI 使用说明

Mira Light 是一个原创项目。我们使用 AI 辅助工具提高调研、编码、文档整理和迭代效率，但项目的问题定义、产品方向、场景设计、系统架构、交互表达和最终实现选择都由团队主导完成。

它不是纯粹依赖 AI 自动生成的代码堆砌，而是一个围绕具身 AI 体验独立构建的完整作品。

## License

本仓库使用：

- `GNU Affero General Public License v3.0`
- SPDX: `AGPL-3.0-only`
