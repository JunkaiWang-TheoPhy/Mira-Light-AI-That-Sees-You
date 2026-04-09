# Mira Light Integration Summary (2026-04-09)

## Purpose

This note collects the release-grade parts of the latest Mira Light update into
one place.

It answers three practical questions:

1. what is newly stable enough to keep in this repository
2. why those changes matter for demo and delivery use
3. which docs should be read first for rehearsal and release work

It is intentionally not a full development diary.

## What Is Worth Keeping

### 1. More stable scene speech

The repository now treats scene narration and a few key lines as a two-layer
playback path:

- first try bundled prerecorded speech assets under `assets/audio/speech/*.aiff`
- if no preset asset matches, fall back to local `say`

Relevant files:

- [scripts/mira_light_audio.py](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/scripts/mira_light_audio.py)
- [scripts/mira_light_runtime.py](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/scripts/mira_light_runtime.py)
- [scripts/scenes.py](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/scripts/scenes.py)

Why this matters:

- booth narration becomes more stable
- key lines no longer depend entirely on live network TTS
- repeated demos sound more consistent in pace and tone

### 2. Clearer device signal contract

The repository now makes a cleaner distinction between:

- raw TCP servo transport on `9527`
- `pixelSignals` for the 40-pixel light state
- `headCapacitive` for the touch sensor

Relevant docs:

- [docs/Guide/04-9527总线舵机TCP帧协议与仓库对齐说明.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/docs/Guide/04-9527总线舵机TCP帧协议与仓库对齐说明.md)
- [docs/Guide/09-Mira Light统一信号交付格式说明.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/docs/Guide/09-Mira%20Light统一信号交付格式说明.md)

Recommended interpretation:

- `/status` is the formal unified read surface
- `/led` is the dedicated LED state surface
- `/sensors` is the dedicated touch-sensor surface
- `/health` is only for health and snapshots

This reduces confusion during rehearsal and integration, especially around
whether everything is supposed to flow through raw TCP.

### 3. Cleaner mock-to-real-hardware path

The strongest release-facing gain is not visual polish. It is a clearer path
for:

- mock-first rehearsal
- offline validation
- bridge/runtime/device loop testing
- later switching back to real hardware

Relevant docs:

- [docs/mira-light-mock-rehearsal-guide.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/docs/mira-light-mock-rehearsal-guide.md)
- [docs/mira-light-offline-validation-stack.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/docs/mira-light-offline-validation-stack.md)

## What Was Not Promoted

The following were intentionally not treated as release-grade additions here:

- temporary director-console visual tweaks
- decorative UI effects and page-only animation experiments
- single-run integration hacks for specific rehearsal moments

Those are still useful, but they belong in active iteration rather than in the
stable explanation surface of this repository.

## Suggested Reading Order

1. [../README.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/README.md)
2. [getting-started.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/docs/getting-started.md)
3. [release-preflight-runbook.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/docs/release-preflight-runbook.md)
4. [release-startup-contract.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/docs/release-startup-contract.md)
5. [mira-light-mock-rehearsal-guide.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/docs/mira-light-mock-rehearsal-guide.md)
6. [Guide/09-Mira Light统一信号交付格式说明.md](/Users/huhulitong/Documents/GitHub/Mira-Light-AI-That-Sees-You/docs/Guide/09-Mira%20Light统一信号交付格式说明.md)

## Minimal Acceptance Checklist

To quickly judge whether the current tree is ready for release-style use:

1. run offline preflight
2. validate one full `mock lamp + bridge + runtime` loop
3. confirm key lines like `celebrate` and `farewell` can resolve to local speech
4. make sure mock and real-hardware status reading do not confuse `/status` and `/health`

## One-Line Conclusion

The high-value part of this sync is not “more stuff.”

It is that the repo is now better aligned around:

- steadier scene speech
- a clearer signal contract
- a more controllable path from mock rehearsal to live hardware
