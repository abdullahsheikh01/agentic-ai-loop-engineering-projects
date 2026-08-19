# Agentic Loop Contract

opencode reads this file at the START of every iteration and performs exactly ONE
loop turn per invocation.

## Goal

Each morning, produce a daily tech brief: search the internet for the day's
trending tech news, write a detailed article and a short social post for the top
story, and record today's progress. The full task must complete in a single turn.

## Per-iteration action

1. Determine today's date in the format `YYYY-MM-DD`.
2. Search the web for today's trending tech news using the `websearch` tool
   (query something like "trending tech news today").
3. Pick the single most significant / most trending topic from the results.
4. Create `articles/<YYYY-MM-DD>-<topic>-article.md` explaining the news in
   depth: what happened, the context, why it matters, and its implications.
   Include a "Tags" section listing EXACTLY 5 topic tags (e.g. a `## Tags`
   heading followed by 5 keywords relevant to the story).
5. Create a SINGLE file `posts/<YYYY-MM-DD>-<topic>-post.md` containing posts
   for five platforms, each as its own clearly labeled section:
   1) **LinkedIn** — professional, longer-form post
   2) **X** — short tweet (max 280 characters), punchy, with hashtags
   3) **Facebook** — conversational post, a few sentences with hashtags
   4) **Discord** — chat-style message, casual and brief
   5) **WhatsApp** — one concise, friendly message
   `<topic>` must be the same short hyphenated slug as in the article filename.
6. Update `progress.md` by APPENDING exactly one paragraph that starts with
   today's date (`YYYY-MM-DD`) and summarizes what was done. Never modify,
   delete, or reorder any existing content in `progress.md`.

## Check / condition to test (each iteration)

Before acting, check whether today's files already exist (glob for
`articles/<YYYY-MM-DD>-*.md` and `posts/<YYYY-MM-DD>-*.md`). If both exist,
today's brief is already complete — do not create duplicates or append a second
progress paragraph.

## Stop condition

When today's article and post are created AND `progress.md` is updated, end your
reply with LOOP_DONE. If today's files already exist and progress was already
recorded, end with LOOP_DONE without changing anything.

## Failure handling

If the web search returns nothing usable or any file cannot be written, retry
once. If the day's brief still cannot be completed, end your reply with
LOOP_FAIL and explain what failed.

## Unattended

- [x] Yes — opencode runs fully autonomous; never stop to ask for approval.

## Constraints

- Work only toward the goal. Never invent new scope.
- Treat every iteration as independent; do not assume prior iterations succeeded.
- Never delete, overwrite, or reorder existing content in `progress.md`; only append.
- Use exactly the filename patterns `<YYYY-MM-DD>-<topic>-article.md` and
  `<YYYY-MM-DD>-<topic>-post.md` (same topic slug in both).
- The article must include a Tags section with EXACTLY 5 topic tags.
- The post file must contain all five platform sections (LinkedIn, X, Facebook,
  Discord, WhatsApp) in one single file.
- End your reply with exactly one token: LOOP_CONTINUE, LOOP_DONE, or LOOP_FAIL.