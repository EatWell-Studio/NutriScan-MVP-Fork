# ADR 0024: Flutter version management with FVM

- Status: Accepted; the rule that Flutter and Dart always run through FVM is superseded by [ADR 0025](./0025-fvmrc-and-version-managers.md)
- Date: 2026-09-27
- Decision: toolchain detail of D22 (ADR 0023)

## Context

ADR 0023 pins Flutter 3.47.5 but leaves open where the pin lives. Both developers work on their own machines, and CI (P1-2) must use exactly the same Flutter version.

## Decision

- Flutter is managed with [FVM](https://fvm.app/). `.fvmrc` at the repository root pins the Flutter version (3.47.5) and is the single source of truth for it.
- Run Flutter and Dart through FVM: `fvm flutter …`, `fvm dart …`. The `.fvm/` directory (a local link to the SDK) is not committed.
- CI (P1-2) reads the Flutter version from `.fvmrc` instead of repeating it in the workflow.
- The Android toolchain is not pinned by FVM. Local builds use JDK 17 and the Android SDK command-line tools; the Android Gradle plugin downloads the SDK platforms it needs.
- A Flutter upgrade is a dedicated PR that changes `.fvmrc` and anything the upgrade requires, nothing else.

## Consequences

- Each developer installs FVM once, then runs `fvm install` in the repository (setup in CONTRIBUTING §9).
- This refines ADR 0023: for Flutter, the "one place" is `.fvmrc`; Dart follows from the Flutter version.
