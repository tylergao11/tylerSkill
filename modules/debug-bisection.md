# Debug Bisection Module

Status: Candidate

## Purpose

Shrink a broad bug hypothesis space using yes/no diagnostic probes before
attempting fixes.

## Current Implementation

- CLI: `scripts/debug_bisection.py`
- Tests: `tests/test_debug_bisection.py`
- Example: `examples/debug-bisection-reward.json`
- Protocol: `docs/references/debug-bisection.md`

## Promotion Notes

This module can become a reusable module after it is used on at least two real
debug sessions and its JSON session shape remains stable.
