# Lecture 1 · 9/22: Course intro + Claude Code in ~200 lines

## 官方材料 / Official materials
| Material | Link |
|---|---|
| Slides (9/22) | [Google Slides](https://docs.google.com/presentation/d/1uztIhjHAG6O_9QOD1N_3wdhwhABml1fANXEN2dGwdbg/edit?usp=drive_link) |
| Sample code | [Google Drive](https://drive.google.com/file/d/1DxKa_autBOu9s8DvItodgUAwH_pBg7aR/view?usp=drive_link) |
| Video | not published yet |
| Transcript | not published yet |
| Related reading | [Building a Coding Agent (YouTube)](https://youtube.com/watch?v=s7ZzkdvCMDY) |


Notes follow the slide order, in our own words.

## 1. State of the world, 2026
A chart slide on how widely AI coding has been adopted.

## 2. What that means for you
Industry-wide adoption means companies need developers who are AI-native. The bar has risen along with productivity. Systems-level thinking, architecture and abstraction, combined with AI-first practice, are what make you hard to replace.

## 3. Principles, not tools
The course deliberately teaches lasting principles rather than specific products.

## 4. The ten weeks on one slide
An overview graphic; see the progress table in the [README](../../../README.md).

## 5. The takeaway
1. **Human-agent engineering:** invest in what AI doesn't yet replace — business and product sense, architectural taste, communication.
2. **LLMs are only as good as you are:** good context produces good code; a codebase you don't understand won't be understood by the model either; guard against AI slop.
3. **Experiment aggressively.**

## 6. Logistics
Instructor Mihail Eric (Head of AI at Monaco; earlier LLM work at Amazon Alexa; founded an ML education startup and a YC-backed AI coding company); CAs Isaac Kan and Vijay Daita. Tue/Thu 5:30–6:20 pm. Six weekly assignments, 3–4 open-source contributions, one open-ended final project; grading 50/15/30/5 (project/assignments/OSS/participation). Fifteen AI-native OSS partners (Vercel, Warp, Marimo, Milvus, CrewAI, OpenHands, Semgrep and others) and guest lectures from the builders of Claude Code, Devin, Replit, Factory and more.

## 7. Building Claude Code in ~200 lines
The point of the slide: it is simple. Read terminal input and append it to the conversation; tell the model which tools exist (`Read_file`, `List_dir`, `Edit_file`); when it asks for one, run it locally and send back the result. Then a live build from scratch — see [03](03_code_walkthrough_minimal_agent.md).

> [!NOTE]
> **Supplement**
> Agent = loop + tools. Self-check: can you explain "good context → good code", and draw the user → harness → model → tools → result loop?
