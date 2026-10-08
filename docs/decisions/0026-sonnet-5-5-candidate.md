# ADR 0026: Sonnet 5.5 replaces Sonnet 5 as an evaluation candidate

- Status: Accepted (by Hannes in the demo fork, 2026-10-08; still proposed upstream)
- Date: 2026-10-07
- Decision: D14 (amends the candidate list of ADR 0002)

## Context

ADR 0002 names Claude Opus 5.5 and Claude Sonnet 5 as the VLM candidates. Since then, Claude Sonnet 5.5 has been released and Claude Sonnet 5 is listed as a legacy model ([models overview](https://platform.claude.com/docs/en/models/overview), checked 2026-10-07).

Facts about Claude Sonnet 5.5 from the official documentation, checked 2026-10-07:

- Claude API ID `claude-sonnet-5-5`, at the same price as Claude Sonnet 5 ([models overview](https://platform.claude.com/docs/en/models/overview)); the price is recorded only in `schema/eval/models.yaml` (C-3).
- Default effort `high`; its effort levels are recalibrated, so a level does not produce the same amount of thinking as on Claude Sonnet 5 ([effort](https://platform.claude.com/docs/en/build-with-claude/effort)).
- High-resolution image tier, like the other candidates ([vision](https://platform.claude.com/docs/en/build-with-claude/vision)), so ADR 0011's derived-image rule is unchanged.
- Supports structured outputs on the Claude API ([structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)).
- Listed among the Claude models on Google Cloud ([Claude on Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)); availability on the `eu` multi-region endpoint is **not yet verified**.

## Decision

- The candidates are **Claude Opus 5.5** and **Claude Sonnet 5.5**. Claude Sonnet 5 is dropped.
- Claude Fable 5.1 remains the accuracy reference, not a candidate.
- Evaluation matrix: Opus 5.5 and Sonnet 5.5 each at effort `low` and `medium`; Fable 5.1 at its default effort. Because Sonnet 5.5's effort levels are recalibrated, no settings are carried over from Sonnet 5.
- Selection criteria are unchanged (ADR 0002): silent error rate, then P90 latency ≤ 25 s, then cost.

## Consequences

- When this ADR is accepted, ADR 0002's status notes that its candidate list is amended by this ADR.
- A follow-up PR updates DEV_PLAN (both languages) and the PRD where they name Sonnet 5.
- `schema/eval/models.yaml` (C-3) lists Opus 5.5, Sonnet 5.5 and Fable 5.1.
- Before the server-side proxy milestone (ADR 0015), verify that the selected model is available on the Vertex AI `eu` multi-region endpoint.
