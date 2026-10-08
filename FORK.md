# Demo fork

This repository is a fork of [EatWell-Studio/NutriScan-MVP](https://github.com/EatWell-Studio/NutriScan-MVP), made to prepare the demo version shown at Claude Founder House Stockholm (2026-10-14). Where this file conflicts with CONTRIBUTING.md or CLAUDE.md, this file wins inside this fork.

## Ownership

- Hannes (`hannesgao`) maintains the fork alone and owns every task in it, including the Track B tasks that mica owns upstream.
- mica (`hyhcrh`) does not take part in the fork. As an organization owner she technically has access, but she is not asked for reviews or work here.

## Process differences from upstream

- **Pull requests are still required**: `main` is protected (linear history, no force pushes, admins included), and every change lands through a PR, merged with rebase merge.
- **No approvals are required.** Reviews happen together with Claude Code in the CLI before merging. Do not request reviewers on GitHub.
- **ADRs**: the ADR workflow (CONTRIBUTING §2) still applies, with Hannes as the only person who accepts an ADR.
- **Code ownership**: CODEOWNERS lists `hannesgao` only; there are no track boundaries.
- Everything else is unchanged: commit format with `Refs:` lines, CI, secrets, toolchain and the hard rules in CLAUDE.md and the PRD.

## Issues and project board

- Issues were imported from upstream with their state and comments; each says which upstream issue it mirrors. **Issue numbers differ from upstream** (upstream #2 is #1 here, and so on).
- Project board: [NutriScan MVP — Demo Fork](https://github.com/orgs/EatWell-Studio/projects/2).
- PRs #41–#44 mirror upstream PRs #45–#48.

## Relation to upstream

- Upstream stays the canonical project. Changes that should outlive the demo go back upstream as normal PRs reviewed by mica.
- To bring upstream changes into the fork, fetch the `upstream` remote and open a PR in the fork with the changes rebased or cherry-picked onto the fork's `main` (no merge commits; linear history).
