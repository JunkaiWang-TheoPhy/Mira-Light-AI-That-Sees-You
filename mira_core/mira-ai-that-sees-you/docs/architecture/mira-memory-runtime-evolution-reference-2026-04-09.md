# Mira Memory Runtime Evolution Reference

## Purpose

This repository is no longer the sole place where Mira's newest runtime memory
work lands first, but it still contains important architecture and migration
context.

This note explains:

- what was recently implemented elsewhere
- how to interpret those changes from the perspective of this repository
- what this repository should now be used for

## What Changed In The Active Runtime

The currently active implementation work happened in two sibling repositories:

- `Javis-Hackathon/Mira_v3`
- `Mira-Light`

Together they now implement the first public-facing slice of:

- session memory
- prompt-pack reinjection
- embodied memory from lamp scene/device outcomes

That means the broader Mira architecture is shifting from:

```text
chat + tools
```

toward:

```text
context capture
-> layered memory
-> task shaping
-> proactive judgment
-> execution
```

## What This Repository Still Contributes

`Mira-AI-that-sees-you` remains valuable as:

- migration context
- release-side architectural reasoning
- deploy and boundary documentation
- copied historical explanation for why certain release-safe boundaries exist

It is especially useful when you need to explain:

- why `OpenClaw` should stay the execution layer
- why Mira should remain a companion-oriented upstream layer
- why memory and proactive logic should not be reduced to a single chat loop

## Mapping Old Concepts To New Implementation

### In this repository

You will mostly find:

- release architecture
- module/service/core boundaries
- migration bundles
- deploy contracts

### In `Javis-Hackathon/Mira_v3`

You will find the current live implementation for:

- `memory-context`
- `session_notes`
- `prompt-pack`
- Lingzhu adapter integration

### In `Mira-Light`

You will find the current live implementation for:

- embodied memory producer behavior
- scene outcome writes
- selected device outcome writes

## What Should Not Be Misread

This repository should not be read as \"obsolete\" just because some newer code
landed elsewhere first.

Its role has shifted slightly:

- less first-stop implementation surface
- more reference and release-architecture surface

That is still important because architecture drift often starts when the
reasoning layer disappears.

## Recommended Cross-Repository Reading

To understand the current state of Mira's memory evolution, use this reading
set:

1. This repository:
   [README.md](../../README.md)
2. This repository:
   [README.md](./README.md)
3. `Javis-Hackathon/Mira_v3`:
   [docs/architecture/mira-v3-layered-memory-and-proactivity-implementation-2026-04-09.md](/Users/Zhuanz/Documents/Github/Javis-Hackathon/Mira_v3/docs/architecture/mira-v3-layered-memory-and-proactivity-implementation-2026-04-09.md)
4. `Mira-Light`:
   [mira-context-proactivity-architecture.md](/Users/Zhuanz/Documents/Github/Mira-Light/docs/mira-context-proactivity-architecture.md)
5. `Mira-Light`:
   [mira-light-embodied-memory-integration-2026-04-09.md](/Users/Zhuanz/Documents/Github/Mira-Light/docs/mira-light-embodied-memory-integration-2026-04-09.md)

## Practical Summary

The best way to understand this repository after the recent changes is:

- use `Mira-AI-that-sees-you` for architectural continuity and release-safe reasoning
- use `Mira_v3` for the mainline implementation of layered memory
- use `Mira-Light` for embodied memory production

That three-repo split is not accidental. It now reflects the real separation of
responsibilities inside Mira's evolving system.
