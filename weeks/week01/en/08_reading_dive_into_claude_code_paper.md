# Reading · Dive into Claude Code (paper)
*Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems* — Liu, Zhao, Shang, Shen (MBZUAI VILA Lab / UCL), arXiv:2604.14228. Links in [links.md](../links.md). A reading guide in our own words, not a translation.

## What and how
Analyzes Claude Code's publicly available TypeScript source and compares it with two open agent systems, OpenClaw and Hermes Agent.

## Main finding
The core is a simple while loop (call model → run tools → repeat); **most of the code is the system around the loop** — consistent with notes 03–04.

## Five values
Human decision authority · safety, security, privacy · reliable execution · capability amplification · contextual adaptability.

## Design principles (selection, our wording)
Deny by default and escalate to a human · graduated trust · defense in depth · policy in external config · context as a scarce resource · append-only durable state · minimal scaffolding · values over rules · composable extensions · weigh risk by reversibility · transparent file-based config/memory · isolated subagents · graceful recovery.

## Architecture highlights
- **Permissions**: several modes from plan-only to near-bypass, plus a classifier; deny rules win over narrower allow rules; content-matching rules; optional shell sandbox. Contrast: container isolation (SWE-Agent, OpenHands), Git rollback (Aider).
- **Five-stage compaction pipeline** before each model call: budget tool results → snip old history → micro-compaction → collapse long history → semantic auto-summary.
- **Four extension mechanisms**: MCP, plugins, skills, hooks — they differ in how much context they cost.
- **Context and memory**: layered CLAUDE.md + automatic memory. **Subagents** run isolated and return only a summary. Sessions are append-only.

## Comparison
| | Claude Code | OpenClaw | Hermes |
|---|---|---|---|
| Safety | per-action review | perimeter-level access | per-action approval across surfaces |
| Runtime | single CLI loop | inside a gateway control plane | single process, role set by entry point |
| Extension | larger context window | gateway capability registry | pluggable memory/model backends |

## Notable
Cited longitudinal data: auto-approve rates rise with experience (~20% early to 40%+ after many sessions) — trust is built over time. The paper ends with six open directions.

Reading order: §1–3 first, then §5 (permissions), §6 (extensions), §7 (context), §8 (subagents).
