# Week 4 · Customizing Your Agent and Repository
> Our own study notes (paraphrase + commentary), not the slides. Official materials: [links.md](../links.md). Chinese version: [../zh/notes.md](../zh/notes.md).
> No transcripts were published; the 10/15 guest talk (Boris Cherny) has no public slides, so there are no notes for it yet.

---
## Lecture 7 · 10/13: Customizing your agent setup
### Why customize
- Getting the most out of coding agents means **taking control of your stack**; there are many customization mechanisms.
- Four main ones: **agent behavior files (CLAUDE.md / AGENTS.md), hooks, skills, subagents** — plus MCP servers.

### Extra MCP perks (adding to week 2)
Seamless auth; easy versioning and updates; portability across clients; native sandboxing for remote MCP.

### Writing a good AGENTS.md
Treat it as **a README for the agent**. Suggested sections:
1. Project overview (a map of the codebase)
2. Build and test commands (e.g. "use maven, not gradle")
3. Code style
4. Testing instructions
5. Security considerations
6. Stack-specific gotchas (e.g. "React 18 + TypeScript, built with Vite")

Principles (paraphrased):
- Keep instructions **broadly applicable**; **avoid code snippets** — they go stale.
- **Mind the length** (the slides suggest under 300 lines).
- Large repos: **nested config files**, with the root AGENTS.md acting as a router to deeper docs (e.g. "for API gateway design see docs/API-GATEWAY.md"). Services/team directories can have their own conventions.
- Loading order: CLAUDE.md files load from the root to the nearest file, so **the most relevant instructions are read last**.
- Real example shown: the Next.js repo's AGENTS.md.
- The same principles apply to CLAUDE.md and similar files.

### Hooks
- **Deterministic scripts** on predefined events: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `PreCompact`, …
- Uses: sanitize prompts; block sensitive actions; run linters/formatters on generated code; run tests when a task finishes.
- Supported in Claude Code and Cursor.

### Skills / commands
- Frequently used prompts as files the agent can run: run tests, create a plan, research, review code, verify output.
- Examples mentioned: a "ship-it" command in Claude Code, Cursor's "deslop" command.

### Subagents
- **Runtime delegation**: cleanly separate contexts for different work streams; only the final message comes back.
- Name, description and tool list load at session start; invoked implicitly or explicitly.
- Good for exploring a codebase, simplifying code after a change, end-to-end testing — **perfect for side tasks**.
- Contrast: CLAUDE.md anchors behavior; subagents divide the work.

### Common MCP server types
| Type | Examples | Use |
|---|---|---|
| Project management | Jira / Linear | Create/update issues, pull issue info and start tasks |
| Documentation | Notion / Confluence | Create issues from feature specs |
| Observability | Datadog / Sentry | Real-time production debugging |
| Database | Redshift | Debug data issues, explore data layout |
| Technical docs | Context7 | Avoid stale library definitions, fewer hallucinations |
| Experiment tracking | Arize | Suggest new runs from test output |

### The context story
A request's context stacks up roughly as: system prompt → memory file → environment info → MCP tools → skills → global AGENTS.md → local AGENTS.md. Every layer spends your context budget.

---
## Lecture 8 · 10/15: Guest Boris Cherny (creator of Claude Code, Anthropic)
No slides or transcript published yet; notes will follow.

---
## Readings (pointers)
- **I Still Prefer MCP Over Skills** — a counterpoint on MCP vs. skills.
- **AGENTS.md (Factory docs)** — conventions for AGENTS.md.
- **Steering Claude Code** — Anthropic's guide to skills, hooks, rules and subagents.
- **Writing a Good CLAUDE.md** — how to write a good CLAUDE.md.

## Exercises
- [ ] Rewrite your project's AGENTS.md / CLAUDE.md with the six sections, under 300 lines
- [ ] Add a `PostToolUse` hook that formats or tests after edits
- [ ] Try a plan / implement / review split across three subagents

