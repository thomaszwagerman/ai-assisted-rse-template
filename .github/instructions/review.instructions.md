---
description: How to review research code in this repository and report findings (used by the reviewer agent and /audit). Read before reviewing or auditing code.
---

# Reviewing code

Read-only. Report findings; never edit files. Follow `AGENTS.md`.

If the optional community skills are installed (see `AGENTS.md`), also use
`rseng-code-review`, `rseng-defensive-coding`, `rseng-numerical-accuracy`,
`rseng-reproducibility` and `rseng-research-integrity` for the detail behind the checks
below. Where they disagree with this file or `AGENTS.md` (for example they suggest
committing, or implementing fixes during the review), this file and `AGENTS.md` win.
If they are not installed, say so once and carry on with the checks below.

## 1. Understand first

- Review what the user names: a diff, a branch, files or a folder. Nothing named: the
  uncommitted changes, or the last commit if there are none.
- Read the code under review, then what it touches: callers of every changed function,
  the functions it calls, the tests and the docs.
- When a signature, return value or behaviour changes, search for every caller
  (code, tests, docs, config, notebooks).
- State what the code does and how you assume it is used (one-off script, library,
  pipeline, service). Judge findings against that assumption.

## 2. Look for

1. **Correctness:** wrong results, crashes, missed edge cases (empty, zero, one element,
   NaN, last item, off-by-one), callers that disagree with what a function returns, the
   same rule implemented differently in two places.
2. **Reproducibility:** unseeded randomness, global state, dependence on the environment,
   paths, locale, time zone, file order or dictionary and set ordering.
3. **Units and quantities:** are the units of every quantity stated, and consistent from
   input to output? Flag unit-ambiguous names and conversions with no stated source unit.
   If the code uses a units library, check it is used consistently; do not suggest one
   unless asked.
4. **Numerics:** float `==`, tolerances without a stated reason, possible overflow,
   underflow, division by zero or loss of precision, results that depend on summation
   or iteration order. If a judgement needs domain knowledge you lack, write "unsure".
5. **Data and provenance:** inputs with no documented source, version, format or schema;
   hard-coded paths; results that cannot be traced to code and inputs.
6. **Docs against behaviour:** docstrings, docs or comments that disagree with the code.
7. **Tests:** risky logic with no test that would fail if it broke; tests that would
   still pass if the numbers changed; weakened assertions or tolerances; non-determinism.
8. **Silent changes:** anything that could alter previously published results without
   being flagged in the changelog or docs.
9. **Integrity and supply chain:** invented citations, data or claims; new dependencies
   without justification; missing SPDX headers; changed workflow permissions or pins;
   new or changed agent skills, hooks or instructions that steer an agent.
10. **Lean:** dead code, duplicated helpers, abstractions with one use. Lean findings
    must never target docstrings, type annotations, tests, seeds, tolerances with a stated
    reason, or documented assumptions.

## 3. Check before you report

- Every finding needs a file, a line and a concrete case: "this input or situation
  leads to this wrong result". No case, no finding.
- Before calling code unused or a change safe, search the whole tree, including tests,
  docs, config and string references.
- Mark anything you could not confirm as "unsure". Do not guess.
- Propose the smallest fix that works. No style taste, no vague worries.

## 4. Output

Short sentences. Explain a term the first time you use it.

Start with `What this does:` (two or three sentences) and the usage you assumed.

Then findings in three groups, most important first, skipping empty groups:

- **Blocker:** wrong results, lost reproducibility, data loss, a security problem.
- **Should fix:** risky code without a test, unclear units or provenance, docs that
  disagree with behaviour, code that should not exist.
- **Nit:** small improvements.

Number findings across all groups so the user can say "fix 2 and 5". At most 20; say how
many you left out. Each finding has four parts:

1. **Title** (`path/file.py:L40-52`)
   - **What this is:** one or two sentences.
   - **Problem:** the concrete case.
   - **Fix:** the smallest change.
   - **If we skip it:** the consequence.

End with:

- `Verdict:` one line, healthy or what to fix first.
- `Not checked:` what you did not read, run or could not judge.

Nothing found: say `No issues found.` and one line on what you checked. Do not invent
findings to fill the report.

## Project-specific checks

Add checks for your field here (for example conventions for your data formats, units
library, or numerical methods). The agent applies them in addition to the list above.

<!-- Empty in the template. -->

## Limits

This is an automated read of the code. It does not replace tests, numerical validation
or review by a domain expert.
