import argparse
import json
import sys
from pathlib import Path


def _normalize(path):
    return path.replace("\\", "/").strip("/")


def _matches(path, prefixes):
    normalized = _normalize(path)
    return [prefix for prefix in prefixes if normalized.startswith(_normalize(prefix))]


def classify_path(path, layers):
    matches = []
    for layer, prefixes in layers.items():
        if _matches(path, prefixes):
            matches.append(layer)
    return matches or ["unknown"]


def validate_layer_map(config, changed_files):
    layers = config.get("layers", {})
    forbidden = config.get("forbidden", [])
    files = [_normalize(item) for item in changed_files]
    classified = {file_path: classify_path(file_path, layers) for file_path in files}
    violations = []

    for rule in forbidden:
        source = rule.get("source")
        target = rule.get("target")
        source_paths = [
            file_path for file_path, file_layers in classified.items() if source in file_layers
        ]
        target_paths = [
            file_path for file_path, file_layers in classified.items() if target in file_layers
        ]
        if source_paths and target_paths:
            violations.append(
                {
                    "rule": f"{source} must not change with {target}",
                    "source_files": source_paths,
                    "target_files": target_paths,
                    "reason": rule.get("reason", ""),
                }
            )

    unknown = [file_path for file_path, file_layers in classified.items() if file_layers == ["unknown"]]
    return {
        "ok": not violations and not unknown,
        "classified": classified,
        "violations": violations,
        "unknown": unknown,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate changed files against a project layer map.")
    parser.add_argument("config", help="Layer map JSON file.")
    parser.add_argument("files", nargs="*", help="Changed files. If omitted, read paths from stdin.")
    args = parser.parse_args(argv)

    try:
        config = json.loads(Path(args.config).read_text(encoding="utf-8"))
        files = args.files or [line.strip() for line in sys.stdin if line.strip()]
        result = validate_layer_map(config, files)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"layer-map-validator error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
