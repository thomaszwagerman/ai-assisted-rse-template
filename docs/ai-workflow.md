<!--
SPDX-FileCopyrightText: 2026 Your Name

SPDX-License-Identifier: MIT
-->

# AI-assisted workflow

How this repository is set up for AI assistants, and a workflow that keeps you in control.
The principle: **the assistant drafts, you decide.** You are the author and remain
responsible for correctness, licensing and the scientific claims.

## What is configured

| File | Purpose |
|---|---|
| `AGENTS.md` | Single source of truth for commands, conventions, integrity rules, and what to ask first. Read by Copilot and other agents (Claude Code, Codex, Cursor, ...). |
| `.github/copilot-instructions.md` | Short Copilot-specific pointer to `AGENTS.md`. |
| `.github/instructions/*.instructions.md` | Rules that apply only to matching files (`applyTo`). |
| `.github/prompts/*.prompt.md` | Reusable workflows. Type `/` in Copilot Chat to run them: `/audit`, `/fair-review`, `/release`, `/write-tests`, `/explain-code`. |
| `.github/agents/*.agent.md` | Personas with restricted tools: `planner` (read-only), `implementer`, `reviewer` (reports, does not edit), `docs-writer`. |
| `.github/instructions/review.instructions.md` | How `/audit` and the `reviewer` agent review code and report findings. Add checks for your field in its "Project-specific checks" section. |

## Community skills (optional)

This template does not ship its own agent skills. We recommend the community
[rseng-agent-skills](https://github.com/fdiblen/rseng-agent-skills) collection: 67 skills
for research software practice (testing, FAIR metadata, citation, releasing,
reproducibility, review). Follow its README for installation, updates and removal.
The prompts and agents in `.github/` work without it, and use the skills when they are
installed. Where a skill disagrees with `AGENTS.md`, `AGENTS.md` wins.

## A loop that works

1. **Plan** with the `planner` agent. It cannot edit files, so you get a plan to critique
   before anything changes. Correct wrong assumptions here, where it is cheap.
2. **Implement in small steps** with the `implementer` agent. It writes tests first, runs
   `make check` and stops to ask before touching dependencies or workflows. One small
   change per session beats one large one.
3. **Verify yourself.** Run `make check`, read the diff, and run the code. Do not accept
   "tests pass" without seeing the output.
4. **Review** with the `reviewer` agent, which looks for what the author missed: unseeded
   randomness, weakened tolerances, unclear units, missing docs, new dependencies.
   Use `/audit` for a read-only look at a whole folder or the repository, and
   `/fair-review` for metadata and sustainability. `/audit` and the `reviewer` follow
   `.github/instructions/review.instructions.md`; add checks for your field in its
   "Project-specific checks" section. An automated review does not replace tests,
   numerical validation or a domain expert.
5. **Commit** in small Conventional Commits. You wrote it, you own it.

## Habits that protect scientific integrity

- Treat generated references, DOIs, numerical constants and "facts" as unverified until you
  check the source. Models fabricate plausible citations.
- Never let an assistant change a test, tolerance or expected value to make a run pass
  without you understanding why.
- Do not paste unpublished data, personal data, credentials or embargoed material into a
  hosted assistant. Check your institute's policy.
- Keep results reproducible: seeds, pinned environment (`uv.lock`), recorded versions.
- If AI contributed substantially to a published analysis, record that in your methods or
  acknowledgements according to your funder and journal rules.

## Keeping the setup healthy

- Update `AGENTS.md` when a command or convention changes. Stale instructions cause bad
  suggestions.
- When you correct the assistant twice for the same thing, write the rule down in
  `AGENTS.md` or a scoped instruction file.
- When you repeat a prompt, turn it into a prompt file.
- Keep instructions short and specific. Long vague rules get ignored.
- Review changes to `.github/` like code: they steer an agent that can edit your repository.

## Getting better at it

- Give context: link the issue, name the files, state the acceptance criteria.
- Ask for the plan, the assumptions and the uncertainties, not only the answer.
- Use the assistant to learn: `/explain-code`, ask for alternatives and trade-offs.
- Keep a short log of where it helped and where it misled you, and fold the lessons back
  into the instruction files.
