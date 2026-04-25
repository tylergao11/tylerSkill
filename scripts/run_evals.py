import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class EvalRunResult:
    checked: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def _output_defined(protocol_text, output):
    pattern = rf"^#+\s+{re.escape(output)}\s*$"
    return re.search(pattern, protocol_text, re.MULTILINE) is not None or output in protocol_text


def run_evals(repo):
    repo = Path(repo).resolve()
    result = EvalRunResult()
    eval_dir = repo / "evals"
    if not eval_dir.exists():
        result.errors.append("Missing evals directory")
        return result

    for eval_file in sorted(eval_dir.glob("*.json")):
        relative_eval = eval_file.relative_to(repo).as_posix()
        result.checked.append(relative_eval)
        try:
            scenario = json.loads(eval_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            result.errors.append(f"{relative_eval}: invalid JSON: {exc}")
            continue

        for key in ("name", "prompt", "expected_protocols", "expected_outputs", "must_not"):
            if key not in scenario:
                result.errors.append(f"{relative_eval}: missing key {key}")

        protocol_text = ""
        for protocol in scenario.get("expected_protocols", []):
            protocol_path = repo / "references" / protocol
            result.checked.append(f"{relative_eval}:{protocol}")
            if not protocol_path.exists():
                result.errors.append(f"{relative_eval}: missing protocol {protocol}")
                continue
            protocol_text += "\n" + protocol_path.read_text(encoding="utf-8")

        for output in scenario.get("expected_outputs", []):
            result.checked.append(f"{relative_eval}:{output}")
            if not _output_defined(protocol_text, output):
                result.errors.append(f"{relative_eval}: undefined expected output {output}")

        for forbidden in scenario.get("must_not", []):
            if not isinstance(forbidden, str) or not forbidden.strip():
                result.errors.append(f"{relative_eval}: empty must_not item")

    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run Agent Collaboration OS eval scenario checks.")
    parser.add_argument("--repo", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)

    result = run_evals(Path(args.repo))
    print(json.dumps(
        {
            "ok": not result.errors,
            "checked": len(result.checked),
            "errors": result.errors,
        },
        ensure_ascii=False,
        indent=2,
    ))
    return 0 if not result.errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
