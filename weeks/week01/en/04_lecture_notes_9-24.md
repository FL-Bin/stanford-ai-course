# 9/24 lecture notes · Anatomy of a modern coding agent
> Our paraphrased notes in lecture order, not a transcript. The official transcript is linked in [links.md](../links.md).

## Logistics
- Final project spec is out, with ~4 milestones (including a proposal) to avoid last-week vibe coding. Teams of up to 2 humans, any number of agents.
- Credits from several coding-agent vendors were arranged; OSS partners introduced the following week.

## From the 200-line agent to a modern harness
- Everything except the model itself is observable from the outside. Demo: Claude Code with a newly released model.
- Thesis: harness design may be the hardest and most important problem for coding agents — and for agents in sales, law, support, etc.

## Method: capture the traffic
- A proxy intercepts Claude Code's requests/responses (like Wireshark or browser devtools). **Assignment 1 is to do this yourself.**
- Request shape: `model` + `messages` (user/assistant/system) + `tools` + `system`; the harness injects some messages silently.

## Tool list
- Each tool: name, description, parameter schema. ~40 native tools (files, Bash, search, LSP, agents, plan/worktree, scheduling, artifacts, MCP resources, interaction).
- MCP tools carry an `mcp__` prefix. **All tool definitions ride along on every request**, so too many MCP servers bloat context.
- **MCP vs. skills**: an MCP tool is a primitive (one call, input → output); a skill composes tools, scripts and glue prompts into a multi-step procedure and uses **progressive disclosure** (metadata first, full text when needed).
- History: Claude Code took off partly because its harness was minimal; early MCP servers with ~100+ tools were bloated. Trend: start with 3–5 strong "Swiss-army" tools.

## System prompt
- Recent versions are much shorter than earlier ones; the instructor guesses that know-how (e.g. Git usage) moved into model weights.
- Sections: identity, safety, harness notes, session notes, **file-based memory**, environment, context management.
- You don't control it but it costs context on every request — possibly tens of thousands of tokens before your first message.
- Why no RAG for memory? Benchmarks suggest flat files are often enough.

## CLAUDE.md / AGENTS.md
- Same idea; AGENTS.md is the cross-tool standard. A symlink can connect them.
- It is the "system prompt you control", injected before the first user message with an instruction that it overrides defaults.
- Keep it short: run/test/start commands; too much over-constrains the model; avoid big code blocks.

## Plan mode
- Enter/exit tools; on entry a long planning prompt is injected: understand (Explore subagents) → design → review → final plan → exit. Output is a plan file.

## Skills
- A written procedure. Demo: a "check code quality" SKILL.md describing good vs. bad code; the harness injects a command message, then loads the SKILL.md.

## Subagents
- The main agent orchestrates fresh-context workers, possibly in parallel; exploration doesn't pollute the main context.

## Hooks and compaction
- Hooks only mentioned briefly. Compaction runs automatically near the limit or manually, using a dedicated summary prompt, replacing history with the summary.

## Takeaways
- The trend is **simplicity**: fewer, stronger tools; more trust in the model. "Dumb zone" is a joke term, not jargon, for degraded quality on long contexts.
