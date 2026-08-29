# Loop Engineering Projects

A portfolio of autonomous **agentic loops** built with [opencode](https://opencode.ai): self-contained experiments in which the agent runs an unattended, recurring task — fixing tests, watching a long-running script, or producing a daily brief — driven by a shell scheduler and a prompt contract.

## Repository Overview

| Module | Path | Description | Docs |
|--------|------|-------------|------|
| Watch Loop | `01-a-watch-loop/` | Launches a long-running script and polls its status via a custom opencode skill (`script-watcher-loop`) | [README](01-a-watch-loop/README.md) |
| Pass the Test | `02-pass-the-test/` | Fixes bugs in three Python files until the full pytest suite passes, writing a progress report each iteration | [README](02-pass-the-test/README.md) |
| Morning Brief with Memory | `03-morning-brief-with-memory/` | Researches trending tech news daily, writes an article and five-platform social posts, and appends to a running log | [README](03-morning-brief-with-memory/README.md) |
| New Project | `06-new-project/` | Template agentic loop that processes a `queue.md` task list one item per iteration until empty | [README](06-new-project/README.md) |
| New Project 2 | `07-new-project-2/` | Second template agentic loop (task-queue pattern) on its own branch | [README](07-new-project-2/README.md) |

## Quick Start

Prerequisites: the `opencode` CLI on `PATH`.

```bash
# run one loop turn (starts an opencode server, runs one iteration, then exits)
bash 02-pass-the-test/agentic-loop.sh

# run a module unattended in the background
nohup bash 03-morning-brief-with-memory/agentic-loop.sh > loop.log 2>&1 &
```

> Command source: the per-module shell drivers (`agentic-loop.sh`).

## Shared Commands

Every loop shares the same driver pattern — the shell script only schedules turns; the agent makes every check, condition test, and decision:

- `agentic-loop.sh` — starts an `opencode serve` instance, prompts one loop turn per iteration, and reads the decision token.
- `loop-prompt.md` — the loop contract opencode reads at the start of each turn (goal, per-iteration action, stop condition).
- `opencode.json` — permission config so the loop runs fully unattended.
- `progress.md` — running log appended each iteration.

Each iteration ends with exactly one decision token: `LOOP_CONTINUE`, `LOOP_DONE`, or `LOOP_FAIL`. The driver stops on `LOOP_DONE` / `LOOP_FAIL`.

Drivers expose shell environment overrides (documented in each `agentic-loop.sh` header): `INTERVAL` (seconds between iterations, default `120` in `02`, `300` in `03`), `ITERATION_TIMEOUT` (max seconds per iteration, `02`, default `900`), `LOG_FILE` (default `loop.log`), and `PORT` (opencode serve port, `01`/`03`, default `4096`).

## Project Structure

```
loop-engineering-projects/
├── 01-a-watch-loop/               # watch-loop experiment
├── 02-pass-the-test/              # self-fixing test loop
├── 03-morning-brief-with-memory/  # cron-driven daily brief
├── 06-new-project/                # template task-queue loop
├── 07-new-project-2/              # second template task-queue loop
└── README.md
```

## Testing and Quality

- `02-pass-the-test`: Python test suite via `02-pass-the-test/.venv/bin/python -m pytest -q`
- Syntax check: `bash -n <module>/agentic-loop.sh`
- Lint: Not found in repo
- Coverage: Not found in repo

## Adding a New Loop

1. Create a directory `NN-<name>/`
2. Add `agentic-loop.sh` (copy an existing driver), `loop-prompt.md`, and `opencode.json`
3. Write a module-level `README.md`
4. Update the Repository Overview table above

## Documentation Maintenance

Update this README when:

- a module is added to or removed from the repo
- the shared loop driver pattern or environment overrides change
- a module gains its own README (add the link in the Repository Overview table)

## License

License: Not found in repo — consider adding a LICENSE file.