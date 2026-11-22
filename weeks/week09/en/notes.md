# Week 9 · The Software Factory

[中文](../zh/notes.md) | **English**

## 官方材料 / Official materials

| 材料 Material | 链接 Link |
|---|---|
| 课程大纲 Syllabus | [themodernsoftware.dev](https://themodernsoftware.dev) (Week 9: the software factory as an operating model; self-running, self-improving software systems; running and securing agents post-deployment) |
| 11/17 Slides | [Google Slides](https://docs.google.com/presentation/d/1hxlLspHQ2WOs2tZmCN3gdDi7dfbbRorxzPr65HyyE6Y/edit) |
| 11/19 嘉宾 Guest (Michele Catasta, Replit) | 未发课件 No slides published |
| 文字稿 / 视频 Transcripts / Video | 官网暂未发布 Not published yet |
| 阅读 Readings | [Warp factory example: issue to PR](https://github.com/warpdotdev/warp-factory-examples/tree/main/examples/02-sdlc-issue-to-pr) · [The Software Factory](https://software-factory.dev) · [OpenInspect](https://openinspect.dev) · [WarpBench](https://warp.dev/factories/benchmarks/warpbench) |
| 全部链接 All links | [links.md](../links.md) |

The 11/17 slides are published; below they are summarized in slide order in our own words, followed by a short summary of each reading. The 11/19 guest lecture has no published materials yet. The full walkthrough is in [Chapter 9](../../../book/en/09-the-software-factory.md). Chinese version: [../zh/notes.md](../zh/notes.md).

Note: the official schedule changed after the term began. Week 9 was originally "Building an AI-Native Team" (guests Elad Gil and Amjad Masad); it is now "The Software Factory" with guest Michele Catasta, President of Replit, and the AI-native team topic moved to Week 10. These notes follow the current schedule.

## Lecture 17 · 11/17: The Software Factory and self-improving software systems

### 1. Logistics
- Assignment 6 due Sunday; Thursday guest Michele Catasta (President, Replit), in STLC 111.

### 2. Why now
- Coding agents have become very good, so orchestration of software tasks is moving from humans *in* the loop to humans *on* the loop.
- Most software work follows a fairly predictable shape, so this is the next step for automation workflows.

### 3. Definition: three parts of a software factory
- **A production line:** a fleet of cloud background agents that take work from wherever it originates (an issue, a Slack thread, a Sentry alert, a cron schedule), do it in an isolated environment and return a PR.
- **Quality control:** CI, static analysis, tests and an AI reviewer that check every artifact against the same standard, regardless of who or what prompted it.
- **A feedback loop:** when a defect slips through, the system captures why and turns it into a doc, a skill, a lint rule or a tool, so the defect rate falls over time.
- Humans move from execution toward intent, judgment, governance and system design.

### 4. Factory prerequisites
- Tool access, an isolated control plane, agent readiness.
- Agent readiness cites Eric Zakariasson (Cursor) at AIE Europe 2026, in three parts:
  - **Runnable:** can an agent start your dev environment with no human in the loop? If so, you can scale it out on separate VMs;
  - **Accessible:** can it reach the external context and tools the task needs?
  - **Verifiable:** can it verify its own changes? The speaker argues people should spend much more time building verifiable systems.

### 5. Anatomy of a software factory
- The slides use a diagram from Zach Lloyd (not reproduced; see slides), read left to right:
  - Work arrives from Slack, Linear, GitHub issues, schedules or alerts;
  - An orchestrator runs triage, spec, implement, review, verify;
  - Then ship (PR, merge, deploy) and monitor.
- Everything is governed by a factory definition in code: skills, rules / AGENTS.md, automation config. Each agent runs in its own isolated sandbox; verification means tests/CI, AI judges and computer-use checks.
- Humans sit at three gates: approve the spec, risk-tiered review, product check.
- Two loops: monitoring files new issues back into triage; telemetry (cost per PR, cycle time, human touches) lets observer agents open PRs against the factory definition, which humans merge.

### 6. One full pass through the factory (from Zach Lloyd)
1. A triage agent tries to understand and reproduce the issue: automatable → implementation agent; unclear scope → spec agent; too ambiguous → ask a human and rerun, or park it;
2. (If needed) a spec agent writes a spec; a human reviews it and passes it on;
3. An implementation agent writes code;
4. A review agent reviews it;
5. A verification agent checks via computer use or other means;
6. A human reviews code and verification output, sending it back to steps 2–5 if needed;
7. CI / CD;
8. Ship;
9. A monitoring agent runs and files issues as needed, closing the loop.

(The slide's numbering skips 7; renumbered here.)

### 7. Tasks suited to the factory
PR reviews, CI failures, merge conflicts, first-pass investigation of production incidents, security vulnerabilities.

### 8. What humans do
- Move from worker to manager: plan synchronously, execute asynchronously;
- Route review by risk: humans own security, data and payments;
- An agent going off the rails is a signal to improve the factory;
- Humans stay accountable for what ships.

### 9. Judges score every run
- An LLM judge grades each whole run against the spec instead of going on vibes. The slides mention a scorer from Zach Lloyd's demo that catches agents writing redundant tests.
- Spotify Honk's judge checks the diff against the original prompt, vetoes about a quarter of sessions, the agent recovers about half the time, and the most common trigger is going outside the prompt.

### 10. Benchmark on your own history
- Private benchmarks beat public ones: replay your own past tasks to compare models and harnesses on cost vs. quality.

### 11. Factory metrics
- Cost per PR and cycle time;
- Human touches per PR;
- Share of merged PRs that went through the factory;
- Not lines of code or tokens.
- The slides caution that Zach Lloyd reports cost per PR trending down, but exact figures vary across sources, so treat it as a trend.

### 12. Two ways to build one
- **Frankenstein:** stitch together existing workflows (Claude automations, Devin, etc.);
- **Infrastructure as code:** the whole factory definition lives in code like Terraform (e.g. Warp): a versioned file in the repo you can diff, review and roll back.

### 13. Crawl, walk, run
- Crawl: point automations at chores (triage, review, Sentry fixes, CI self-heal) in standardized repos with good tests;
- Walk: one end-to-end factory on a simple product surface;
- Run: complex repos.
- Meet people where they work (Slack, Linear, GitHub) rather than a new portal; encourage, don't require; use risk tiers to decide what is auto-approved and what goes to people.

## Lecture 18 · 11/19: Guest Michele Catasta (President, Replit)

Materials and recording not yet published. The instructor's preview on X says Replit calls itself a "self-driving company" and predicts every Fortune 500 company will be one by 2030; Replit's engineers nearly tripled code output in the first half of 2026 while review times, reverts and incidents stayed flat. Will be added once available. Related public talks are in [links.md](../links.md).

## Key points from the readings

### Warp factory example: issue to pull request
- A complete engineering factory: requests from Slack, Linear and GitHub go through triage, a spec when needed, and implementation, then another agent reviews before the PR goes to a human.
- Five default agents (FOREMAN, TRIAGE, SPEC, IMPLEMENT, REVIEW) plus a custom one; the reviewer uses a different model from the implementer to reduce shared blind spots.
- Different stages use different runners: 4 vCPU / 8 GB Linux for stages that read code and write prose, 8 vCPU / 16 GB for implementation (compiling and testing), macOS for mobile builds.
- GitHub intake fires only when both a mention/assignment filter and a routing label match; the example warns to widen filters carefully.
- It also includes scorers: one for implementation runs with self-improvement on, one for review runs.

### The Software Factory (Ona's public experiment)
- Goal: build a real product (Memo, a Notion-style notes app) with zero human-written code, livestreamed over ten days.
- Day-ten numbers: 375 PRs merged, 50k+ lines of code, 16 automations, 1,067 tests, 87% autonomous rate, median PR-to-merge 4.9 minutes.
- Main lessons: spec quality determines output quality; the operations side needed more automations than the build side.
- The company's COO stress-tested the app and filed 12 bugs; the factory had been fixing bugs too, just not the same ones: Sentry catches runtime errors, while visual and interaction bugs still need a human to point them out.

### OpenInspect
- An open-source, self-hostable background coding agent framework, modeled on Ramp's Inspect (a Week 8 reading).
- Control plane on Cloudflare Workers and Durable Objects for sessions and streaming; data plane on Modal sandboxes running the agents; a Next.js web client with GitHub login.
- Its pitch: PMs and designers can turn ideas straight into PRs, and sessions are collaborative.

### WarpBench: Evaluating coding agents
- Warp had its foreman agent pick 30 representative tasks (sized S, M, L, XL) from past agent runs, replayed them in their original environments, and scored them with judges on cost, quality and other dimensions.
- A full run took 3h 46m and cost $2,130.57, so the post suggests running it only when new models ship or configuration changes significantly.
- After switching the default implementation model based on the results, Warp's internal cost per completed PR fell from about $80 to about $30 with merge rate unchanged, and task-compliance scores rose from 69% to 87% (figures as reported in the post).

> [!NOTE]
> **Supplement**
> The four readings cover four sides of a factory: the Warp example shows what a factory definition in code looks like, Ona's experiment what happens when one actually runs, OpenInspect the base of a production line, and WarpBench how to know the factory is getting better. Week 8 was a single production line; this week closes the loop.
