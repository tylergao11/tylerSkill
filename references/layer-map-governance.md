# Layer Map Governance

Use this protocol when Development Agent may place code in the wrong layer,
cross MVC boundaries, or scatter platform/API logic through presentation code.

## Core Rule

Simple MVC-style separation is the default for most game work:

```text
Model/Data -> Controller/System -> View/Presentation
```

Validate layer placement before treating a change as complete.

## Layer Map

```markdown
## Layer Map

Project:
Model/Data Paths:
Controller/System Paths:
View/Presentation Paths:
Service/Cloud Paths:
Config Paths:
Test Paths:
Forbidden Cross-Layer Writes:
Exceptions:
```

## Layer Placement Review

```markdown
## Layer Placement Review

Changed Files:
Expected Layers:
Detected Layers:
Violations:
Allowed Exceptions:
Required Move:
Validation:
```

Use `scripts/layer_map_validator.py` with a project-owned JSON layer map when
changed files are known.
