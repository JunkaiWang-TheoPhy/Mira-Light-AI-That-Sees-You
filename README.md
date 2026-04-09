# Mira Light: AI That Sees You

`#RedHackathon` `#小红书黑客松巅峰赛`

[English](./README.en.md)

**Tagline**

AI that sees you first.

**Proof Points**

- `Innovation`：把 AI 从聊天框推进到真实空间中的具身交互
- `Completion`：从 vision 到 runtime 到 bridge 到 console 的完整可运行闭环
- `Technical Difficulty`：单摄像头事件提取、四自由度硬件控制与 embodied memory 集成

---

## 中文

大多数 AI，要等你开口。

Mira Light 会先看见你。

如果今天我们还只是把 AI 塞进一个聊天框里，它再聪明，也还是隔着一层屏幕。

我们想做的，是把 AI 从屏幕里请出来，让它真的出现在你面前。

所以 Mira Light 不是一个只会亮灯的智能硬件，也不是一个被动等待指令的助手。

它是一盏会醒来、会观察、会跟随、会表达情绪、也会目送你离开的具身 AI 灯。

它想回答的问题很简单：

> 如果 AI 不只会回答你，而是能先注意到你的存在，再在真实空间里回应你，它会是什么样子？

我们的答案是，一盏四自由度智能灯。

也是一个真正“看见你”的 AI companion。

## 一句话项目介绍

Mira Light 让 AI 从被动等待输入的聊天框，变成一个会看见你、跟随你、回应你，并在物理空间中表达关心的智能陪伴体。

## 如果你站在我们的展位前，10 秒钟会发生什么

- 你靠近，它会醒来
- 你停下，它会看你
- 你移动，它会追随你
- 你互动，它会表达情绪
- 你离开，它会送别并回到休息状态

那一刻你会明白，这不是“自动化台灯”。

这是一个会在空间里让你感到“自己被看见了”的 AI。

## 为什么它有冲击力

因为它把一个大家已经很熟悉的 AI 命题，变成了一个你能立刻感受到的物理体验：

- 别的 AI 在等你发 prompt，Mira Light 先看见你
- 别的 AI 用文字回答你，Mira Light 用动作和光线回应你
- 别的 AI 活在屏幕里，Mira Light 出现在你面前

所以 “AI That Sees You” 在这里不是口号。

它是一个观众站到展位前几秒钟，就能亲眼看到、亲身感到、并且记住的体验。

## 黑客松定位

按照 `小红书黑客松巅峰赛 2026` Playbook，这个项目按硬件方向进行展示与提交。

这份 README 也按评委速读的方式组织：

- 先讲体验和记忆点
- 再讲为什么它值得评奖
- 最后给出实现能力、架构与运行入口

## Demo 想讲的，不是功能，而是一段关系

Mira Light 在展位上的演示，不是“播放一套预设动作”，而是一条非常清晰的情绪曲线：

1. 你出现，它醒来。
2. 你停下，它好奇地观察你。
3. 你移动，它持续跟随你，证明它真的看见你。
4. 你互动，它表现出亲近、开心或温柔提醒。
5. 你离开，它目送你，再慢慢回到安静状态。

这一段关系里最重要的不是动作本身，而是它传达出的感觉：

AI 不再只是回答问题。

AI 开始拥有 presence。

它让“感知 -> 理解 -> 回应”第一次以一种非常直觉、非常可感、非常适合现场展示的方式发生在真实空间里。

## 为什么它适合现场评审

### 创新性

- 把 AI 从屏幕交互推进到具身交互
- 将感知、决策、动作、情绪表达串成同一个体验闭环
- 用真实空间中的物理反馈，把 “AI That Sees You” 做成直观体验

### 现场讲述效果

- 观众几秒内就能理解项目核心
- 物理动作与光线变化天然具备展示力
- 叙事路径清晰：看见 -> 理解 -> 回应 -> 送别

### 完成度

- 仓库已经包含运行时、bridge、console、receiver、测试、文档和脚本
- 既能跑真机，也能做 dry-run 与离线演练
- 已有清晰的 runbook、scene bundle 和 preflight 流程

### 商业潜力

- 桌面陪伴式 AI 硬件
- 家庭照护与儿童互动
- 零售展陈 / 门店迎宾 / 空间装置
- 办公环境提醒与主动式 ambient intelligence

### 技术难度

- 四自由度硬件控制与安全约束
- 单摄像头视觉事件抽取
- scene runtime 与 bridge API 设计
- OpenClaw 接入与云端 embodied memory 写入

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
