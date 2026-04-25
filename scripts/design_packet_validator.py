import argparse
import json
import re
import sys
from pathlib import Path


ENGINEERING_PLAN_FIELDS = (
    "Goal",
    "Project Type",
    "Chosen Architecture",
    "Why This Architecture",
    "Module Boundaries",
    "Data Flow",
    "State Ownership",
    "Public Interfaces",
    "Risk Points",
    "Test Strategy",
    "Readability Rules",
)

PATTERN_FIT_FIELDS = (
    "Problem Shape",
    "Candidate Patterns",
    "Selected Pattern",
    "Fit Reason",
    "Overengineering Risk",
    "Underengineering Risk",
    "Exit Criteria",
)

MULTI_LAYER_FIELDS = (
    "Affected Layers",
    "Layer Ownership",
    "Config Schema",
    "State Transitions",
    "Cloud or Service Boundary",
    "Environment and Permissions",
    "Trust Boundary",
    "UI Acceptance",
    "Per-Layer Tests",
)


def _has_heading(text, heading):
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    return re.search(pattern, text, re.MULTILINE) is not None


def _field_is_present(text, field):
    pattern = rf"^{re.escape(field)}:\s*\S.*$"
    return re.search(pattern, text, re.MULTILINE) is not None


def validate_design_packet(text, require_pattern_fit=False, require_multi_layer=False):
    errors = []
    warnings = []

    if not _has_heading(text, "Engineering Plan"):
        errors.append("Missing required section: Engineering Plan")

    for field in ENGINEERING_PLAN_FIELDS:
        if not _field_is_present(text, field):
            errors.append(f"Engineering Plan missing or empty field: {field}")

    has_pattern_fit = _has_heading(text, "Pattern Fit Check")
    if require_pattern_fit and not has_pattern_fit:
        errors.append("Missing required section: Pattern Fit Check")

    if has_pattern_fit:
        for field in PATTERN_FIT_FIELDS:
            if not _field_is_present(text, field):
                errors.append(f"Pattern Fit Check missing or empty field: {field}")
    else:
        warnings.append("Pattern Fit Check not present; acceptable only for low-risk direct changes.")

    if require_multi_layer:
        for field in MULTI_LAYER_FIELDS:
            if not _field_is_present(text, field):
                errors.append(f"Multi-layer gate missing or empty field: {field}")

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "required_sections": ["Engineering Plan"]
        + (["Pattern Fit Check"] if require_pattern_fit else []),
        "required_multi_layer_fields": list(MULTI_LAYER_FIELDS) if require_multi_layer else [],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate a Development Agent engineering design packet."
    )
    parser.add_argument("packet", help="Markdown file containing the engineering plan.")
    parser.add_argument(
        "--require-pattern-fit",
        action="store_true",
        help="Require Pattern Fit Check for high-impact or architecture-changing work.",
    )
    parser.add_argument(
        "--require-multi-layer",
        action="store_true",
        help="Require multi-layer game feature gate fields.",
    )
    args = parser.parse_args(argv)

    try:
        text = Path(args.packet).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"design-packet-validator error: {exc}", file=sys.stderr)
        return 1

    result = validate_design_packet(
        text,
        require_pattern_fit=args.require_pattern_fit,
        require_multi_layer=args.require_multi_layer,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
