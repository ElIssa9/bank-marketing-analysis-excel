"""Independently reproduce the Excel campaign summaries using the standard library.

Run from the project root: python3 src/validate_data.py
This script validates and summarizes CSV data; Excel remains the analysis workbook.
"""

import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/raw/bank-additional-full.csv"
RESULTS = ROOT / "results"
EXPECTED_HEADER = [
    "age", "job", "marital", "education", "default", "housing", "loan",
    "contact", "month", "day_of_week", "duration", "campaign", "pdays",
    "previous", "poutcome", "emp.var.rate", "cons.price.idx", "cons.conf.idx",
    "euribor3m", "nr.employed", "y",
]
NUMERIC = ["age", "duration", "campaign", "pdays", "previous",
           "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]


def age_band(age):
    if age < 30:
        return "Under 30"
    if age < 40:
        return "30-39"
    if age < 50:
        return "40-49"
    if age < 60:
        return "50-59"
    return "60+"


def contact_band(contacts):
    if contacts == 1:
        return "1 contact"
    if contacts <= 3:
        return "2-3 contacts"
    if contacts <= 5:
        return "4-5 contacts"
    return "6+ contacts"


def main():
    with SOURCE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        assert reader.fieldnames == EXPECTED_HEADER, "Unexpected source schema"
        rows = list(reader)

    assert len(rows) == 41188, "Unexpected number of original records"
    for i, row in enumerate(rows, 2):
        assert None not in row, f"Unexpected extra CSV fields on line {i}"
        assert all(v is not None and v != "" for v in row.values()), f"Empty value on line {i}"
        assert row["y"] in {"yes", "no"}, f"Unknown outcome on line {i}"
        for field in NUMERIC:
            float(row[field])
        assert 0 < int(row["age"]) < 120
        assert int(row["duration"]) >= 0
        assert int(row["campaign"]) >= 1
        assert int(row["previous"]) >= 0
        assert int(row["pdays"]) >= 0

    subscriptions = sum(row["y"] == "yes" for row in rows)
    assert subscriptions == 4640, "Unexpected original outcome total"
    excess_repeats = len(rows) - len({tuple(row[k] for k in EXPECTED_HEADER) for row in rows})
    assert excess_repeats == 12, "Unexpected repeated-row count"

    grouped = {key: defaultdict(lambda: [0, 0]) for key in
               ["job", "y", "age_band", "education", "contact", "month",
                "day_of_week", "contact_band", "poutcome", "housing"]}
    for row in rows:
        prepared = dict(row)
        prepared["age_band"] = age_band(int(row["age"]))
        prepared["contact_band"] = contact_band(int(row["campaign"]))
        for key, groups in grouped.items():
            group = groups[prepared[key]]
            group[0] += 1
            group[1] += row["y"] == "yes"

    metrics = []
    for key, groups in grouped.items():
        assert sum(v[0] for v in groups.values()) == len(rows)
        assert sum(v[1] for v in groups.values()) == subscriptions
        for group, (count, subscribed) in sorted(groups.items()):
            metrics.append({"dimension": key, "group": group, "records": count,
                            "subscriptions": subscribed, "subscription_rate": subscribed / count})

    # Check band boundaries independently of this particular sample.
    assert [age_band(x) for x in [29, 30, 39, 40, 49, 50, 59, 60]] == [
        "Under 30", "30-39", "30-39", "40-49", "40-49", "50-59", "50-59", "60+"]
    assert [contact_band(x) for x in [1, 2, 3, 4, 5, 6]] == [
        "1 contact", "2-3 contacts", "2-3 contacts", "4-5 contacts", "4-5 contacts", "6+ contacts"]

    summary = {
        "source_file": str(SOURCE.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "source_columns": len(EXPECTED_HEADER),
        "records": len(rows), "subscriptions": subscriptions,
        "non_subscriptions": len(rows) - subscriptions,
        "subscription_rate": subscriptions / len(rows),
        "average_campaign_contacts": sum(int(r["campaign"]) for r in rows) / len(rows),
        "excess_exact_repeated_rows_retained": excess_repeats,
        "unknown_values_by_field": {k: sum(r[k] == "unknown" for r in rows)
                                    for k in EXPECTED_HEADER if any(r[k] == "unknown" for r in rows)},
        "pdays_999_records": sum(r["pdays"] == "999" for r in rows),
        "missing_values": sum(v is None or v == "" for r in rows for v in r.values()),
        "observed_months": sorted({r["month"] for r in rows}),
        "age_minimum": min(int(r["age"]) for r in rows),
        "age_maximum": max(int(r["age"]) for r in rows),
        "grouped_dimensions_reconciled": len(grouped),
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "validation_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    with (RESULTS / "group_metrics.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(metrics[0]))
        writer.writeheader()
        writer.writerows(metrics)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
