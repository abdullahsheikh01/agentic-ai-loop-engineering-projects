# Pass the Test

An autonomous **self-fixing loop**: each iteration, opencode reads the loop contract, fixes bugs across three Python files, runs the pytest suite, and logs progress — repeating until every test passes and replying `LOOP_DONE`.

## Quick Start

Prerequisites: the `opencode` CLI on `PATH` and `pytest` (installed in the project venv).

```bash
# create the venv if missing
python3 -m venv .venv && .venv/bin/pip install pytest

# run the loop (starts an opencode server, drives iterations until all tests pass)
bash agentic-loop.sh
```

> Command source: `agentic-loop.sh` (driver header + usage).

## Common Commands

```bash
bash agentic-loop.sh                          # run the loop to completion
.venv/bin/python -m pytest -q                 # run the test suite directly
cat progress.md                               # per-iteration progress log
tail -f loop.log                              # watch loop activity
```

Environment overrides (from the `agentic-loop.sh` header): `INTERVAL` (seconds between iterations, default `120`), `ITERATION_TIMEOUT` (max seconds per iteration, default `900`), `LOG_FILE` (default `loop.log`).

## Project Structure

```
02-pass-the-test/
├── agentic-loop.sh              # driver: schedules iterations, reads the LOOP_* decision token
├── loop-prompt.md               # loop contract (goal, per-iteration action, stop condition)
├── number_guess.py              # buggy source 1
├── seconds_calculator.py        # buggy source 2
├── todo_app.py                  # buggy source 3
├── test_number_guess.py         # tests
├── test_seconds_calculator.py   # tests
├── test_todo_app.py             # tests
├── opencode.json                # permission config (unattended, allow-all tools)
├── progress.md                  # per-iteration bug/test report
└── loop.log                     # loop activity log
```

## How the Loop Works

Each iteration opencode:

1. fixes exactly four bugs in the source files (never the tests),
2. runs `.venv/bin/python -m pytest -q`,
3. appends a report to `progress.md`,
4. ends with `LOOP_CONTINUE`, `LOOP_DONE` (all tests pass), or `LOOP_FAIL`.

## Testing and Quality

- Tests: `.venv/bin/python -m pytest -q`
- Syntax check: `bash -n agentic-loop.sh`
- Lint: Not found in repo
- Coverage: Not found in repo

## Documentation Maintenance

Update this README when:

- the loop contract (`loop-prompt.md`) goal or iteration steps change
- the driver's commands or environment overrides change
- source or test files are added or removed

## License

License: Not found in repo — consider adding a LICENSE file.