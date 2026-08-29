# new-project

> A new agentic loop. Describe what your loop does here.

This is a self-contained **agentic loop** built with
[opencode](https://opencode.ai). The shell driver only schedules turns; opencode
makes every check, condition test, and decision each iteration, ending with a
single decision token (`LOOP_CONTINUE`, `LOOP_DONE`, or `LOOP_FAIL`).

## Quick Start

Prerequisites: the `opencode` CLI on `PATH`.

```bash
# run one loop turn (starts an opencode server, runs one iteration, then exits)
bash agentic-loop.sh

# run the loop unattended in the background
nohup bash agentic-loop.sh > loop.log 2>&1 &
```

> Command source: `agentic-loop.sh` (driver header + usage).

## Common Commands

```bash
bash agentic-loop.sh                          # run the loop
tail -f loop.log                              # watch loop activity
cat progress.md                               # per-iteration progress log
```

Environment overrides (from the `agentic-loop.sh` header): `INTERVAL`
(seconds between iterations, default `120`), `ITERATION_TIMEOUT` (max seconds per
iteration, default `900`), `LOG_FILE` (default `loop.log`).

## Project Structure

```
06-new-project/
├── agentic-loop.sh              # driver: schedules iterations, reads the LOOP_* decision token
├── loop-prompt.md               # loop contract (goal, per-iteration action, stop condition)
├── opencode.json                # permission config (unattended, allow-all tools)
├── progress.md                  # per-iteration progress log
└── loop.log                     # loop activity log
```

## How the Loop Works

Each iteration opencode:

1. reads `loop-prompt.md` and performs exactly one loop turn,
2. acts toward the goal and runs the per-iteration check,
3. appends a report to `progress.md`,
4. ends with `LOOP_CONTINUE`, `LOOP_DONE` (goal reached), or `LOOP_FAIL`.

## Testing and Quality

- Syntax check: `bash -n agentic-loop.sh`
- Lint: Not found in repo
- Coverage: Not found in repo

## Documentation Maintenance

Update this README when:

- the loop contract (`loop-prompt.md`) goal or iteration steps change
- the driver's commands or environment overrides change

## License

License: Not found in repo — consider adding a LICENSE file.
