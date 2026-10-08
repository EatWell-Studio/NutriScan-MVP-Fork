# Architecture Decision Records (ADRs)

One record per decided design question. Numbers increase and are never reused. When a decision changes, write a new ADR and set the old one's status to "Superseded by ADR NNNN". Do not rewrite an old ADR's decision. Two exceptions: sections marked "to be filled in" (test and evaluation results), and ADRs whose introducing PR has not been merged yet, which may still be edited in place.

Open an ADR PR before writing code for any new design decision, and start coding only after both developers agree. When an ADR is needed, when it may share a PR with code, and the exact steps are in [CONTRIBUTING §2 "ADR workflow"](../../CONTRIBUTING.md#adr-workflow).

**Status flow**: an ADR is added as `Proposed` in its own PR and changed to `Accepted` in the same PR once both developers agree, right before merging. A later decision that replaces it sets its status to `Superseded by ADR NNNN`.

## Index

| ADR | Decision | Status |
| --- | --- | --- |
| [0001](./0001-object-storage-b2.md) | D3 Object storage on Backblaze B2 (EU) | Accepted, pending P0-6 tests |
| [0002](./0002-vlm-model-selection.md) | D14 VLM model selection process and criteria | Accepted (process); model pending evaluation |
| [0003](./0003-mistral-eval-only.md) | D15 Mistral only in the evaluation script | Accepted |
| [0004](./0004-ui-language.md) | D2 UI language: Chinese + English | Accepted |
| [0005](./0005-nutrient-key-naming.md) | D4 Internal nutrient key naming | Accepted |
| [0006](./0006-off-hit-rate-threshold.md) | D5 OFF hit-rate thresholds and sample size | Accepted |
| [0007](./0007-no-usda-in-mvp.md) | D6 No USDA data bundled in the MVP | Accepted |
| [0008](./0008-odbl-review-before-release.md) | D7 ODbL review before release | Accepted |
| [0009](./0009-pending-extraction-entries.md) | D8 Log offline misses first (data model) | Accepted |
| [0010](./0010-provenance-manual.md) | D9 Add `manual` to provenance | Accepted |
| [0011](./0011-photo-original-and-derived.md) | D10 Keep original and derived images, strip EXIF | Accepted |
| [0012](./0012-bucket-object-layout.md) | D11 Bucket object layout | Accepted |
| [0013](./0013-riverpod-drift.md) | D12 Riverpod + drift | Accepted |
| [0014](./0014-secrets-and-api-keys.md) | D13 Secrets and API key management | Accepted |
| [0015](./0015-server-proxy-milestone.md) | D17 Server-side proxy milestone | Accepted |
| [0016](./0016-app-id.md) | D1 App name and package name | Accepted |
| [0017](./0017-code-ownership.md) | D18 Code ownership | Accepted |
| [0018](./0018-collaborator-is-second-user.md) | D19 The collaborator counts as the second real user | Accepted |
| [0019](./0019-android-first-demo.md) | D20 Android-first demo, iOS afterwards | Accepted |
| [0020](./0020-claude-access.md) | D21 How we use Claude: subscriptions for development, API later | Accepted; API question resolved by 0022 |
| [0021](./0021-mit-license-for-mvp.md) | D16 MIT license for the MVP phase | Accepted |
| [0022](./0022-prepaid-api-before-demo.md) | D21 Prepaid API access before the demo (resolves the open question in 0020) | Accepted |
| [0023](./0023-ci-architecture.md) | D22 CI architecture and commit conventions | Accepted |
| [0024](./0024-flutter-version-via-fvm.md) | Flutter version management with FVM (refines 0023) | Accepted; partly superseded by 0025 |
| [0025](./0025-fvmrc-and-version-managers.md) | `.fvmrc` constraints and other version managers (refines 0024) | Accepted |
| [0026](./0026-sonnet-5-5-candidate.md) | D14 Sonnet 5.5 replaces Sonnet 5 as an evaluation candidate (amends 0002) | Accepted |

## Template

```markdown
# ADR NNNN: Title

- Status: Proposed / Accepted / Superseded by ADR NNNN
- Date: YYYY-MM-DD
- Decision: Dn

## Context
## Decision
## Consequences
## References
```
