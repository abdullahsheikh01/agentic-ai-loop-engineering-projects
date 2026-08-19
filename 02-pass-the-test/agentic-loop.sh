#!/usr/bin/env bash
# =============================================================================
# agentic-loop driver — SCHEDULER ONLY. No loop logic lives here.
# Every check, condition test, and decision is made by opencode, which is
# prompted once per iteration.
#
# NOTE: opencode's `run --attach` is broken in 1.18.18 (sessions start but the
# model never executes), so this driver runs `opencode run` directly, which
# spins up its own in-process server and works reliably. The loop brain is
# still opencode: the shell script only schedules turns and reads the
# decision token.
#
# Usage:
#   bash agentic-loop.sh [path/to/loop-prompt.md]
#
# Env overrides:
#   INTERVAL             seconds between iterations  (default: 120)
#   ITERATION_TIMEOUT    max seconds per iteration   (default: 900)
#   LOG_FILE             where loop activity is appended (default: loop.log)
# =============================================================================
set -uo pipefail

LOOP_PROMPT="${1:-loop-prompt.md}"
INTERVAL="${INTERVAL:-120}"
ITERATION_TIMEOUT="${ITERATION_TIMEOUT:-900}"
LOG_FILE="${LOG_FILE:-loop.log}"
PROJECT_DIR="$(pwd)"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

[ -f "$LOOP_PROMPT" ] || { log "ERROR: loop prompt file not found: $LOOP_PROMPT"; exit 1; }

# Ctrl+C / kill must stop the loop cleanly.
stop() {
  log "Signal received — stopping the loop."
  exit 130
}
trap stop INT TERM

# --- 1. Loop: opencode checks, acts, and decides each iteration ---------------
ITERATION=0
while true; do
  ITERATION=$((ITERATION + 1))
  log "Iteration ${ITERATION} — prompting opencode..."

  OUTPUT="$(timeout "$ITERATION_TIMEOUT" opencode run --dir "$PROJECT_DIR" --auto \
    "You are driving an agentic loop. Read the loop contract at ${LOOP_PROMPT}. Perform ONE loop turn: run the check, act toward the goal, and evaluate the stop condition. End your reply with exactly one decision token: LOOP_CONTINUE, LOOP_DONE, or LOOP_FAIL." 2>&1)"
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