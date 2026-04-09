# Mira Light: AI That Sees You

`#RedHackathon` `#小红书黑客松巅峰赛`

[中文](./README.md)

**Tagline**

AI that sees you first.

**Proof Points**

- `Innovation`: AI moved from the chat window into embodied interaction in real space
- `Completion`: An end-to-end runnable loop across vision, runtime, bridge, and console
- `Technical Difficulty`: Single-camera event extraction, four-DOF hardware control, and embodied memory integration

---

Most AI waits for your prompt.

Mira Light sees you first.

This is not another chatbot wrapped in hardware.

It is an embodied AI lamp that wakes up when you arrive, studies you when you pause, follows you when you move, responds with emotion when you interact, and watches you go when you leave.

Mira Light turns perception into motion, light, and presence.

## One-Line Project Intro

Mira Light turns AI from a passive interface into a physical companion that notices you, follows you, responds to you, and expresses care in real space.

## Why It Hits Fast

- You understand it in seconds
- You remember it because it is physical
- You feel the product before anyone explains the tech

This is what "AI That Sees You" looks like when it leaves the screen.

## Demo Arc

1. You approach. It wakes.
2. You pause. It studies you.
3. You move. It follows.
4. You engage. It responds.
5. You leave. It watches you go.

Not automation.

Presence.

## Why It Works For Hackathon Judging

- Clear in seconds at an Expo booth
- Strong physical storytelling from perception to response
- Real hardware + runtime + bridge + tests + rehearsal stack
- Commercially extensible into companion devices and ambient intelligence
- Technically non-trivial across vision, scene orchestration, hardware control, and memory integration

## Core Loop

```text
camera input
-> vision event extraction
-> runtime scene selection
-> bridge / safety layer
-> ESP32 lamp motion + light response
-> optional embodied memory writeback
```

## Key Scenes

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

## Quick Start

```bash
cd Mira-Light-AI-That-Sees-You
bash scripts/one_click_install.sh
bash scripts/run_preflight_release.sh offline
bash scripts/start_local_stack.sh
```

Open the director console at:

```text
http://127.0.0.1:8765/
```

## Repository Highlights

- [docs/cam_receiver_new.py](./docs/cam_receiver_new.py)
- [scripts/track_target_event_extractor.py](./scripts/track_target_event_extractor.py)
- [scripts/vision_runtime_bridge.py](./scripts/vision_runtime_bridge.py)
- [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
- [scripts/scenes.py](./scripts/scenes.py)
- [tools/mira_light_bridge/bridge_server.py](./tools/mira_light_bridge/bridge_server.py)
- [tools/mira_light_bridge/embodied_memory_client.py](./tools/mira_light_bridge/embodied_memory_client.py)

## Why It Matters

Most AI products still live behind glass.

Mira Light argues for something bigger: AI that is ambient, embodied, emotionally legible, and physically present.

## License

- `GNU Affero General Public License v3.0`
- SPDX: `AGPL-3.0-only`
