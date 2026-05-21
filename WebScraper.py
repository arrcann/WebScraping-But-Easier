import json
import csv
from datetime import datetime, timedelta
from pathlib import Path


INPUT_FILE = "starlink_data.json"
OUTPUT_FILE = "starlink_daily_usage.csv"


def parse_billing_cycles(payload: dict) -> list[list]:
    """Extract daily usage rows from the nested billing cycle structure."""
    rows = []
    billing_cycles = payload.get("content", {}).get("billingCyclesAnnotated", [])

    for cycle in billing_cycles:
        start_date = datetime.strptime(
            cycle.get("startDate").split("T")[0], "%Y-%m-%d"
        )

        for index, usage_wrapper in enumerate(cycle.get("dailyData", [])):
            date_str = (start_date + timedelta(days=index)).strftime("%Y-%m-%d")
            gb_value = round(usage_wrapper[0], 2) if usage_wrapper else 0.0
            rows.append([date_str, f"{gb_value} GB"])

    return rows


def write_csv(rows: list[list], output_path: str) -> None:
    """Write extracted rows to a CSV file with labeled headers."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Data Usage"])
        writer.writerows(rows)


def main():
    payload = json.loads(Path(INPUT_FILE).read_text(encoding="utf-8"))
    rows = parse_billing_cycles(payload)
    write_csv(rows, OUTPUT_FILE)
    print(f"Done! Generated '{OUTPUT_FILE}' containing {len(rows)} tracked entries.")


if __name__ == "__main__":
    main()