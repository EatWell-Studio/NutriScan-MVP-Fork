# ADR 0002: VLM model selection process and criteria

- Status: Accepted (process and criteria). The model is added to the "Results" section after the P05-5 evaluation. The candidate list is amended by [ADR 0026](./0026-sonnet-5-5-candidate.md).
- Date: 2026-09-26
- Decision: D14

## Context

Label extraction now uses Claude (PRD section 4). Models change quickly while the evaluation set stays fixed. The choice must rest on evaluation data, not impressions.

## Decision

- **Candidates**: Claude Opus 5.5, Claude Sonnet 5.
- **Dropped**: Claude Haiku 4.5 (decided 2026-09-26). It does not support the effort parameter, is limited to the standard-resolution image tier, and could retire on Vertex AI and Bedrock as early as mid-October 2026, which would block the EU route (ADR 0015).
- **Reference**: Claude Fable 5.1 runs once on the evaluation set as an accuracy ceiling. It is **not a candidate**.
- **Mistral** runs only in the evaluation script; see ADR 0003.
- **Selection criteria, in priority order**:
  1. Silent error rate: the share of fields that disagree with ground truth and were flagged by neither a validation rule nor low confidence.
  2. P90 latency ≤ 25 s.
  3. Cost. At our volume this is single-digit dollars, so it decides only when the first two criteria are tied.
- **Evaluation matrix**: Opus 5.5 and Sonnet 5 each run at effort `low` and `medium`. Fable 5.1 runs at its default effort. Every call records input and output token counts, and cost is computed from the prices in `schema/eval/models.yaml`.
- **Until results are in**, the app uses Opus 5.5, the officially recommended default starting point, at effort `low`. This is set in `app_default` in `models.yaml`.
- Model IDs, prices and image limits are defined only in `models.yaml`. This ADR gives no specific numbers.

## Known facts to weigh in the choice (verified 2026-09-26)

- Opus 5.5 always runs with thinking on. Thinking cannot be disabled, and the default effort is `medium`.
- Both candidates are in the high-resolution image tier.
- On the EU route, the Vertex AI EU multi-region offers Opus 5.5 and Sonnet 5 with structured outputs. On Bedrock, Opus 5.5 and Sonnet 5 do not support structured outputs.

## Results (filled in by P05-5)

| Configuration | ① Atwater failure rate | ② Per-field accuracy | ③ Silent error rate | P50 | P90 | Cost per call |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

- Selected model and effort:
- Confidence and validation thresholds:
- Whether "confirm all in one tap when everything passes" is enabled (based on ③):

## References

- [Models overview](https://platform.claude.com/docs/en/models/overview)
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)
- [Vision](https://platform.claude.com/docs/en/build-with-claude/vision)
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- [Claude on Vertex AI](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)
