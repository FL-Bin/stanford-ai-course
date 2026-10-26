# Reading · Lessons from Building Claude Code: Seeing like an Agent

## 官方材料 / Official materials
| Material | Link |
|---|---|
| Article (X) | [@trq212 on X](https://x.com/trq212/status/2027463795355095314) |

By @trq212 (Claude Code team), Feb 2026. Notes in our own words, following the article's order.

## The question: how to design the agent's action space
One do-everything tool or fifty special ones? The author's analogy: which tools you want for a hard math problem depends on your own skills. **Fit tools to what the model is good at** — learn that by watching its outputs and experimenting ("see like an agent").

## Case 1 · AskUserQuestion
Adding a questions parameter to the exit-plan tool confused the model; a special Markdown question format was unreliable; a dedicated tool that blocks until the user answers worked — structured, reusable, and the model *likes* calling it. Lesson: a well-designed tool is useless if the model won't use it.

## Case 2 · From Todo to Tasks
Periodic todo reminders helped early models but constrained stronger ones; shared Tasks with dependencies replaced TodoWrite for multi-agent work. Lesson: re-check old tools as models improve.

## Case 3 · From RAG to Grep
Vector search was fast but fragile and "fed" context; giving the model Grep let it build its own context. Skills formalize **progressive disclosure** (files reference files, read on demand).

## Case 4 · A guide subagent instead of a new tool
Each new tool is one more option for the model to weigh, so the bar is high. To answer rare "how do I use Claude Code" questions without context rot, they added a docs-lookup subagent that returns only the answer.

## Conclusion
No fixed rules — tool design is art and science; experiment and read outputs.

> [!NOTE]
> **Supplement**
> The lecture says ~40 built-in tools, the article (Feb 2026) ~20 — different dates and counting.
