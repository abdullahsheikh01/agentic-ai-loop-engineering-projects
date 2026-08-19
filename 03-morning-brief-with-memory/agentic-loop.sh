#!/usr/bin/env bash
# =============================================================================
# agentic-loop driver — SCHEDULER ONLY. No loop logic lives here.
# Every check, condition test, and decision is made by opencode, which is
# prompted once per iteration.
#
# Usage:
#   bash agentic-loop.sh [path/to/loop-prompt.md]
#
# Env overrides:
#   PORT       port for opencode serve            (default: 4096)
#   INTERVAL   seconds between iterations         (default: 300)
#   LOG_FILE   where loop activity is appended    (default: loop.log)
# =============================================================================
set -uo pipefail

export PATH="$HOME/.opencode/bin:$PATH"

LOOP_PROMPT="${1:-loop-prompt.md}"
PORT="${PORT:-4096}"
INTERVAL="${INTERVAL:-300}"
LOG_FILE="${LOG_FILE:-loop.log}"
PROJECT_DIR="$(pwd)"
SERVER_URL="http://127.0.0.1:${PORT}"
SERVER_LOG="/tmp/agentic-loop-serve.log"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

[ -f "$LOOP_PROMPT" ] || { log "ERROR: loop prompt file not found: $LOOP_PROMPT"; exit 1; }

# --- 1. Start opencode on its own port ---------------------------------------
log "Starting opencode server on port ${PORT}..."
: > "$SERVER_LOG"
opencode serve --port "$PORT" --hostname 127.0.0.1 >> "$SERVER_LOG" 2>&1 &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null' EXIT INT TERM

for _ in $(seq 1 30); do
  if grep -q "server listening" "$SERVER_LOG" 2>/dev/null; then
    log "Server is up (PID ${SERVER_PID})."
    break
  fi
  if ! kill -0 "$SERVER_PID" 2>/dev/null; then
    log "ERROR: opencode server died; see ${SERVER_LOG}."
    exit 1
  fi
  sleep 2
done

# --- 2. Loop: opencode checks, acts, and decides each iteration ---------------
ITERATION=0
while true; do
  ITERATION=$((ITERATION + 1))
  log "Iteration ${ITERATION} — prompting opencode..."

  OUTPUT="$(opencode run --attach "$SERVER_URL" --dir "$PROJECT_DIR" --format json \
    "You are driving an agentic loop. Read the loop contract at ${LOOP_PROMPT}. Perform ONE loop turn: run the check, act toward the goal, and evaluate the stop condition. Finish your reply with a final line that contains EXACTLY ONE of the tokens LOOP_CONTINUE, LOOP_DONE, or LOOP_FAIL and nothing else on that line." 2>&1)"
  log "$OUTPUT"

  case "$OUTPUT" in
    *LOOP_DONE*)
      log "Loop finished (LOOP_DONE)."
      break
      ;;
    *LOOP_FAIL*)
      log "Loop failed (LOOP_FAIL)."
      break
      ;;
    *LOOP_CONTINUE*)
      log "Continuing; next iteration in ${INTERVAL}s."
      ;;
    *)
      log "No decision token found; treating as CONTINUE."
      ;;
  esac

  sleep "$INTERVAL"
done

log "Done. Full activity in ${LOG_FILE}."