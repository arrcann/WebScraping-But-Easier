# Starlink-Daily-Usage-WebScraper-But-Easier
Starlink WebScraper using JSON


Extracts per-day data usage from a Starlink billing JSON export and writes it to a clean CSV file.

## Requirements

- Python 3.10+
- No third-party dependencies — uses only the standard library (`json`, `csv`, `datetime`, `pathlib`)

## Usage

1. Export your Starlink billing data and save it as `starlink_data.json` in the same directory as the script.
2. Run the script:

```bash
python starlink_parser.py
```

3. A file named `starlink_daily_usage.csv` will be created in the same directory.

## Input Format

The script expects a JSON file with the following structure:

```json
{
  "content": {
    "billingCyclesAnnotated": [
      {
        "startDate": "2025-11-17T00:00:00Z",
        "dailyData": [
          [1.23],
          [4.56],
          ...
        ]
      }
    ]
  }
}
```

Each entry in `dailyData` is a single-element array containing the GB used for that day, offset from `startDate`.

## Output Format

`starlink_daily_usage.csv` contains two columns:

| Date       | Data Usage |
|------------|------------|
| 2025-11-17 | 1.23 GB    |
| 2025-11-18 | 4.56 GB    |

## Configuration

The input and output filenames are defined as constants at the top of the script:

```python
INPUT_FILE  = "starlink_data.json"
OUTPUT_FILE = "starlink_daily_usage.csv"
```

Change these to point to different paths if needed.
