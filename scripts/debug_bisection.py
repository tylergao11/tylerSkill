import argparse
import copy
import json
import sys
from pathlib import Path


ACTIVE_STATUS = "active"
ELIMINATED_STATUS = "eliminated"


def active_hypothesis_ids(hypotheses):
    return [
        item["id"]
        for item in hypotheses
        if item.get("status", ACTIVE_STATUS) != ELIMINATED_STATUS
    ]


def _active_eliminations(probe, result, active_ids):
    key = "eliminates_if_yes" if result == "yes" else "eliminates_if_no"
    return sorted(set(probe.get(key, [])) & set(active_ids))


def score_probe(probe, active_ids):
    yes_eliminated = _active_eliminations(probe, "yes", active_ids)
    no_eliminated = _active_eliminations(probe, "no", active_ids)
    active_count = len(active_ids)
    yes_remaining = active_count - len(yes_eliminated)
    no_remaining = active_count - len(no_eliminated)

    return {
        "probe": probe,
        "yes_eliminated": yes_eliminated,
        "no_eliminated": no_eliminated,
        "best_case_eliminated": max(len(yes_eliminated), len(no_eliminated)),
        "worst_case_remaining": max(yes_remaining, no_remaining),
        "balance_gap": abs(yes_remaining - no_remaining),
    }


def recommend_probe(hypotheses, probes):
    active_ids = active_hypothesis_ids(hypotheses)
    if len(active_ids) < 2:
        raise ValueError("Need at least two active hypotheses to bisect.")

    scored = [score_probe(probe, active_ids) for probe in probes]
    useful = [
        item
        for item in scored
        if item["yes_eliminated"] or item["no_eliminated"]
    ]
    if not useful:
        raise ValueError("No probe eliminates any active hypothesis.")

    useful.sort(
        key=lambda item: (
            item["worst_case_remaining"],
            item["balance_gap"],
            -item["best_case_eliminated"],
            item["probe"].get("id", ""),
        )
    )
    best = useful[0]
    return {
        "active_hypotheses": active_ids,
        "probe": best["probe"],
        "yes_eliminated": best["yes_eliminated"],
        "no_eliminated": best["no_eliminated"],
        "best_case_eliminated": best["best_case_eliminated"],
        "worst_case_remaining": best["worst_case_remaining"],
        "why": "Selected probe minimizes worst-case remaining hypotheses.",
    }


def apply_probe_result(session, probe_id, result):
    if result not in {"yes", "no"}:
        raise ValueError("Probe result must be 'yes' or 'no'.")

    probes = session.get("probes", [])
    probe = next((item for item in probes if item.get("id") == probe_id), None)
    if probe is None:
        raise ValueError(f"Probe not found: {probe_id}")

    updated = copy.deepcopy(session)
    active_ids = active_hypothesis_ids(updated.get("hypotheses", []))
    eliminated = _active_eliminations(probe, result, active_ids)
    eliminated_set = set(eliminated)

    for hypothesis in updated.get("hypotheses", []):
        if hypothesis.get("id") in eliminated_set:
            hypothesis["status"] = ELIMINATED_STATUS
            hypothesis["eliminated_by"] = probe_id
            hypothesis["eliminated_result"] = result
        elif hypothesis.get("status", ACTIVE_STATUS) != ELIMINATED_STATUS:
            hypothesis["status"] = ACTIVE_STATUS

    history = updated.setdefault("diagnostic_history", [])
    history.append(
        {
            "probe_id": probe_id,
            "question": probe.get("question", ""),
            "result": result,
            "eliminated": eliminated,
            "remaining": active_hypothesis_ids(updated.get("hypotheses", [])),
        }
    )
    return updated


def _load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _write_json(data, path):
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if path == "-":
        print(text)
        return
    Path(path).write_text(text + "\n", encoding="utf-8")


def _recommend_command(args):
    session = _load_json(args.session)
    recommendation = recommend_probe(
        session.get("hypotheses", []),
        session.get("probes", []),
    )
    _write_json(recommendation, args.output)


def _apply_command(args):
    session = _load_json(args.session)
    updated = apply_probe_result(session, args.probe, args.result)
    _write_json(updated, args.output)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Recommend and apply bisection-style diagnostic probes."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    recommend = subparsers.add_parser("recommend")
    recommend.add_argument("session")
    recommend.add_argument("-o", "--output", default="-")
    recommend.set_defaults(func=_recommend_command)

    apply = subparsers.add_parser("apply")
    apply.add_argument("session")
    apply.add_argument("--probe", required=True)
    apply.add_argument("--result", choices=["yes", "no"], required=True)
    apply.add_argument("-o", "--output", default="-")
    apply.set_defaults(func=_apply_command)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"debug-bisection error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
