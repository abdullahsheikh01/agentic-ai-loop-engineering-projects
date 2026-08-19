---
name: script-watcher-loop
description: Use when the user asks to execute, watch, run, loop, or check the status of a script in this project (e.g. script.sh, run.sh, watch.sh, watcher, or "run the script"). Executes the script via bash and tracks its status by writing to progress.md (creating the file if missing). Use ONLY when a script must be executed and/or its run status tracked.
---

# Script Watcher Loop

Watch and execute a project script, reporting its status through `progress.md`.

## HARD RULE: NEVER READ THE SCRIPT

- **Never** read, open, view, or print the contents of the target script file — not even to debug, fix, or understand it.
- **Never** use `read`, `cat`, `head`, `tail`, `less`, `grep`, or `sed` on the script file.
- **Never** ask the model to summarize, modify, or explain the script's code.
- Locate the script **by name only** (e.g. via `ls` / `glob`). That is all.
- Execution is the **only** task. If you cannot execute without reading it, still do not read it — report the problem in `progress.md` instead.

## Where the Script Comes From

- Use the script the user named or pointed to.
- If the user explicitly says "external script" (or gives an explicit path/URL outside the current directory), that external script may be executed with the user's permission. The "current directory only" rule is waived only when the user explicitly requests an external script.
- Otherwise, if none is named, execute the script **in the current working directory only**. Do **not** search globally or outside the current directory.
- Find the script by common names (`script.sh`, `run.sh`, `watch.sh`, `main.sh`) via `ls`/`glob` **in the current directory only**.
- If no script is found in the current directory, write a `NOT_FOUND` status to `progress.md` and tell the user.
- **Always ask the user for permission before executing** the script (e.g. via the `question` tool). Do not run without explicit approval.

## Status File: progress.md

All status updates go into `progress.md` in the project root. Create it if it does not exist. Keep the status current on every change.

```markdown
# Progress

## Status: RUNNING

- Script: <script name>
- Started: <timestamp>
- PID: <pid>
- Last check: <timestamp>
```

Allowed statuses: `RUNNING`, `COMPLETED`, `FAILED`, `ALREADY_RUNNING`, `NOT_FOUND`. Use `ALREADY_RUNNING` when the script is already executing; write the PID and the last-check time there.

## Procedure

1. **Locate** the script by name only in the current directory — never read its contents. Do not search elsewhere.
2. **Ask the user for permission** to execute the script before running it (e.g. via the `question` tool). If the user declines, write the refusal/status to `progress.md` and stop.
3. **Check if it is already executing** with `pgrep -f <script-name>` (or a PID/lockfile if present). Do not read the script to determine this.
4. If **already executing**: write an `ALREADY_RUNNING` status to `progress.md` (PID + timestamp) and report that status to the user. Do **not** launch a second instance.
5. If **not executing**: execute it via `bash ./<script-name>` (background it if it is a long-running loop). Note the PID.
6. After launching, write a `RUNNING` status to `progress.md` (PID, start time).
7. When execution finishes, write `COMPLETED` (with exit code) or `FAILED` (with the observed error/exit code) to `progress.md`.
8. If a **problem** occurs during execution (launch fails, non-zero exit, crash): write the failure status and whatever error output was surfaced to `progress.md`, then inform the user. **Never** open the script to debug it.

## Guidelines

- Never read, view, or debug the script source. Ever.
- Only ever execute the script in the current working directory — never look for or run scripts outside it — **unless** the user explicitly asked for an external script, in which case execute that specific external script only.
- Always obtain the user's permission before executing.
- Never open a second instance if one is already running.
- Keep `progress.md` accurate and up to date; it is the single source of truth for status.
- When in doubt about what to do, write the situation to `progress.md` and report to the user.
