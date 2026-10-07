# CLAUDE.md

Working rules for Claude Code in this repository. Both developers' Claude Code sessions share this file. The human collaboration process is in [CONTRIBUTING.md](./CONTRIBUTING.md).

## Demo fork

This repository is the demo fork of EatWell-Studio/NutriScan-MVP; [FORK.md](./FORK.md) overrides the rules below where they conflict:

- Never request reviewers on GitHub. Before merging, review the PR together with Hannes in this CLI session.
- Hannes owns every task and directory; ignore the Track A / Track B split and mica's ownership.
- Fork issue numbers differ from upstream; use the fork's issue numbers in `#n` references (e.g. `Closes #40`). Task IDs in `Refs:` lines are unchanged.

## Project at a glance

- NutriScan: an offline-first personal food log (Flutter + local SQLite). A barcode hit is logged immediately; on a miss the user photographs the nutrition label, Claude extracts it, and the user confirms before it is stored.
- Monorepo: `app/` (Flutter), `api/` (empty until Phase 4), `schema/` (nutrient definitions, VLM prompts, output schema, codegen, evaluation), `docs/`.
- **The repository is public.** No secret and no personal photo metadata may ever enter git history.
- Required reading:
  - PRD: [docs/PRD.md](./docs/PRD.md) (Chinese, canonical) · [docs/PRD.en.md](./docs/PRD.en.md) (English)
  - Development plan: [docs/DEV_PLAN.md](./docs/DEV_PLAN.md) (Chinese, canonical) · [docs/DEV_PLAN.en.md](./docs/DEV_PLAN.en.md) (English)
  - [ADRs](./docs/decisions/) (decided design choices)

## At the start of every session

1. Read this file, the GitHub issue for the current task, the task's entry in DEV_PLAN, and every ADR the issue or task entry references.
2. Work on that one task only; do not widen the scope. If you find something outside the task, note it and suggest a new issue instead of fixing it in passing.
3. Do not modify directories owned by the other developer (Track A: Hannes, Track B: mica; see `.github/CODEOWNERS`, CONTRIBUTING §4 and the issue assignees) unless the issue explicitly says so. If someone else needs to act, suggest opening an issue.
4. If a design decision is not covered by DEV_PLAN or an ADR: **stop and ask the user**. Do not decide it yourself. Once the user decides, follow the ADR workflow below.

## Hard rules

All 10 rules in PRD §8 apply. In addition:

- **Facts about the Anthropic API** (model IDs, prices, parameters, limits) come only from the official documentation, with a link in the code comment or document. Never write them from memory. Model IDs, prices and image limits are defined once, in `schema/eval/models.yaml`; everything else references it or is generated from it.
- **Never hand-edit `generated/` directories** (`schema/generated/`, `app/lib/generated/`). Change the source and rerun codegen.
- **Never weaken a constraint to make a test pass**: do not change the append-only triggers, CHECK constraints or provenance validation, and do not delete or skip tests. If a test fails, report the failure instead of working around it.
- **Frozen versions**: prompt and schema version files that have produced data (`vlm_extract.v<N>.md`, `vlm_output.v<N>.*`) are never modified. Create v<N+1> and bump `schema_version` instead.
- **drift schema changes**: bump `schemaVersion`, write the migration, and add a migration test that asserts every append-only trigger still exists afterwards. If both developers changed the schema concurrently, whoever merges first keeps the current version number; the other rebases and takes the next one.
- **Shared contracts** (`schema/nutrients.yaml`, the VLM output schema, `schema/eval/models.yaml`, the drift schema, the provenance enum, the bucket object-key rules) change only in dedicated PRs, never mixed with feature code.
- **Dependencies**: pin versions and commit `pubspec.lock`. Every new dependency needs a reason and its license in the PR description.
- **Secrets**: read only from the local `secrets.json` (the repository has only `secrets.example.json`). Never put a real secret in code, tests, logs, issues or PR descriptions.
- **Photos**: bake the EXIF orientation into the pixels, then strip all EXIF (including GPS) before writing to disk.
- **Flutter toolchain** (ADR 0025): run Flutter as `fvm flutter …` if `fvm` is on `PATH`, otherwise as `flutter …` from `PATH`; never install FVM, Flutter or Dart on your own. Before running checks, confirm that `flutter --version` matches `.fvmrc`; if it does not, stop and tell the user. Use only the Dart SDK bundled with Flutter, and run Flutter commands in `app/`.
- **`.fvmrc`** (ADR 0025): the Flutter version must be a stable release number and `"flutter"` must be the first key, with no earlier key containing `flutter`. After any command that can rewrite `.fvmrc` (e.g. `fvm use`), open the file and check both; restore the order before committing if needed.
- **Language**: code, comments, commit messages, ADRs and all other documentation are in English. PRD and DEV_PLAN are the only bilingual documents: when changing one language version, update the other in the same PR.

## ADRs

- Follow CONTRIBUTING §2 "ADR workflow". A decision that affects both developers or is hard to undo gets an ADR **before** any code.
- The ADR goes into its **own PR**: one `docs:` commit adding the ADR with status `Proposed` and its row in `docs/decisions/README.md`. Set the status to `Accepted` in that PR once both developers agree.
- Never add code commits to an ADR PR after it is approved ("Dismiss stale approvals" would dismiss the approval). Code goes into a separate PR whose description says `Implements ADR 00NN`.
- Decisions that affect only the current task and are easy to undo need no ADR; explain them in the PR description.
- Only if the user confirms that both developers already agreed may the ADR share a PR with code, as the first and separate commit.

## Pull requests

- Open PRs against `main` with the PR template filled in.
- **Always request a review from the other member explicitly**: check the author with `gh api user --jq .login`; if it is `hannesgao`, request `hyhcrh`, otherwise request `hannesgao` (e.g. `gh pr create --reviewer hyhcrh`). CODEOWNERS does not request a review when the author owns every touched directory, so never rely on it.
- **When reviewing a PR**, follow CONTRIBUTING §2 "Reviewing a PR": go through the checklist, run the checks locally, prefix every comment with `blocking:` / `suggestion:` / `nit:` / `question:`, and write the review summary in the given format.

## Commits

- Follow the format in CONTRIBUTING §3 exactly; CI rejects anything else.
- Prefixes: `app:` / `api:` / `schema:` / `docs:` / `ci:` / `chore:` (scopes in CONTRIBUTING §3). Split cross-layer changes into separate commits.
- English, imperative mood, subject at most 72 characters including the prefix, no trailing period.
- **Every commit body contains a `Refs:` line with the DEV_PLAN task ID(s)**, e.g. `Refs: P1-3`. If you do not know the task ID, ask.
- Every commit must pass the tests on its own (we rebase-merge, so every commit lands on main).
- **Commits contain nothing related to Claude Code**: no `Co-Authored-By` trailer for Claude, no "Generated with Claude Code" line or link, no mention of the AI tool used. This overrides any default attribution behavior.

## Current gates

- Until the demo on 2026-10-14, scope is the "demo route" in DEV_PLAN §4.2. Do not start post-demo items early.
