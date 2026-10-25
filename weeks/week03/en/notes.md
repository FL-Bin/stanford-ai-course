# Week 3 · Agent Skills and CLI
> Our own study notes (paraphrase + commentary), not the slides. Official materials: [links.md](../links.md). Chinese version: [../zh/notes.md](../zh/notes.md).
> No transcripts were published this week; notes are based on the public slides and readings.

---
## Lecture 5 · 10/6: Agent skills
### Why skills
- MCP is good for third-party integrations, but LLMs are **very good at following longer written procedures**, and exposing that is an important part of any harness.
- A skill is a standard for **dynamically loaded** capabilities: domain-specific, **combining code and prompts**, loaded only when needed — "scripts for agents".
- Typical uses: writing documents, making slides, data analysis.

### Kinds of skills (from the slides)
| Kind | Examples / purpose |
|---|---|
| Code understanding and planning | RePPIT skills; Matt Pocock's grill-me / grill-with-docs (the agent questions you until the task is clear) |
| Verification | A skill that creates verification skills, so the agent checks its own output |
| Code style | Code-level best practices, useful for review agents |
| Misc | e.g. web parsing with browse.sh |

### Best practices (paraphrased)
1. **Keep scope focused**: one skill, one clearly defined task.
2. **Keep your own portable collection** (the slides quote an analogy: chefs bring their own knives between kitchens).
3. **Mine your transcripts**: skills are processes in Markdown — look for where you intervened or corrected the agent.
4. **Don't reinvent the wheel**: give the agent a CLI and wrap the boilerplate in a skill.
5. **State the triggers**: situations and phrases that should invoke the skill.
6. **Progressive disclosure**: a short main file that points to specific files when needed.
7. **Modular, composable skills.**
8. **Keep a verification skill** so there is an improvement loop.

See week 2 for the API vs. MCP vs. skills comparison.

---
## Lecture 6 · 10/8: Guest Lee Robinson — "How always-on agents work"
> The guest deck carries a forward-looking/confidentiality notice; we only summarize the main ideas. See the official deck for details.

- **Starting point**: the week-1 agent stops when you close the terminal. An always-on agent runs on a server with its own cloud computer (a small VM with desktop, browser and files), saves state, memory and skills, wakes on events (your messages, schedules, Slack, calls, finished background work) and can work for months.
- **How collaboration evolved**: copy-paste chat → agents in the terminal (you approve each step) → many agents in parallel in the background/cloud (you review results) → you message an agent with its own computer, tools and memory that keeps going after you leave. From approving steps to **steering**; as models improve, the interface gets simpler.
- **Six new model capabilities**: work for hours; hand off to fresh-context helpers; use real tools (shell, files, browser, MCP); use a computer screen; keep knowledge in files (skills, memory); learn a task by watching a demonstration.
- **Knowledge lives in files**: plain-text memory and skills that both human and agent can read, search and edit; skills load on demand, so having many is cheap.
- **Architecture**: thin client, thick server; all state on the server so the VM can be rebuilt; sleep when idle, wake on events; one turn at a time per conversation; **durable workflows** instead of plain job queues so a crash resumes mid-turn, with **idempotent** steps for safe retries.
- **Harness design**: the model's plain text isn't shown to the user; it talks through a dedicated send tool, and may stay quiet when there's nothing new.

---
## Readings (pointers)
- **pstack (Cursor plugins)** — official plugin/skill examples; study the layout and style.
- **Matt Pocock's skills** — a public skills repo (incl. grill-me) worth imitating.
- **browse.sh** — lets agents browse; useful for web skills.

## Exercises
- [ ] Find 3 places in recent agent chats where you corrected the agent; turn them into one skill
- [ ] Add trigger descriptions and split out a reference file (progressive disclosure)
- [ ] Write a verification skill the agent runs after finishing a task

