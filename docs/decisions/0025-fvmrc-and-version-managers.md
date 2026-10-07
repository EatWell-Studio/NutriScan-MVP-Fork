# ADR 0025: `.fvmrc` constraints and other version managers

- Status: Accepted (agreed in advance in chat, see "Context")
- Date: 2026-10-07
- Decision: toolchain detail of D22; refines ADR 0024 and supersedes its rule that Flutter and Dart always run through FVM

## Context

ADR 0024 makes `.fvmrc` the single source of truth for the Flutter version and tells everyone to run `fvm flutter …`. Hannes uses FVM; mica manages toolchains with [mise](https://mise.jdx.dev/), which does not read `.fvmrc` natively ([idiomatic version files](https://mise.jdx.dev/configuration.html) are off by default and do not cover Flutter). mica's local setup reads the Flutter version from `.fvmrc` through a mise template ([templates](https://mise.jdx.dev/templates.html)), which relies on two properties of the file. FVM may rewrite `.fvmrc` (for example on `fvm use`) and change its key order. mica proposed recording these constraints on 2026-10-03 while reviewing #44, and both members agreed.

## Decision

**`.fvmrc` constraints**

1. **Stable release only**: the Flutter version is a plain stable version number such as `3.47.5`, never a channel name (`stable`, `beta`, `master`) or a version with a channel or fork suffix (restates ADR 0023).
2. **`flutter` is the first key**: `"flutter"` is the first field of the JSON object, and no field before it contains the string `flutter`.

Any command that can write `.fvmrc` (`fvm use`, `fvm config`, editor integrations) is followed by a check of both constraints; if the order changed, it is restored before committing.

**Version managers**

- Each developer may use FVM or another version manager such as mise, provided the Flutter version it uses comes from `.fvmrc`. This replaces ADR 0024's rule that Flutter and Dart always run through FVM; `.fvmrc` stays the single source of truth.
- Commands are written tool-neutrally (`flutter …`). With FVM, prefix them with `fvm`. Before running checks, confirm that `flutter --version` reports the version in `.fvmrc`.
- Use only the Dart SDK bundled with that Flutter version. Do not install a separate Dart (for example through mise) that could come first on `PATH`; code generation (`dart run build_runner`) depends on the bundled version.
- Personal version-manager configuration stays out of git: `mise.local.toml` is ignored. Committing a shared `mise.toml` would be a new decision.

## Consequences

- ADR 0024 is marked as partly superseded by this ADR.
- The agent rules (CLAUDE.md) and the development setup (CONTRIBUTING §9) state the constraints, the tool-neutral commands and the version check.
- CI (P1-2) reads the Flutter version from `.fvmrc` with a JSON parser and adds a check that fails when either constraint is violated.
