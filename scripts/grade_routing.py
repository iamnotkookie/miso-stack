#!/usr/bin/env python3
"""Grade a routing evaluation trace against the labels withheld from the prompt."""
import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = {"routing": {"workflow": "expected_workflow"}, "capability-routing": {"skill": "skill", "mode": "mode"}}


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)


def arrays_in(text):
    decoder = json.JSONDecoder()
    index = text.find("[")
    while index != -1:
        try:
            value, end = decoder.raw_decode(text, index)
        except ValueError:
            index = text.find("[", index + 1)
            continue
        if isinstance(value, list) and value and all(isinstance(row, dict) and "id" in row for row in value):
            yield value
        index = text.find("[", end)


def last_answer(trace):
    """Host traces differ, so take the last array of id-bearing objects in any string of any event."""
    answer = None
    for line in Path(trace).read_text().splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        for text in strings(event):
            for found in arrays_in(text):
                answer = found
    if answer is None:
        raise ValueError("No routing answer found in the trace.")
    return answer


def grade(case, trace):
    if "evals/" in Path(trace).read_text():
        raise ValueError("The trace mentions evals/, so the agent could have read the labels. The grade is invalid.")
    fields = FIELDS[case]
    expected = json.loads((ROOT / "evals" / (case + ".json")).read_text())["cases"]
    answers = {str(row["id"]): row for row in last_answer(trace)}
    misses = []
    for row in expected:
        answer = answers.get(str(row["id"]), {})
        for field, label in fields.items():
            if answer.get(field) != row[label]:
                misses.append({"id": row["id"], "field": field, "expected": row[label], "actual": answer.get(field)})
    return {"case": case, "total": len(expected), "correct": len(expected) - len({miss["id"] for miss in misses}),
            "misses": misses}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Grade a routing trace. Exit 1 when any case is misrouted.")
    parser.add_argument("--case", choices=sorted(FIELDS), required=True)
    parser.add_argument("trace", help="stdout.jsonl from run_evaluation.py")
    args = parser.parse_args()
    try:
        result = grade(args.case, args.trace)
    except (OSError, ValueError) as error:
        parser.exit(2, str(error) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result["misses"] else 0)
