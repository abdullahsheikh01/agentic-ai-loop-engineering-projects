# Watch Loop

An experiment in **agentic watch loops**: a bash driver launches a long-running script, then polls its status in a loop — using opencode and a custom skill (`script-watcher-loop`) — until the task completes. The driver and agent never read the script source; they locate it by name and execute it.

## Quick Start

Prerequisites: the `opencode` CLI on `PATH`.

```bash
# run the watch loop (starts an opencode server, launches script.sh, polls until done)
bash run-opencode-loop.sh
```

> Command source: `run-opencode-loop.sh` (driver header + usage).

## Common Commands

```bash
bash run-opencode-loop.sh          # run the watch loop (default poll 70s)
bash run-opencode-loop.sh 30       # poll every 30 seconds
bash script.sh                     # run the long-running task directly
cat progress.md                    # current script status
cat output.txt                     # task output when completed
```

The driver accepts an optional poll interval as its first argument (default `70` seconds) and reads `PORT` from the environment (default `4096`).

## Project Structure

```
01-a-watch-loop/
├── run-opencode-loop.sh            # driver: starts opencode server, polls script status
├── script.sh                       # simulated long-running task (180s)
├── .agents/skills/script-watcher-loop/SKILL.md  # custom skill: execute + track status
├── AGENTS.md                       # project rule: execute the script, never read it
├── progress.md                     # status file: RUNNING / COMPLETED / FAILED / ...
└── output.txt                      # result written by script.sh on completion
```

## Testing and Quality

- Syntax check: `bash -n run-opencode-loop.sh script.sh`
- Lint: Not found in repo
- Coverage: Not found in repo

## Documentation Maintenance

Update this README when:

- the driver's arguments or environment overrides change
- the watch-loop skill changes
- new scripts are added

## License

License: Not found in repo — consider adding a LICENSE file.