<!-- Title format: <scope>: <summary> (<task-id>), e.g. app: add drift tables and append-only triggers (P1-3) -->

## Task

- Task ID:
- Closes #

## What changed

<!-- One or two sentences on the change and why it was made this way. -->

## How it was tested

<!-- Automated tests, on-device steps, airplane mode, etc. -->

## PRD rules involved

<!-- Rule numbers from PRD §8, e.g. rule 3 (append-only), rule 5 (main flow must not depend on the network). Write "none" if none apply. -->

## Screenshots

<!-- Required for UI changes; delete this section otherwise. -->

## Checklist

- [ ] After changing sources under `schema/`, codegen was rerun and `generated/` matches
- [ ] No secrets, no `secrets.json`, no photos with EXIF are committed
- [ ] Design decisions (pick one; see CONTRIBUTING §2 "ADR workflow"):
  - [ ] This is an ADR PR: docs only, status `Proposed`, changed to `Accepted` before merge
  - [ ] Implements ADR ____
  - [ ] Makes no new design decision (local choices are explained above)
  - [ ] Exception: the decision was agreed in advance; the ADR is the first, separate commit
- [ ] Does this PR **change a shared contract** (`nutrients.yaml`, VLM output schema, `models.yaml`, drift schema, provenance enum, bucket object-key rules)?
  - [ ] No
  - [ ] Yes, and this PR contains only the contract change, no feature code
- [ ] If the drift schema changed: `schemaVersion` bumped, migration and migration test added
- [ ] If PRD or DEV_PLAN changed: both the Chinese and English versions are updated
- [ ] If dependencies were added: reason and license are stated above
- [ ] Every commit has a valid prefix, a `Refs:` line with the task ID, and passes the tests on its own
