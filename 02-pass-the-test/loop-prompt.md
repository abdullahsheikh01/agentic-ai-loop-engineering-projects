# Agentic Loop Contract

opencode reads this file at the START of every iteration and performs exactly ONE
loop turn per invocation.

## Goal

Fix ALL bugs in the three source files (`number_guess.py`, `seconds_calculator.py`,
`todo_app.py`) so that every test in `test_number_guess.py`,
`test_seconds_calculator.py`, and `test_todo_app.py` passes (108 tests total).

## Per-iteration action

1. Identify and fix exactly **4 distinct bugs** in the source files
   (`number_guess.py`, `seconds_calculator.py`, `todo_app.py`). Do not modify any
   test files. If fewer than 4 bugs remain, fix all remaining ones.
2. Run the full test suite: `.venv/bin/python -m pytest -q`
3. Update `progress.md` (create it if it does not exist) with a report for this
   iteration: iteration number, bugs fixed this turn, current pass/fail counts,
   and which test failures remain (if any).

## Check / condition to test (each iteration)

- Run the full test suite with `.venv/bin/python -m pytest -q` and count passing
  and failing tests.
- Confirm `progress.md` exists and reflects this iteration's results.
- If the venv or pytest is missing, recreate it with
  `python3 -m venv .venv && .venv/bin/pip install pytest` before running tests.

## Stop condition

When the test suite reports **0 failures** (all 108 tests pass): write a final
summary into `progress.md` and end your reply with the token LOOP_DONE.

## Failure handling

- If a fix makes the test results worse than the previous iteration, revert that
  specific change before ending the turn.
- If pytest cannot run even after recreating the venv, end your reply with
  LOOP_FAIL.
- Otherwise end with LOOP_CONTINUE so a new iteration starts.

## Unattended

- [x] Yes — opencode runs fully autonomous; never stop to ask for approval.
- [ ] No — opencode may stop and ask for input.

## Constraints

- Work only toward the goal. Never invent new scope.
- Never modify the test files.
- Treat every iteration as independent; do not assume prior iterations succeeded.
- End your reply with exactly one token: LOOP_CONTINUE, LOOP_DONE, or LOOP_FAIL.