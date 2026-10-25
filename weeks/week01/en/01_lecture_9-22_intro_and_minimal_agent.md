# Lecture 1 · 9/22: Course intro + building a coding agent in ~200 lines
> Our notes, not the slides. Slides: see [links.md](../links.md).

## What the course is about
- Industry now writes a lot of code with AI, so being **AI-native** is the new baseline for engineers.
- Higher productivity raises the bar: the instructor stresses combining **systems thinking, architecture and abstraction** with an AI-first workflow.
- The course teaches **principles, not tools** — tools change, principles last.

## Three core ideas (our reading)
1. **Human-agent engineering**: focus on what AI can't replace yet — understanding the business and product, making architecture calls, developing taste, communicating.
2. **The model is only as good as you are**: good context → good code. If you can't explain your codebase, neither can the model. Watch out for **AI slop**.
3. **Experiment aggressively** with tools and workflows.

## Format (Fall 2026)
- Instructor Mihail Eric, two CAs; Tue/Thu lectures.
- Grading: final project 50%, open-source contributions 30%, weekly assignments 15%, participation 5%.
- A group of AI-native open-source projects act as "OSS partners" that students send PRs to; most Thursdays are industry guest talks.

## Live demo: the smallest possible agent
**Agent = a loop + a set of tools.**
1. Read user input in the terminal and append it to the conversation.
2. Tell the model which tools exist (read file, list directory, edit file).
3. When the model asks for a tool, run it locally and send the result back.
4. When the model stops asking for tools, print the answer and wait for the next input.

Walkthrough: [03](03_code_walkthrough_minimal_agent.md).

## Self-check
- [ ] Explain "good context → good code" in your own words
- [ ] Draw the loop: user → harness → model → tool → result back

