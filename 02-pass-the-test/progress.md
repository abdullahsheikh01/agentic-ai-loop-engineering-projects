# Progress Report

## Iteration 4 — COMPLETE

- **Bugs fixed this turn (1, all remaining):**
  1. `todo_app.py` — `get_task()` returned `self.tasks[index]` and raised IndexError for out-of-range indices; now returns None when index is negative or out of range.
- **Test results:** 108 passed, 0 failed, 0 errors (out of 108).
- **Remaining failures:** none. **All 108 tests pass.**

## Iteration 3

- **Bugs fixed this turn (4):**
  1. `seconds_calculator.py` — `add_seconds()` did not wrap after 24 hours; now wraps using modulo 86400.
  2. `todo_app.py` — `remove_task()` did not match task names case-insensitively.
  3. `todo_app.py` — `mark_complete()` returned True for a missing task; now returns False.
  4. `todo_app.py` — `search()` was not case-insensitive.
- **Test results:** 107 passed, 1 failed, 0 errors (out of 108).
- **Remaining failures (1):**
  - `todo_app.py` (1): `get_task()` raises IndexError instead of returning None for out-of-range index.

## Iteration 2

- **Bugs fixed this turn (4):**
  1. `number_guess.py` — `reset()` did not clear the `won` flag.
  2. `seconds_calculator.py` — `time_difference()` returned a signed difference instead of an absolute one.
  3. `seconds_calculator.py` — `is_valid_time()` did not validate minutes (only hours and seconds).
  4. `seconds_calculator.py` — `hours_to_seconds()` multiplied by 60 instead of 3600.
- **Test results:** 101 passed, 7 failed, 0 errors (out of 108).
- **Remaining failures (7):**
  - `seconds_calculator.py` (3): `add_seconds` doesn't wrap after 24h (`test_add_seconds_wraps_after_midnight`, `test_add_seconds_full_day_wraps`, `test_add_seconds_across_midnight`).
  - `todo_app.py` (4): `remove_task` not case-insensitive; `mark_complete` returns True for missing task; `search` not case-insensitive; `get_task` raises instead of returning None for out-of-range index.

## Iteration 1

- **Bugs fixed this turn (4):**
  1. `seconds_calculator.py` — `to_seconds()` ignored the `seconds` argument (missing `+ seconds`).
  2. `seconds_calculator.py` — `format_seconds()` computed hours with `total // 60` instead of `total // 3600`.
  3. `todo_app.py` — `add_task()` did not reject empty/whitespace-only or duplicate (case-insensitive) tasks.
  4. `todo_app.py` — `pending_tasks()` / `completed_tasks()` returned task dicts instead of task names.
- **Test results:** 89 passed, 19 failed, 0 errors (out of 108).
- **Remaining failures:**
  - `number_guess.py` (7): out-of-range counts as attempt; correct guess not recorded in history; `is_game_over` not true after win; `guess` doesn't return "game over" after loss/win; `last_guess` after correct guess; `reset` doesn't clear `won`.
  - `seconds_calculator.py` (6): `time_difference` not absolute; `add_seconds` doesn't wrap after 24h; `hours_to_seconds` uses 60 instead of 3600; `is_valid_time` doesn't validate minutes.
  - `todo_app.py` (4): `remove_task` not case-insensitive; `mark_complete` returns True for missing task; `search` not case-insensitive; `get_task` raises instead of returning None for out-of-range index.