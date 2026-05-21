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

## Getting the JSON File

The input file is captured directly from the Starlink account portal using your browser's developer tools.

1. Navigate to the **Subscription** section of your [Starlink account portal](https://www.starlink.com/account).

2. Right-click anywhere on the page and select **Inspect**.

3. Click the **Network** tab in the Developer Tools panel, then select the **Fetch/XHR** filter.

4. Refresh the page, then look through the listed requests for one containing the `annotated` data structure. Click it and open the **Response** tab — copy the entire text.

5. In your project folder, create a new file named `starlink_data.json` and paste the copied response into it.

Each entry in `dailyData` is a single-element array containing the GB used for that day, offset from `startDate`.

## Output Format

`starlink_daily_usage.csv` contains two columns:

| Date       | Data Usage |
|------------|------------|
| 2026-06-17 | 0.00 GB    |
| 2026-06-18 | 0.00 GB    |

## Configuration

The input and output filenames are defined as constants at the top of the script:

```python
INPUT_FILE  = "starlink_data.json"
OUTPUT_FILE = "starlink_daily_usage.csv"
```

Change these to point to different paths if needed.
