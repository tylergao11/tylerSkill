# Regression and Iteration Control

Use this when revisions loop, art/dev disagree repeatedly, or a change may break
nearby systems.

## Iteration Control

No infinite polish loops.

Every revision must change either the artifact, the acceptance criteria, or the
decision owner.

### Revision Budget

```markdown
## Revision Budget

Target:
Budget:
Current Round:
Revision Type: Minor | Major | Direction Change
Owner:
Acceptance Criteria:
Escalate When:
```

### Revision Classification

```markdown
## Revision Classification

Issue:
Type: Defect Fix | Polish | Direction Change
Blocks Acceptance: Yes | No
Reason:
```

### Revision Delta

```markdown
## Revision Delta

Target:
Previous Issue:
Change Made:
Expected Effect:
Verification:
```

### Acceptance Lock

```markdown
## Acceptance Lock

Target:
Accepted Version:
Accepted By:
Acceptance Criteria Met:
Known Imperfections:
Future Polish:
```

## Regression Control

No change is local until its impact boundary is proven.

### Impact Scope

```markdown
## Impact Scope

Change:
Touched Areas:
Expected Affected Systems:
Expected Unaffected Systems:
Shared Dependencies:
Risk Level: Low | Medium | High
Regression Hotspots:
Required Regression Checks:
```

Shared system changes are at least Medium Risk. Payment, save data, reward,
auth, cloud function, leaderboard, ad reward, gacha/drop probability, core combat,
resource loading, and scene lifecycle changes are High Risk unless proven
otherwise.

### Regression Check Plan

```markdown
## Regression Check Plan

Change:
Risk Level:
Must Re-test:
Sample Re-test:
Can Skip:
Reason:
Required Evidence:
```

### Change Summary

```markdown
## Change Summary

Task ID:
Files or Systems Changed:
Behavior Changed:
Behavior Intentionally Unchanged:
Risk Areas:
Backward Compatibility:
Validation Performed:
Regression Checks Needed:
```

### Regression Incident Review

```markdown
## Regression Incident Review

Incident:
Original Change:
Broken System:
Why Impact Was Missed:
Missing Test:
Missing Dependency Map:
Process Fix:
Code Fix:
Prevention:
```
