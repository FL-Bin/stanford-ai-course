# Lecture 2 · 9/24: The anatomy of a modern coding agent
> Our notes, not the slides. Lecture details: [04](04_lecture_notes_9-24.md).

## From the minimal loop to a full harness
Production agents such as Claude Code wrap the loop in a **harness**; the instructor calls harness design one of the most important problems in coding agents. Eight parts:

| Part | One-line explanation (ours) |
|---|---|
| System prompt | The agent's master instructions: behavior, guardrails, environment |
| Config files (AGENTS.md / CLAUDE.md) | User-written project instructions that take priority over defaults |
| Tool list | Few, powerful tools; names, descriptions and signatures are themselves prompt text |
| Plan mode | Write a spec/plan and clarify requirements before editing |
| Subagents | A fresh context for a side task that returns only its conclusion; parallel but costs more tokens |
| Skills | A written procedure (prompt + optional scripts) loaded on demand |
| Hooks | Code or prompts run automatically at fixed lifecycle points, good for pre/post-processing |
| Compaction | Summarize history when the context fills up; lossy |

## Three principles of a good harness (paraphrased)
1. **Simplicity**: a few general tools (bash, sql) beat many narrow ones.
2. **Protect the context window**: overfilled context makes the model worse (the instructor jokingly calls it the "dumb zone"); avoid tool bloat.
3. **Prompts keep changing**: structure them so they are easy to iterate.

## Self-check
- [ ] Name the eight parts and say which are always in context vs. loaded on demand

> 💡 **Gaibin's note**: (to be added)
