# AI Runtime And Cognition Additions

This document explains the AI-related material that has been imported into
`Mira-Light-AI-That-Sees-You` from the broader `Mira-Light` workspace.

The goal of this import is not to turn the repository into a generic AI lab.
The goal is to keep the release-oriented Mira Light stack intact while bringing
in the missing AI-facing files that matter for:

- local model experiments
- realtime voice interaction
- embodied memory capture
- OpenClaw and Lingzhu integration
- progress documentation for memory, voice, and AI system evolution

## Import Principles

The imported content follows three rules:

1. Keep the current repository layout stable.
   AI-related scripts stay under `scripts/`, docs stay under `docs/`, speech
   assets stay under `assets/`, and OpenClaw workspace files stay under
   `tools/`.
2. Keep file formats clean.
   Only source files and reusable assets were imported. Runtime caches,
   `__pycache__`, and transient state files were intentionally excluded.
3. Preserve relative execution expectations where practical.
   Scripts that expect sibling imports in `scripts/` were imported into the same
   directory rather than being moved into a new package boundary.

## What Was Added

### 1. Local-model And Prompt-Pack Scripts

These files support local Qwen / llama.cpp style experiments and prompt-pack
generation for Mira-style reasoning:

- `scripts/ask_mira_local_qwen.py`
- `scripts/build_mira_qwen_messages.py`
- `scripts/download_mlx_model.py`
- `scripts/download_llama_cpp_model.py`
- `scripts/setup_mlx_qwen_env.sh`
- `scripts/setup_llama_cpp_env.sh`
- `scripts/run_llama_cpp_server.sh`
- `scripts/smoke_test_mlx_model.py`
- `scripts/smoke_test_llama_cpp.py`

These are useful when you want to test a local Mira cognition path without
depending entirely on the release runtime alone.

### 2. Realtime Voice And Voice-to-Action Scripts

These files support local speech capture, intent classification, voice-to-scene
bridging, and realtime Mira voice experiments:

- `scripts/openclaw_voice_to_claw.py`
- `scripts/mira_realtime_claw_chat.py`
- `scripts/mira_realtime_voice_interaction.py`
- `scripts/mic_event_bridge.py`
- `scripts/mira_voice_intents.py`
- `scripts/measure_realtime_claw_chat_timing.py`
- `scripts/run_openclaw_voice_to_claw.sh`
- `scripts/run_mira_realtime_claw_chat.sh`
- `scripts/run_mira_realtime_voice_interaction.sh`
- `docs/mira-light-openclaw-voice-stt-guide.md`
- `docs/mira-light-realtime-voice-interaction-design.md`

These files are complementary to the current release stack. They extend the
repository into voice-driven demo and booth-interaction scenarios.

### 3. Embodied Memory And Capture Observation

These files add a more explicit embodied-memory and capture-to-memory path:

- `scripts/capture_memory_observer.py`
- `scripts/run_capture_memory_observer.sh`
- `docs/mira-light-to-mira-v3-layered-memory-integration-plan.md`
- `docs/feature/01-memory-and-knowledge-graph-progress.md`
- `docs/feature/02-local-vector-memory-progress.md`
- `docs/feature/06-context-proactivity-and-layered-memory-progress.md`

They matter when Mira Light is used not only as a motion system, but also as an
observation-producing edge surface for a broader Mira memory stack.

### 4. OpenClaw, Lingzhu, And Bridge-Adjacent Integration

These files extend the local integration story around OpenClaw and Lingzhu:

- `scripts/apply_claw_native_local.py`
- `scripts/mira_lingzhu_client.py`
- `scripts/sync_local_mira_light_service.py`
- `scripts/setup_local_mira_light_service_env.sh`
- `scripts/ensure_mira_light_bridge_tunnel.sh`
- `scripts/ensure_mira_lingzhu_tunnel.sh`
- `tools/mira_light_bridge/bridge_cli.py`
- `tools/openclaw_agents/mira_voice_spark_workspace/*`
- `docs/mira-light-openclaw-plugin-tool-reference.md`
- `docs/feature/03-claw-native-local-openclaw-progress.md`
- `docs/feature/23-openclaw-plugin-bridge-api-layering-and-openapi-draft.md`
- `docs/feature/28-cloud-openclaw-architecture-backup-and-mira-light-overlay-progress.md`

This layer is mainly about integration boundaries, transport shape, and how the
lamp-facing system participates in a larger Mira / OpenClaw runtime.

### 5. Audio Speech Assets

The import also adds bundled prerecorded speech assets under:

- `assets/audio/speech/`

These `.aiff` files cover host lines and a small set of key spoken responses.
They make booth playback more stable by preferring local speech assets before
falling back to `say` or TTS.

### 6. Progress Documentation

The following progress notes were imported because they describe important AI
surfaces that now exist alongside the release runtime:

- `docs/feature/12-local-audio-and-tts-progress.md`
- `docs/feature/16-speech-to-text-and-claw-voice-ingress-progress.md`
- `docs/feature/17-control-safety-and-openclaw-rollback-progress.md`
- `docs/feature/26-realtime-voice-dialogue-lingzhu-and-voice-mode-progress.md`

These documents are not operator runbooks. They are architecture and progress
context.

## How To Read The Imported AI Layer

If your goal is:

- local model bring-up:
  start with `scripts/ask_mira_local_qwen.py` and `scripts/build_mira_qwen_messages.py`
- realtime voice interaction:
  start with `scripts/mira_realtime_voice_interaction.py` and `docs/mira-light-realtime-voice-interaction-design.md`
- embodied memory:
  start with `scripts/capture_memory_observer.py` and `docs/mira-light-to-mira-v3-layered-memory-integration-plan.md`
- OpenClaw integration:
  start with `tools/mira_light_bridge/README.md`, `tools/mira_light_bridge/bridge_cli.py`, and `tools/openclaw_agents/mira_voice_spark_workspace/`

## What Was Intentionally Not Imported

The migration intentionally excluded:

- `__pycache__` directories
- `.pyc` files
- transient workspace state
- duplicate helper copies such as `README copy.md`

This keeps the imported AI layer source-oriented and repository-safe.

## Relation To The Main Release Runtime

The main release runtime still centers on:

- `scripts/scenes.py`
- `scripts/mira_light_runtime.py`
- `scripts/vision_runtime_bridge.py`
- `tools/mira_light_bridge/`
- `docs/release-*.md`

The imported AI layer does not replace that core. It expands the repository so
that local cognition, memory, voice, and OpenClaw-adjacent workflows can live
in the same release-facing tree.
