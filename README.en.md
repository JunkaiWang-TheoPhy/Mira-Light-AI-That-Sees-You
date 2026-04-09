# Mira Light: AI That Sees You

`#RedHackathon` `#小红书黑客松巅峰赛`

[中文](./README.md)

**Some forms of care do not need to be spoken.**

Mira Light is an embodied AI interaction project built around a four-DOF smart
lamp. It tries to move "seeing you, understanding you, and responding to you"
out of the chat window and into real space through posture, direction, light,
and rhythm.

This repository is not a single-feature demo and not just a loose collection of
scripts. It is the release-oriented mainline for demo use, rehearsal, and
handoff, covering the full path from vision input to scene choreography, from
the local bridge to the director console, and from mock rehearsal to live
hardware validation.

## Project Positioning

Mira Light is built for expo demos, director-led presentations, and technical
handoff. Its core goal is not simply to prove that "a lamp can move," but to
prove that:

```text
AI can first notice your presence
-> interpret your position and interaction context
-> then respond through motion and light
```

The repository is currently organized around this loop:

```text
camera input
-> vision event extraction
-> scene selection
-> bridge / safety layer
-> ESP32 lamp motion + light response
-> optional embodied memory writeback
```

## Demo Experience

At the booth, Mira Light is meant to make one thing clear within a few seconds:
this is not a lamp randomly replaying motions, but a physical system that sees
you first and then responds.

Typical interactions include:

- you approach, it wakes up
- you pause, it observes you
- you move, it follows you
- you engage, it shows affection, excitement, or reminder behavior
- you leave, it watches you go and settles back into rest

Representative scene references:

- [docs/mira-light-booth-scene-table.md](./docs/mira-light-booth-scene-table.md)
- [docs/mira-light-scene-implementation-index.md](./docs/mira-light-scene-implementation-index.md)
- [docs/release-scene-bundles.md](./docs/release-scene-bundles.md)

## Current Capability Scope

The repository currently provides these release-grade capabilities:

- single-camera input and structured vision event extraction
- scene-based motion choreography instead of direct raw servo output
- four-joint ESP32 lamp motion and light execution
- a local bridge, director console, receiver, and a unified startup contract
- mock device, dry-run, offline rehearsal, and mock-to-live handoff paths
- prerecorded host lines, local audio cues, and `say` fallback behavior
- a shared control safety layer with clamp / reject handling for pose, absolute control, and relative `nudge`
- optional embodied memory writeback

The main scenes currently covered are:

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

At the moment, `track_target` still functions mainly as a rehearsal-oriented
surrogate choreography and has not yet fully converged into the final live
vision loop. See:

- [docs/mira-light-pdf2-engineering-handoff.md](./docs/mira-light-pdf2-engineering-handoff.md)
- [docs/mira-light-pdf2-implementation-audit.md](./docs/mira-light-pdf2-implementation-audit.md)

## Motion And Implementation Source Of Truth

If you need to decide what the current motion truth should be, read in this
order:

1. [docs/source-pdfs/Mira Light 展位交互方案2.pdf](./docs/source-pdfs/Mira%20Light%20展位交互方案2.pdf)
2. [docs/source-pdfs/ESP32 智能台灯.pdf](./docs/source-pdfs/ESP32%20智能台灯.pdf)
3. [scripts/scenes.py](./scripts/scenes.py)
4. [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
5. [docs/mira-light-scene-implementation-index.md](./docs/mira-light-scene-implementation-index.md)
6. [docs/mira-light-pdf2-implementation-audit.md](./docs/mira-light-pdf2-implementation-audit.md)

At the program layer, the hardware model is currently unified around four servo
joints:

- `servo1`: base yaw
- `servo2`: lower arm lift
- `servo3`: forward / middle joint extension and lift
- `servo4`: head pitch / micro-expression

## Repository Layout

```text
.
├── README.md
├── README.en.md
├── assets/                      audio cues and demo assets
├── config/                      profiles, scene bundles, and event schemas
├── deploy/                      repo manifest and environment templates
├── docs/                        release docs, runbooks, handoff notes, and source PDFs
├── scripts/                     runtime, scenes, receiver, console, diagnostics, and startup scripts
├── tests/                       lightweight verification scripts
├── tools/mira_light_bridge/     local bridge and OpenClaw plugin
└── web/                         director console and scene showcase pages
```

The most important entry points are:

- [scripts/scenes.py](./scripts/scenes.py)
- [scripts/mira_light_runtime.py](./scripts/mira_light_runtime.py)
- [scripts/vision_runtime_bridge.py](./scripts/vision_runtime_bridge.py)
- [scripts/track_target_event_extractor.py](./scripts/track_target_event_extractor.py)
- [tools/mira_light_bridge/README.md](./tools/mira_light_bridge/README.md)
- [docs/release-startup-contract.md](./docs/release-startup-contract.md)

## Quick Start

### Requirements

- Python `3.10+`
- local `curl`

### One-Command Install

```bash
cd Mira-Light-AI-That-Sees-You
bash scripts/setup_local_env.sh
```

Or:

```bash
npm run bootstrap
```

### Fastest Local Demo Path

If you want the safest mock-first path:

```bash
bash scripts/setup_local_env.sh
bash scripts/start_mock_console.sh
```

If you want to start the full local stack using the release contract:

```bash
bash scripts/run_preflight_release.sh offline
bash scripts/start_local_stack.sh
```

Common commands:

```bash
npm run bootstrap
npm run preflight
npm start
npm run doctor
npm run smoke:http
npm run rehearsal:offline
npm run demo:live-follow
```

Default director console entry:

```text
http://127.0.0.1:8765/
```

If you are using live hardware, set the lamp base URL first:

```bash
export MIRA_LIGHT_LAMP_BASE_URL=http://172.20.10.3
```

If you want to avoid live hardware for now:

```bash
export MIRA_LIGHT_DRY_RUN=1
```

## Current Startup Contract

The current release uses this unified topology:

```text
browser
-> director console
-> local bridge
-> lamp runtime target
```

This means:

- the console does not talk to the lamp directly
- the bridge owns the public API, runtime state, and safety decisions
- `MIRA_LIGHT_LAMP_BASE_URL` and `MIRA_LIGHT_DRY_RUN` belong to the bridge runtime
- the receiver remains a separate path and is not part of the console startup contract

Details:

- [docs/release-startup-contract.md](./docs/release-startup-contract.md)
- [docs/release-control-safety-and-openclaw-rollback.md](./docs/release-control-safety-and-openclaw-rollback.md)

## Scene Bundles And Delivery Modes

To separate the smallest showable path from the full booth path, the current
release provides scene bundles:

- `minimal`
- `booth_core`
- `booth_extended`
- `sensor_demos`

Example:

```bash
MIRA_LIGHT_SCENE_BUNDLE=booth_core bash scripts/start_local_stack.sh
```

Reference:

- [docs/release-scene-bundles.md](./docs/release-scene-bundles.md)

## Recommended Reading Order

If you are taking over this repository for the first time, read in this order:

1. [docs/getting-started.md](./docs/getting-started.md)
2. [docs/release-preflight-runbook.md](./docs/release-preflight-runbook.md)
3. [docs/release-startup-contract.md](./docs/release-startup-contract.md)
4. [docs/release-scene-bundles.md](./docs/release-scene-bundles.md)
5. [docs/mira-light-pdf2-engineering-handoff.md](./docs/mira-light-pdf2-engineering-handoff.md)
6. [docs/mira-light-scene-implementation-index.md](./docs/mira-light-scene-implementation-index.md)
7. [docs/Guide/README.md](./docs/Guide/README.md)

Full documentation entry:

- [docs/README.md](./docs/README.md)

## Current Boundaries

This repository should currently be understood as:

- a runnable Mira Light release repository
- a local system organized around booth demo, rehearsal, and delivery
- a release surface centered on the bridge, safety layer, scene bundles, and mock-to-live switching

It should not be misread as:

- a final hardware product with every sensing loop fully completed
- a simple demo that can be understood from one script alone
- just a collection of lamp motion assets

## Related Entry Points

- [README.md](./README.md)
- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [CHANGELOG.md](./CHANGELOG.md)
- [deploy/README.md](./deploy/README.md)
- [tools/mira_light_bridge/README.md](./tools/mira_light_bridge/README.md)
