# Agentic Loop Contract

opencode reads this file at the START of every iteration and performs exactly ONE
loop turn per invocation.

## Goal

Process every pending item in `queue.md` — one item per iteration — until the
queue is empty. This is a template loop; replace the goal with your own
unattended task (e.g. fix a test suite, generate a daily brief, watch a script).

## Per-iteration action

1. Read `queue.md`. Find the first item that is not yet marked `[done]`.
2. Complete that single item (create/modify the relevant files as needed). Do
   not work on more than one item per iteration.
3. Mark the item `[done]` in `queue.md` and record what you did.
4. Update `progress.md` (create it if it does not exist) with a report for this
   iteration: iteration number, which item was processed, and remaining count.

## Check / condition to test (each iteration)

- Confirm `queue.md` exists; if not, create it with at least one pending item.
- After processing, verify the item is now marked `[done]`.
- Count how many items remain unmarked.

## Stop condition

When `queue.md` has **no pending items left** (every item marked `[done]`):
write a final summary into `progress.md` and end your reply with the token
LOOP_DONE.

## Failure handling

- If an item cannot be completed, leave it unmarked, note the blocker in
  `progress.md`, and end with LOOP_CONTINUE so the next iteration can retry.
- If `queue.md` is missing and cannot be created, end your reply with LOOP_FAIL.
- Otherwise end with LOOP_CONTINUE so a new iteration starts.

## Unattended

- [x] Yes — opencode runs fully autonomous; never stop to ask for approval.
- [ ] No — opencode may stop and ask for input.

## Constraints

- Work only toward the goal. Never invent new scope.
- Treat every iteration as independent; do not assume prior iterations succeeded.
- End your reply with exactly one token: LOOP_CONTINUE, LOOP_DONE, or LOOP_FAIL.
