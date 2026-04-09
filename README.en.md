# Mira Light: AI That Sees You

`#RedHackathon` `#小红书黑客松巅峰赛`

[中文](./README.md)

**Tagline**

An embodied AI companion that notices you before you ask.

**Highlights**

- `Embodied interaction`: AI moves from the chat window into real-space interaction
- `End-to-end system`: A runnable loop across vision, runtime, bridge, and console
- `Extensible memory path`: Selected scene and device outcomes can be written back into cloud memory

---

## Overview

Mira Light is an embodied AI interaction project built around a four-DOF lamp.
It explores a simple shift in interaction design: instead of waiting for an
explicit prompt, the system notices presence, interprets movement and context,
and responds through motion, direction, light, and rhythm.

This repository is not just a concept sketch or a visual mockup. It contains a
working chain across:

- camera input
- event extraction
- scene selection
- lamp runtime control
- bridge and safety boundaries
- optional memory writeback into cloud Mira

The project is best understood as a physical companion prototype rather than a
smart lamp feature demo.

## One-Line Project Intro

Mira Light turns AI from a passive interface into a physical companion that can
notice you, interpret interaction context, and respond in real space through
light and movement.

## What The Demo Feels Like

If you stand in front of the demo, the intended interaction is simple:

1. You approach. It wakes.
2. You pause. It turns toward you.
3. You move. It follows.
4. You engage. It shifts tone or motion.
5. You leave. It watches you go and settles back down.

The point is not motion in isolation. The point is that the motion appears to
be grounded in perception and timing rather than in random playback.

## Why This Project Matters

The project is trying to move AI interaction from:

```text
input -> answer
```

toward:

```text
notice -> interpret -> respond
```

That matters because:

- the system no longer has to wait for a command before it becomes relevant
- response is no longer limited to text or voice
- interaction becomes part of the surrounding physical space

Mira Light is not simply arguing that “AI can control hardware.”  
It is exploring what happens when AI starts to behave less like a utility panel
and more like a low-disturbance companion with presence.

## Current Capabilities

At the moment, the repository already supports a real working loop:

- receiving live JPEG camera input
- extracting structured visual events from a single camera
- deciding whether a target is present, where it is, and how it is moving
- mapping those events into high-level scenes rather than raw servo output
- executing motion and lighting responses through a four-DOF ESP32 lamp
- exposing a stable local bridge for control and integration
- supporting dry-run, mock-device, and offline rehearsal modes
- optionally writing selected scene and device outcomes back into cloud memory

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

The shortest local path is:

```bash
cd Mira-Light-AI-That-Sees-You
bash scripts/one_click_install.sh
```

Then run the release preflight:

```bash
bash scripts/run_preflight_release.sh offline
```

Then start the local stack:

```bash
bash scripts/start_local_stack.sh
```

After the stack is up, open the director console at:

```text
http://127.0.0.1:8765/
```

If you are working with real hardware, set the lamp base URL before starting:

```bash
export MIRA_LIGHT_LAMP_BASE_URL=http://172.20.10.3
```

## Key Files

The most useful entry points in this repository are:

- [docs/cam_receiver_new.py](./docs/cam_receiver_new.py)
  camera receiver for JPEG input and local preview
- [scripts/track_target_event_extractor.py](./scripts/track_target_event_extractor.py)
  converts vision input into structured tracking events
- [scripts/vision_runtime_bridge.py](./scripts/vision_runtime_bridge.py)
  maps vision events into runtime behavior and scene decisions
- [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
  unified runtime surface for scene execution
- [scripts/scenes.py](./scripts/scenes.py)
  scene choreography definitions
- [tools/mira_light_bridge/bridge_server.py](./tools/mira_light_bridge/bridge_server.py)
  stable local bridge layer
- [tools/mira_light_bridge/embodied_memory_client.py](./tools/mira_light_bridge/embodied_memory_client.py)
  optional embodied-memory writer into cloud `memory-context`

If you want the release-oriented local stack and operational runbooks, start
with:

- [docs/release-preflight-runbook.md](./docs/release-preflight-runbook.md)
- [docs/release-local-stack-runbook.md](./docs/release-local-stack-runbook.md)
- [docs/release-scene-bundles.md](./docs/release-scene-bundles.md)

## License

This repository is licensed under:

- `GNU Affero General Public License v3.0`
- SPDX: `AGPL-3.0-only`
