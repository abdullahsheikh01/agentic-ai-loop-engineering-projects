# Morning Brief with Memory

An unattended agentic loop that runs daily at 9:30 AM: it searches the web for trending tech news, writes an in-depth article and a five-platform social post, and records each day's progress in a running log.

## Quick Start

Run the loop once manually (starts an `opencode serve` instance, runs one full turn, then exits):

```bash
bash agentic-loop.sh
```

For an unattended background run:

```bash
nohup bash agentic-loop.sh > loop.log 2>&1 &
```

The loop is fully scheduled via cron at 09:30 every day:

```bash
30 9 * * * cd /home/abdullahshaikh/code/agent-factory-projects/loop-engineering-projects/03-morning-brief-with-memory && /bin/bash agentic-loop.sh >> loop.log 2>&1
```

> Command source: `agentic-loop.sh` header (Usage / Env overrides) and the installed crontab.

### Prerequisites

- The `opencode` CLI at `~/.opencode/bin/opencode` (the driver prepends this to `PATH` on line 15).
- The `cron` daemon running (auto-starts at boot on Ubuntu via `cron.service`).
- The loop runs unattended; all tool permissions are pre-approved in `opencode.json`.

## Common Commands

```bash
bash agentic-loop.sh                        # run one loop turn
nohup bash agentic-loop.sh > loop.log 2>&1 &  # run in background
tail -f loop.log                            # watch loop activity
cat progress.md                             # read daily progress entries
ls articles/ posts/                         # list generated briefs
```

Environment overrides (from `agentic-loop.sh` header):

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `4096` | Port for `opencode serve` |
| `INTERVAL` | `300` | Seconds between loop iterations |
| `LOG_FILE` | `loop.log` | Where loop activity is appended |

## Project Structure

```
03-morning-brief-with-memory/
├── agentic-loop.sh   # scheduler driver — starts the server and drives loop turns
├── loop-prompt.md    # the loop contract opencode reads each turn
├── opencode.json     # permission config (unattended, allow-all tools)
├── articles/         # daily articles: <YYYY-MM-DD>-<topic>-article.md
├── posts/            # daily posts: <YYYY-MM-DD>-<topic>-post.md
└── progress.md       # running log; one dated paragraph appended per day
```

Each daily brief generates:

- `articles/<date>-<topic>-article.md` — in-depth news explainer (what happened, context, why it matters, implications) with a `## Tags` section of exactly 5 topic tags.
- `posts/<date>-<topic>-post.md` — a single file with five platform-specific posts: **LinkedIn**, **X** (≤ 280 chars), **Facebook**, **Discord**, and **WhatsApp**.
- One appended paragraph to `progress.md` dated `YYYY-MM-DD` (existing content is never modified).

## Testing and Quality

- Syntax check: `bash -n agentic-loop.sh`
- Lint: Not found in repo
- Coverage: Not found in repo
- No test files found in repo

## Documentation Maintenance

Update this README when:

- the loop contract (`loop-prompt.md`) output format changes — e.g. new sections in the article or post files
- the driver's commands or env overrides change
- the cron schedule or project path changes

## License

License: Not found in repo — consider adding a LICENSE file.