# Release Sync Notes (2026-04-09)

## Purpose

This note records the incremental sync that pulled delivery-grade runtime,
director-console, mock, audio, and rehearsal capabilities from
`Mira_Light_Released_Version` into `Mira-Light-AI-That-Sees-You`.

The goal of this sync was:

- keep the target repository structure intact
- keep the target repository identity files intact
- bring over the release-ready operational surface so this repo can be used
  as a fuller local demo, rehearsal, and delivery workspace

## What Was Synced

### Runtime and scene execution

- `scripts/mira_light_runtime.py`
- `scripts/scenes.py`
- `scripts/mira_light_audio.py`
- `scripts/console_server.py`

These updates bring in:

- delivery-oriented scene/runtime behavior
- dynamic farewell and touch/avoid routing
- richer audio/TTS playback support
- director-console endpoints for sensors, vision state, pose capture, and servo
  metadata editing

### Bridge and OpenClaw integration

- `tools/mira_light_bridge/bridge_server.py`
- `tools/mira_light_bridge/bridge_client.py`
- `tools/mira_light_bridge/openclaw_mira_light_plugin/index.mjs`
- `tools/mira_light_bridge/README.md`

These updates bring in:

- richer bridge endpoints
- better alignment with release mock payloads
- richer LED and sensor transport
- updated plugin-side schema and bridge usage

### Director console and local UI

- `web/index.html`
- `web/app.js`
- `web/styles.css`

These updates bring in:

- graphical mock controls
- `headCapacitive` sensor toggling
- 40-pixel `pixelSignals` visualization
- tracking and vision summaries
- release-aligned operator workflow

### Mock, rehearsal, replay, and live-follow tooling

- `scripts/mock_lamp_server.py`
- `scripts/mock_mira_light_device.py`
- `scripts/run_mock_lamp.sh`
- `scripts/run_mira_light_offline_rehearsal.sh`
- `scripts/run_mira_light_offline_rehearsal.py`
- `scripts/run_mira_light_live_follow_demo.sh`
- `scripts/run_mira_light_vision_stack.sh`
- `scripts/replay_camera_frames_to_receiver.py`
- `scripts/scene_trace_recorder.py`
- `scripts/vision_replay_bench.py`

These updates bring in:

- offline rehearsal workflows
- mock-device rehearsals
- live-follow demo entry points
- replay-based validation and scene trace capture

### Config, fixtures, and release docs

- `config/mira_light_vision_event.schema.json`
- `config/mira_light_mock_faults.example.json`
- `config/mira_light_offline_rehearsal.json`
- `deploy/repo.env.example`
- release-oriented docs and runbooks under `docs/`
- vision event fixtures under `fixtures/vision_events/`

These updates bring in:

- release-aligned vision schema
- mock/rehearsal example configuration
- expanded runbooks and delivery docs
- additional fixtures used by replay and bridge tests

## Intentionally Preserved Differences

The following files are intentionally not overwritten by the release sync:

- `README.md`
- `README.en.md`
- `LICENSE`

Reason:

- the target repository keeps its own presentation and bilingual README surface
- the target repository keeps its own license identity

## Validation Performed

The sync was checked with the following methods:

1. tree diff against `Mira_Light_Released_Version`
2. syntax checks for frontend/plugin files
3. Python compile checks on synced runtime and bridge files
4. core test execution using a Python 3.10+ virtualenv

After sync, the only expected tree differences versus
`Mira_Light_Released_Version` are:

- `README.md`
- `README.en.md`
- `LICENSE`

## Current Environment Status

This repository now has its own local `.venv` configured on this machine with
Python 3.11, and the release test script can run directly with that environment.

Notes:

- the system `python3` on this machine still resolves to Python 3.9.6
- `scripts/run_release_tests.sh` will automatically prefer `.venv/bin/python`
- local runtime and validation commands should therefore use the repository
  virtualenv by default

## Recommended Entry Points

If you want to use the freshly synced release-oriented flows from this repo,
start with:

- `scripts/run_mock_lamp.sh`
- `scripts/run_mira_light_offline_rehearsal.sh`
- `scripts/run_mira_light_live_follow_demo.sh`
- `docs/release-preflight-runbook.md`
- `docs/release-local-stack-runbook.md`
- `docs/mira-light-mock-rehearsal-guide.md`
- `docs/mira-light-live-follow-demo-runbook.md`
