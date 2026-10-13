# Duplicate Record Check — Data Analytics

## Objective
Identify exact duplicate rows in a retail-sales sample, document them, and save a cleaned copy.

## Tools
- Python
- Pandas
- CSV files (Excel-compatible)

## Dataset
`sample_retail_sales.csv` is a small **synthetic demo dataset** created for this project. It contains 8 rows, including intentional exact duplicate rows.

## Files
- `sample_retail_sales.csv` — original demo dataset
- `duplicate_check.py` — repeatable Python script
- `duplicate_report.csv` — rows belonging to duplicate groups
- `cleaned_retail_sales.csv` — cleaned copy with exact duplicate rows removed
- `audit_note.txt` — method and row-count summary

## How to run
1. Install Python and Pandas (`pip install pandas`).
2. Keep the script and CSV in the same folder.
3. Run `python duplicate_check.py`.

The script creates/overwrites the report, cleaned copy, and audit note.

## Method
- `df.duplicated(keep=False)` marks every row that belongs to an exact duplicate group.
- `df.drop_duplicates()` keeps the first occurrence and removes additional exact copies.

## Important limitation
This example detects **exact full-row duplicates**. It does not automatically treat matching Order_IDs with different details as duplicates. In a real business dataset, investigate the business rules before deleting records.

## Result for the included demo data
- Original rows: 8
- Rows in duplicate groups: 4
- Extra duplicate rows removed: 2
- Rows in cleaned copy: 6

## Interview questions
**What is a duplicate row?**  
A row that repeats another record according to the selected matching rule.

**How can duplicates affect totals?**  
Repeated transactions can inflate sales, quantities, and counts, causing incorrect reports and decisions.

## Audit note
Always record the input file, detection rule, number of duplicate rows found, number removed, and output filename. Keep the original dataset unchanged.
