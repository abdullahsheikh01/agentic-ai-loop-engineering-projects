#!/usr/bin/env bash
set -uo pipefail

POLL_INTERVAL=${1:-70}
PORT=${PORT:-4096}
SERVER_URL="http://127.0.0.1:${PORT}"
PROGRESS_FILE="progress.md"
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$PROJECT_DIR"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

stop_server() {
  log "Stopping opencode server (PID: ${SERVER_PID:-unknown})..."
  [ -n "${SERVER_PID:-}" ] && kill "$SERVER_PID" 2>/dev/null
}

trap 'stop_server; exit 0' INT TERM EXIT

log "Starting opencode server on port ${PORT}..."
opencode serve --port "$PORT" --hostname 127.0.0.1 > /tmp/opencode-server.log 2>&1 &
SERVER_PID=$!

SERVER_READY=0
for i in $(seq 1 30); do
  if grep -q "server listening" /tmp/opencode-server.log 2>/dev/null; then
    SERVER_READY=1
    break
  fi
  sleep 2
done

if [ "$SERVER_READY" -eq 0 ]; then
  log "Server failed to start; aborting."
  exit 1
fi

log "Server is up (PID: ${SERVER_PID}). Waiting for session handling to be ready..."
sleep 5

log "Running opencode on the server via loop-watcher skill..."
opencode run --attach "$SERVER_URL" --dir "$PROJECT_DIR" \
  "Use your loop-watcher skill (script-watcher-loop) to execute the script now."

log "Script launched. Checking status via opencode every ${POLL_INTERVAL}s..."

while true; do
  sleep "$POLL_INTERVAL"
  log "Asking opencode to check script status..."

  OUTPUT="$(opencode run --attach "$SERVER_URL" --dir "$PROJECT_DIR" \
    "Use your loop-watcher skill (script-watcher-loop) to check the current status of the script. Report whether it is RUNNING, COMPLETED, FAILED, or NOT_FOUND." 2>&1)"

  log "$OUTPUT"

  case "$OUTPUT" in
    *COMPLETED*)
      log "Script completed. Exiting loop."
      break
      ;;
    *FAILED*)
      log "Script failed. Exiting loop."
      break
      ;;
    *NOT_FOUND*)
      log "Script not found. Exiting loop."
      break
      ;;
    *)
      continue
      ;;
  esac
done

stop_server
log "Done. Final progress:"
cat "$PROGRESS_FILE"