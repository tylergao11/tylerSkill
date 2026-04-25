# Reusable Modules

Use this when deciding whether code should become reusable, portable, or part of a
long-term capability module.

## Core Rule

A reusable module must be useful outside the project without carrying the project
with it.

Build project code first. Promote reusable weapons only after repeated need and
clean boundaries are proven.

## Reuse Layers

```text
Agent OS Workflow -> Game Architecture Profile -> Reusable Capability Modules -> Optional Game Template
```

Agent OS is not a fixed game template. It selects profiles and modules.

## Module Levels

- **Project Code**: only serves the current project.
- **Reusable Module Candidate**: likely useful elsewhere, but not proven.
- **Reusable Module**: independently useful, tested, documented, and portable.
- **Core Toolkit**: validated across multiple projects.

Do not default everything into reusable infrastructure.

## Candidate Criteria

A module may become a candidate only if:

- The problem appears likely to repeat across features or projects.
- Inputs and outputs are clear.
- It does not depend on current project globals.
- It does not bind to specific UI, art, text, or one-off business rules.
- It can be tested alone.

Good candidates:

- Debug bisection
- Preflight debug capture
- Config validation
- Asset manifest checks
- Cloud function boundary wrappers
- Reward trace logging
- Numeric simulation
- State machine utilities

Poor early candidates:

- One game's exact combat logic
- One event page
- One reward copywriting table
- One-off UI popup implementation

## Module Contract

```markdown
## Module Contract

Name:
Purpose:
Reusable Level: Project Code | Candidate | Reusable Module | Core Toolkit
Problem It Solves:
Inputs:
Outputs:
Dependencies:
Does Not Own:
Extension Points:
Failure Modes:
Test Strategy:
Portability Notes:
```

`Does Not Own` is required. Reusable modules should have sharp boundaries.

## Port and Adapter Boundary

Use a simple boundary:

- **Core**: pure or mostly pure logic.
- **Port**: small interface for external capability.
- **Adapter**: current project/platform implementation.

Keep ports small. Do not create generic frameworks unless repeated use proves
they are needed.

## Anti-Coupling Review

```markdown
## Anti-Coupling Review

Module:
Project-Specific Dependencies:
Hidden Globals:
Platform Locks:
UI/Art Coupling:
Config Coupling:
Can Be Tested Alone: Yes | No
Required Decoupling:
```

## Module Promotion Review

```markdown
## Module Promotion Review

Module:
From:
To:
Reuse Evidence:
API Stability:
Known Limitations:
Migration Cost:
Decision:
```

Promotion path:

```text
Project Code -> Candidate -> Reusable Module -> Core Toolkit
```

Promotion should be earned by repeated need, not imagined future use.

## Minimum Weapon Standard

A reusable module should include:

- Module Contract
- Small public API
- Example usage
- Tests
- Failure modes
- Portability notes

If adding those feels too heavy, the code is probably still Project Code or a
Candidate, not a Reusable Module.
