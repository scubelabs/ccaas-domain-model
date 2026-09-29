#!/usr/bin/env python3
"""Validate published JSON Schemas and event examples."""
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
ENVELOPE = ROOT / "events" / "event-envelope.schema.json"
PAYLOADS = {
    "recording.available": "recording-available.v1.schema.json",
    "routing.agent.reserved": "routing-agent-reserved.v1.schema.json",
}

def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate(schema, instance):
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(instance)

def main():
    schemas = [ENVELOPE, *sorted(SCHEMAS.glob("*.schema.json"))]
    for path in schemas:
        Draft202012Validator.check_schema(read(path))
    envelope = read(ENVELOPE)
    examples = sorted((ROOT / "examples" / "events").glob("*.json"))
    if not examples:
        raise AssertionError("No event examples found")
    ids = set()
    for path in examples:
        event = read(path)
        validate(envelope, event)
        event_id = event["event_id"]
        if event_id in ids:
            raise AssertionError(f"Duplicate event_id: {event_id}")
        ids.add(event_id)
        kind = event["event_type"]
        if kind not in PAYLOADS:
            raise AssertionError(f"{path.name}: no payload contract for {kind}")
        if event["event_version"] != 1:
            raise AssertionError(f"{path.name}: unsupported fixture version")
        validate(read(SCHEMAS / PAYLOADS[kind]), event["data"])
        if event.get("interaction_id") != event["data"].get("interaction_id"):
            raise AssertionError(f"{path.name}: envelope/payload interaction_id mismatch")
    valid = read(examples[0])
    for label, patch in (
        ("missing event_id", lambda e: e.pop("event_id")),
        ("invalid timestamp", lambda e: e.update(occurred_at="not-a-date")),
        ("invalid version", lambda e: e.update(event_version=0)),
    ):
        changed = dict(valid)
        patch(changed)
        try:
            validate(envelope, changed)
        except ValidationError:
            continue
        raise AssertionError(f"Known-invalid envelope accepted: {label}")
    print(f"Validated {len(schemas)} schemas, {len(examples)} event examples and 3 negative cases")

if __name__ == "__main__":
    main()
