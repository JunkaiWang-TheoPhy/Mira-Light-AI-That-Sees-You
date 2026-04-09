#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [[ -z "${MIRA_LIGHT_PYTHON:-}" ]]; then
  for candidate in \
    "${HOME}/.local/bin/python3.11" \
    "$(command -v python3.11 2>/dev/null || true)" \
    "$(command -v python3.10 2>/dev/null || true)" \
    "$(command -v python3 2>/dev/null || true)"; do
    if [[ -n "${candidate}" && -x "${candidate}" ]]; then
      export PYTHON_BIN="${candidate}"
      break
    fi
  done
else
  export PYTHON_BIN="${MIRA_LIGHT_PYTHON}"
fi

echo "[setup-local-env] repo root: ${REPO_ROOT}"
echo "[setup-local-env] python: ${PYTHON_BIN:-not-found}"

exec bash "${REPO_ROOT}/scripts/one_click_install.sh"
