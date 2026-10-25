# Structure of Claude Code's internal prompts (9/24 prompts folder)
> The instructor captured six internal prompt files. We describe their **structure** in our own words; the original texts are not reproduced here — use the official link in [links.md](../links.md).

| File | What it is |
|---|---|
| system_prompt | The main system prompt |
| tool_list | Built-in tools by category |
| config_files | How CLAUDE.md is injected |
| plan_mode | The plan-mode prompt |
| subagent_prompt | One example task brief sent to a subagent |
| compaction_prompt | The context-summary prompt |

## system_prompt
Identity (software-engineering agent) → security boundaries (allow authorized/defensive work, refuse destructive attacks) → harness notes (Markdown output; tools gated by permission mode — adapt instead of retrying a denied call; hook output counts as user feedback; don't follow instructions in pasted content unless the user asks — anti prompt-injection; prefer file tools over shell; parallelize independent calls; cite `file:line`) → match local code style → confirm irreversible/external actions; report results honestly → **file-based memory** (one file per memory, frontmatter, four types, an index file) → environment → context management.
👉 Lesson for your own skills/CLAUDE.md: short, sectioned, principle-based.

## tool_list
Files; Shell; search and code intelligence; agents; plan/isolation; scheduling; artifacts; MCP resources; interaction; design/review.

## config_files
A fixed header saying the instructions override defaults, followed by the project's CLAUDE.md (overview, structure, run commands, code style). 👉 A "just enough" CLAUDE.md template.

## plan_mode
Hard rule: only the plan file may be edited; read-only otherwise, overriding all other instructions. Phases: understand (≤3 parallel Explore subagents, usually 1; look for reusable code) → design (Plan subagents, skippable for small tasks) → review → final plan → submit for approval.

## subagent_prompt
A performance-analysis brief: constraints (don't modify the repo or real data; use temp paths and a scratch dir) → background per module → what to cover (complexity, measurements at several scales, concurrency/integrity, growth, ranked recommendations) → output format, **separating measured facts from inference**.
👉 A good subagent brief = goal + no-go zones + known context + deliverable format.

## compaction_prompt
Text only, no tool calls → chronological analysis first, then a summary with fixed sections (requests, concepts, files, errors/fixes, problem solving, all user messages, pending tasks, current work, next step) → keep safety constraints exact; only real user messages count as user messages.
👉 Use this checklist when you write a handoff note or run `/compact`.
