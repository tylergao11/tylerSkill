# Compatibility and Registry

Use this protocol when publishing, installing, vendoring, or evaluating this
skill across agent platforms or project repositories.

## Core Rule

This repository is the canonical source for Agent Collaboration OS. Consumer
projects may install, vendor, or submodule it, but they must not fork runtime
state back into the skill path.

## Compatibility Levels

```text
supported: expected to work as-is.
portable-reference: concepts and files can be reused with small adaptation.
partial-reference: useful as guidance, but tools or triggers may not run.
reference-only: read for process design; do not assume automation support.
```

Current compatibility is recorded in `skill-manifest.json`.

## Registry Record

```markdown
## Skill Registry Record

Name:
Version:
Source:
Install Mode: Codex Skill | Vendor | Submodule | Reference Only
Compatibility:
Stability: Experimental | Tested | Production Ready | Deprecated
Consumer Project:
Pinned Commit or Tag:
Loaded Protocols:
Enabled Tools:
Known Gaps:
```

## Adoption Filter

When borrowing ideas from external GitHub skills or tools, adopt only items that
meet at least one condition:

- They create enforceable gates.
- They reduce repeated agent mistakes.
- They improve context isolation.
- They provide deterministic tooling.
- They improve portability or version tracking.

Reject items that only add vocabulary, ceremony, platform lock-in, or duplicate
existing protocols.
