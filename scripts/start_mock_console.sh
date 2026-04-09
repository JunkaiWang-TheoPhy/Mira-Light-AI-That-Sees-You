#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
LOG_ROOT="${MIRA_LIGHT_STACK_LOG_ROOT:-${REPO_ROOT}/.mira-light-runtime/mock-console}"

MOCK_HOST="${MIRA_LIGHT_MOCK_HOST:-127.0.0.1}"
MOCK_PORT="${MIRA_LIGHT_MOCK_PORT:-9791}"
BRIDGE_HOST="${MIRA_LIGHT_BRIDGE_HOST:-127.0.0.1}"
BRIDGE_PORT="${MIRA_LIGHT_BRIDGE_PORT:-9783}"
CONSOLE_HOST="${MIRA_LIGHT_CONSOLE_HOST:-127.0.0.1}"
CONSOLE_PORT="${MIRA_LIGHT_CONSOLE_PORT:-8765}"
BRIDGE_TOKEN="${MIRA_LIGHT_BRIDGE_TOKEN:-test-token}"
WAIT_SECONDS="${MIRA_LIGHT_STACK_WAIT_SECONDS:-15}"

usage() {
  cat <<'EOF'
Usage:
  bash scripts/start_mock_console.sh [options]

Options:
  --mock-port N         Override the mock lamp port
  --bridge-port N       Override the bridge port
  --console-port N      Override the director console port
  --bridge-token TOKEN  Override the bridge bearer token
  --wait-seconds N      Maximum seconds to wait for services
  --help                Show this message
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mock-port)
      MOCK_PORT="${2:?missing value for --mock-port}"
      shift 2
      ;;
    --bridge-port)
      BRIDGE_PORT="${2:?missing value for --bridge-port}"
      shift 2
      ;;
    --console-port)
      CONSOLE_PORT="${2:?missing value for --console-port}"
      shift 2
      ;;
    --bridge-token)
      BRIDGE_TOKEN="${2:?missing value for --bridge-token}"
      shift 2
      ;;
    --wait-seconds)
      WAIT_SECONDS="${2:?missing value for --wait-seconds}"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

mkdir -p "${LOG_ROOT}"
MOCK_LOG="${LOG_ROOT}/mock-lamp.log"
BRIDGE_LOG="${LOG_ROOT}/bridge.log"

export MIRA_LIGHT_BRIDGE_TOKEN="${BRIDGE_TOKEN}"
export MIRA_LIGHT_BRIDGE_HOST="${BRIDGE_HOST}"
export MIRA_LIGHT_BRIDGE_PORT="${BRIDGE_PORT}"
export MIRA_LIGHT_LAMP_BASE_URL="http://${MOCK_HOST}:${MOCK_PORT}"
export MIRA_LIGHT_BASE_URL="${MIRA_LIGHT_LAMP_BASE_URL}"
export MIRA_LIGHT_CONSOLE_HOST="${CONSOLE_HOST}"
export MIRA_LIGHT_CONSOLE_PORT="${CONSOLE_PORT}"
export MIRA_LIGHT_CONSOLE_BRIDGE_URL="http://${BRIDGE_HOST}:${BRIDGE_PORT}"
export MIRA_LIGHT_BRIDGE_URL="${MIRA_LIGHT_CONSOLE_BRIDGE_URL}"

MOCK_HEALTH_URL="http://${MOCK_HOST}:${MOCK_PORT}/health"
BRIDGE_HEALTH_URL="http://${BRIDGE_HOST}:${BRIDGE_PORT}/health"
CONSOLE_URL="http://${CONSOLE_HOST}:${CONSOLE_PORT}/"

BG_PIDS=()

cleanup() {
  local exit_code=$?
  trap - EXIT INT TERM
  for pid in "${BG_PIDS[@]:-}"; do
    if kill -0 "${pid}" >/dev/null 2>&1; then
      kill "${pid}" >/dev/null 2>&1 || true
    fi
  done
  for pid in "${BG_PIDS[@]:-}"; do
    wait "${pid}" >/dev/null 2>&1 || true
  done
  exit "${exit_code}"
}

trap cleanup EXIT INT TERM

wait_for_http() {
  local url="$1"
  local label="$2"
  local deadline=$((SECONDS + WAIT_SECONDS))

  until curl -fsS "${url}" >/dev/null 2>&1; do
    if (( SECONDS >= deadline )); then
      echo "[mock-console] ${label} did not become healthy in ${WAIT_SECONDS}s: ${url}" >&2
      return 1
    fi
    sleep 0.5
  done
  echo "[mock-console] ${label} healthy: ${url}"
}

echo "[mock-console] log root: ${LOG_ROOT}"
echo "[mock-console] mock lamp url: ${MIRA_LIGHT_LAMP_BASE_URL}"
echo "[mock-console] bridge url: ${MIRA_LIGHT_CONSOLE_BRIDGE_URL}"

echo "[mock-console] starting mock lamp"
bash "${REPO_ROOT}/scripts/run_mock_lamp.sh" --host "${MOCK_HOST}" --port "${MOCK_PORT}" >"${MOCK_LOG}" 2>&1 &
BG_PIDS+=("$!")
wait_for_http "${MOCK_HEALTH_URL}" "mock lamp"

echo "[mock-console] starting bridge"
bash "${REPO_ROOT}/tools/mira_light_bridge/start_bridge.sh" >"${BRIDGE_LOG}" 2>&1 &
BG_PIDS+=("$!")
wait_for_http "${BRIDGE_HEALTH_URL}" "bridge"

echo "[mock-console] mock log: ${MOCK_LOG}"
echo "[mock-console] bridge log: ${BRIDGE_LOG}"
echo "[mock-console] console url: ${CONSOLE_URL}"
echo "[mock-console] press Ctrl-C to stop mock lamp + bridge + console"

exec bash "${REPO_ROOT}/scripts/start_director_console.sh"
