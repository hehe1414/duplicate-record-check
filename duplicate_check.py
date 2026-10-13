"""
Duplicate Record Check
Demo dataset: sample_retail_sales.csv
Run: python duplicate_check.py
Requires: pandas
"""
from pathlib import Path
import pandas as pd

DATA_FILE = Path("sample_retail_sales.csv")
REPORT_FILE = Path("duplicate_report.csv")
CLEAN_FILE = Path("cleaned_retail_sales.csv")
AUDIT_FILE = Path("audit_note.txt")

df = pd.read_csv(DATA_FILE)

# Mark every row that belongs to a duplicate group.
duplicate_mask = df.duplicated(keep=False)
duplicate_report = df.loc[duplicate_mask].copy()

# Keep the first occurrence of each exact full-row duplicate.
cleaned_df = df.drop_duplicates().copy()

duplicate_report.to_csv(REPORT_FILE, index=False)
cleaned_df.to_csv(CLEAN_FILE, index=False)

audit_note = f"""Duplicate Record Check — Audit Note
Input file: {DATA_FILE.name}
Original rows: {len(df)}
Rows participating in duplicate groups: {int(duplicate_mask.sum())}
Extra duplicate rows removed (keep first): {len(df) - len(cleaned_df)}
Rows in cleaned file: {len(cleaned_df)}
Method: exact full-row matching with pandas duplicated(keep=False)
Cleaning rule: drop exact duplicate rows while keeping the first occurrence.
Important: this demo checks exact full-row duplicates. In real data, confirm business rules
before removing rows; records sharing an Order_ID may need investigation rather than deletion.
"""
AUDIT_FILE.write_text(audit_note, encoding="utf-8")

print(audit_note)
print("Created:", REPORT_FILE.name, CLEAN_FILE.name, AUDIT_FILE.name)
