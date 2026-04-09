# Changelog

## 2026-04-09

- created `Mira_Light_Released_Version/` as a self-contained release tree
- copied core runtime, bridge, web, config, tests, and scene docs into the release folder
- added one-click install entrypoint: `bash scripts/one_click_install.sh`
- added machine-readable deploy manifest under `deploy/repo-manifest.json`
- added release docs index and getting-started docs
- added release-side doctor and OpenClaw plugin install wrappers
- stabilized scene host-line playback by preferring bundled prerecorded speech assets before falling back to local `say`
- switched key scene lines (`celebrate`, `farewell`, comfort demos) to the more stable local-speech path
- documented the unified signal contract across raw TCP servo frames, `pixelSignals`, and `headCapacitive`
- tightened mock/offline docs so `/status`, `/led`, `/sensors`, and `/health` now have clearer responsibilities
- added an integration summary that explains which recent changes are intentionally treated as release-grade
