## Summary

-

## Agent Collaboration OS Checks

- [ ] Skill version updated when behavior changed.
- [ ] `CHANGELOG.md` updated.
- [ ] Protocol routing updated when a new reference was added.
- [ ] Runtime project files were not written into the skill repository.
- [ ] Agent-facing Markdown remains precise English.
- [ ] User-facing Markdown remains Chinese where practical.

## Tool Evidence

```text
python -m unittest discover tests
python scripts/validate_skill_repo.py
python scripts/install_skill.py --dry-run
```

## Risk And Rollback

- Risk:
- Rollback:
