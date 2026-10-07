# Contributing

> **This is the demo fork.** [FORK.md](./FORK.md) overrides this file where they conflict: one maintainer, no required approvals, reviews done in the Claude Code CLI.

Two developers, a public repository, one monorepo. This file covers the human collaboration process; the rules for Claude Code are in [CLAUDE.md](./CLAUDE.md). If the two conflict, this file wins and CLAUDE.md must be fixed promptly.

Members: `hannesgao` (Hannes) and `hyhcrh` (mica). **External code contributions are not accepted during the MVP phase** (ADR 0021); issues are welcome.

## 1. Task tracking

- [DEV_PLAN](./docs/DEV_PLAN.en.md) contains the plan only, **never progress**. Progress lives in GitHub Issues / Projects, so the two of us never edit DEV_PLAN concurrently.
- Every task in DEV_PLAN has one issue whose title starts with the task ID (e.g. `P1-3 drift tables and triggers`), assigned to its owner.
- Assign the issue to yourself before you start, so we never work on the same thing.
- Changes to the plan itself (new tasks, dependencies, owners) go in a separate `docs:` PR against DEV_PLAN.

## 2. Branches and PRs

- `main` is protected; every change is merged through a PR.
- One task = one branch = one PR. Branch name: `<task-id>-<short-description>`, all lowercase, e.g. `p1-3-drift-tables`.
- PR title: `<scope>: <summary> (<task-id>)`, e.g. `app: add drift tables and append-only triggers (P1-3)`. The description contains `Closes #<issue>`.
- Fill in the [PR template](./.github/pull_request_template.md).
- **Request the other member as reviewer explicitly** when opening a PR (e.g. `gh pr create --reviewer <other>`). CODEOWNERS does not request anyone when the author owns every touched directory.
- Keep PRs small and complete. Anything found outside the task's scope becomes a new issue, not a drive-by change.
- **Changes to shared contracts get their own PR**, never mixed with feature code. Shared contracts are: `schema/nutrients.yaml`, the VLM output schema, `schema/eval/models.yaml`, the drift schema, the provenance enum, and the bucket object-key rules.
- **New design decisions start as an ADR PR** (`docs/decisions/`); code follows only after both of us approve. See [ADR workflow](#adr-workflow) below; the ADR format is in [docs/decisions/README.md](./docs/decisions/README.md).
- Merge method: **rebase merge only** (commits split by layer land on main as they are). Squash merges and merge commits are disabled.
- PRD and DEV_PLAN exist in Chinese (canonical) and English. A PR that changes one version must update the other. All other documentation is English only.

### ADR workflow

**When an ADR is needed**

| Situation | Examples | What to do |
| --- | --- | --- |
| Affects both of us, or is hard to undo | Shared contracts, data structures, architecture, toolchain, external services, licensing, privacy | ADR PR first, then code |
| Affects only the current task and is easy to undo | How to split a function, how to structure a widget | No ADR; explain the reasoning in the code PR description |
| Both of us already agreed in a meeting or chat | Setting up FVM (ADR 0024) | ADR may share the PR with the code, as the **first, separate commit**; the PR description says it was agreed in advance |

When unsure, treat it as needing an ADR PR: a small extra PR costs less than rework.

**Steps**

1. **ADR PR**: a single `docs:` commit that adds the ADR with status `Proposed` and its row in the ADR index. Title: `docs: propose ADR 00NN <topic> (<task-id>)`; the commit body carries `Refs:` with the task that raised the decision.
2. Discuss in the PR comments and revise until both of us agree. Before merging, change the status to `Accepted`, approve and merge.
3. **Code PR**: a separate PR on the task branch whose description says `Implements ADR 00NN`. Its review is about the implementation, not the decision.

Do not add code commits to an ADR PR after it has been approved: "Dismiss stale approvals" is on, so any new commit dismisses the approval, and the decision could not land on `main` on its own. While an ADR PR is open, the author may prototype locally or in a draft PR, but does not request a merge.

### Branch protection for main

Configure in the GitHub repository settings (owner: DEV_PLAN task G-2):

| Setting | Value |
| --- | --- |
| Require a pull request before merging | On |
| Required approvals | 1 (with two people, this means the other person approves every PR) |
| Dismiss stale approvals when new commits are pushed | On |
| Require status checks to pass | On: `fvmrc`, `commits`, `secrets`, `flutter` (the jobs of `.github/workflows/ci.yml`, ADR 0023) |
| Require branches to be up to date before merging | On |
| Require linear history | On |
| Do not allow bypassing the above settings | On (admins cannot bypass either) |
| Require review from Code Owners | **Off**, see below |
| Repository merge button | "Allow rebase merging" only |
| Always suggest updating pull request branches | On (the "Update branch" button on a PR; choose "Update with rebase") |
| Automatically delete head branches | On |

About CODEOWNERS: [CODEOWNERS](./.github/CODEOWNERS) is used to request reviewers automatically. "Require review from Code Owners" stays off because GitHub does not let authors approve their own PRs: when the PR author is the only owner of a directory (e.g. an owner changing their own `app/` subdirectory), the PR could never be merged. In a two-person team, "at least 1 approval" already guarantees that the other person reviews.

## 3. Commits

Format (ADR 0023):

```
<prefix>: <summary in imperative mood>

<optional body>

Refs: <task-id>[, <task-id> …]
```

- **Prefixes** (lowercase, exactly one per commit):

  | Prefix | Scope |
  | --- | --- |
  | `app:` | Flutter client (`app/`) |
  | `api:` | Batch processing layer (`api/`) |
  | `schema:` | `schema/`: nutrient definitions, prompts, output schemas, codegen, evaluation |
  | `docs:` | Documentation: PRD, DEV_PLAN, ADRs, README, CONTRIBUTING, agent rules, `LICENSE` |
  | `ci:` | CI workflows, PR template, CODEOWNERS and other files under `.github/` |
  | `chore:` | Repository-level housekeeping not covered above, e.g. `.gitignore`, editor configuration |

- One commit touches one layer; split cross-layer changes into several commits.
- Subject line: English, imperative mood, no trailing period, at most 72 characters including the prefix.
- **The body must contain a `Refs:` line with the DEV_PLAN task ID(s)**, e.g. `Refs: P1-3` or `Refs: C-1, C-2`.
- Every commit passes the tests on its own (rebase merge puts every commit on main).
- No tool attribution in commit messages: no `Co-Authored-By` trailer for AI tools, no "Generated with …" lines.
- CI checks the prefix, the subject length and the `Refs:` line of every commit in a PR.

## 4. Directory ownership

[CODEOWNERS](./.github/CODEOWNERS) is authoritative; the split is explained in DEV_PLAN §4.3.

- **Track A (Hannes)**: `app/lib/domain/`, `app/lib/data/clients/vlm/`, `app/lib/features/confirm/`.
- **Track B (mica)**: `app/lib/features/scan/`, `capture/`, `portion/`, `summary/`; `app/lib/data/repositories/`, `app/lib/data/clients/off/`, `app/lib/data/clients/bucket/`, `app/lib/data/upload/`.
- **Shared contracts**: Hannes drafts, mica reviews. `schema/` and `app/lib/data/db/` are owned by both.
- **Owned by both**: everything else, including `docs/decisions/`, `CLAUDE.md`, `CONTRIBUTING.md`, `.github/`.
- Changing a directory owned by the other person requires either an explicit note in the issue or prior agreement.

## 5. Shared contracts and the drift schema

- Every drift schema change: bump `schemaVersion`, write the migration, add a migration test (including an assertion that the append-only triggers still exist after migrating).
- If both of us changed the schema concurrently, whoever merges first keeps the current version number; the other rebases, takes the next number and regenerates the migration.
- Prompt / schema version files that have produced data are frozen; any change creates a new version.

## 6. Secrets and privacy

The repository is public.

- Local secrets live in each developer's own `secrets.json` (ignored via `.gitignore`); the repository contains only `secrets.example.json`.
- Each developer has their own Anthropic API key and their own write-only B2 key, so each can be revoked independently.
- Secrets are shared only through a password manager and must **never** appear in issues, PRs, commits, logs or chat.
- CI scans for secrets with gitleaks. If a secret ever reaches git history, **revoke it immediately**; rewriting history is not a substitute for revocation.
- Strip EXIF from evaluation photos before committing them, and check that the image shows nothing personal.

## 7. Dependencies

- Pin versions and commit `pubspec.lock` (same for Python lock files).
- State the reason and license of every new dependency in the PR description. Licenses must be compatible with the project's MIT license (ADR 0021); copyleft licenses (GPL family) need an explicit decision first.

## 8. Collaboration rhythm

- **Reviews**: review and merge as quickly as practical, ideally within 24 hours of a PR being opened. This is a guideline, not a hard deadline: review when you have time. With the 9-hour time difference, a 24-hour window lets each of us review during our own day.
- **Shared contract PRs first**: Hannes drafts the shared contracts (data structures first) and mica reviews them. Contract PRs get review priority because they are on the critical path.
- **Progress sync**: one or two Google Meet calls every weekend.
- **New decisions**: open an ADR PR first; code follows only after both of us approve it (see [ADR workflow](#adr-workflow)).

## 9. Development setup

Toolchain versions follow ADR 0023. `.fvmrc` is the single source of truth for the Flutter version (ADR 0024); any version manager that takes its Flutter version from `.fvmrc` may be used (ADR 0025).

1. **Flutter**, with either:
   - [FVM](https://fvm.app/): install it (to `~/fvm/bin`, no sudo), add it to `PATH`, then run `fvm install` in the repository root; or
   - another version manager such as [mise](https://mise.jdx.dev/), configured to read the version from `.fvmrc`. Keep that configuration out of git (`mise.local.toml` is ignored).

   Check that `flutter --version` reports the version in `.fvmrc`. Use only the Dart SDK bundled with Flutter; do not install a separate Dart that could come first on `PATH`.
2. **`.fvmrc` constraints** (ADR 0025): a stable release number, and `"flutter"` as the first key. Check both after any command that rewrites the file, such as `fvm use`.
3. **Android**: install JDK 17 and the Android SDK command-line tools, set `JAVA_HOME` and `ANDROID_HOME`, and accept the SDK licenses (`sdkmanager --licenses`). The first Android build downloads the SDK platforms it needs.
4. **Secrets**: copy `secrets.example.json` to `secrets.json` (ignored by git) and fill in your values; `CONTRIBUTOR` is your GitHub username. Real values come from the password manager.

Common commands, run in `app/` (with FVM, prefix each with `fvm`):

| Purpose | Command |
| --- | --- |
| Install dependencies | `flutter pub get` |
| Regenerate localizations | `flutter gen-l10n` |
| Static analysis | `flutter analyze` |
| Tests | `flutter test` |
| Debug build (Android) | `flutter build apk --debug` |
| Run with secrets | `flutter run --dart-define-from-file=../secrets.json` |

UI strings go into both `app/lib/l10n/app_en.arb` and `app/lib/l10n/app_zh.arb` (ADR 0004); the generated files under `app/lib/generated/l10n/` are committed and never edited by hand.
