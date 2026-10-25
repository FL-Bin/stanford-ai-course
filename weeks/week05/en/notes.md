# Week 5 · Agent-Ready Codebases
> Our own study notes, not official material. Links: [links.md](../links.md). Chinese version: [../zh/notes.md](../zh/notes.md).
> ⚠️ As of 2026-10-25 (Beijing time) the site **has not published** slides or transcripts for this week, so this page has only the topic outline, reading pointers and exercises. It will be completed when materials appear.

## Topics (from the official syllabus)
- **Tue 10/20**: repository agent readiness — what makes a codebase agent-friendly (structure, docs, tests, checks), how to score and audit it, common blockers.
- **Thu 10/22**: guest Eno Reyes (Factory CTO).

## Links to earlier weeks (our synthesis)
- Week 2: good research docs and specs help agents onboard — a clear codebase makes that much easier.
- Week 4: AGENTS.md, hooks and subagents are direct levers for agent readiness.

## Agent-readiness self-check (ours, unofficial)
| Area | Check |
|---|---|
| Docs | AGENTS.md/CLAUDE.md with codebase map, build/test commands, style, gotchas; nothing stale |
| Structure | Clear directories and module boundaries; consistent naming; nested docs in big repos |
| Build | One command to install, one to run |
| Tests | Fast tests the agent can run to verify its own changes |
| Checks | Lint, format and type checks run automatically (hooks/CI) |
| Feedback | Clear error messages the agent can act on |

## Readings (pointers)
- **Making Codebases Agent Ready (video)**
- **Making Ergonomic Repositories (X post)**

## Exercises
- [ ] Watch the video and read the post
- [ ] Score one of your repos with the checklist and fix the weakest area
- [ ] Revisit when the slides are published

> 💡 **Gaibin's note**: (to be added)
