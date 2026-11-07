"""
RECORD CHECK  -  my version
===========================

Name  :mkhokheli neville mpofu
Lane  :  AI / Cyber / IT      (delete two)
Date  :06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

"""Cleans and parses a raw, messy line into a dictionary."""
def parse_line(raw_line):
    parts = raw_line.strip().upper().split(",")
    data = {}
    for part in parts:
        key, value = part.split("=", 1)
        data[key.strip()] = value.strip()
    return data

def status_of(data):
    if data["RESULT"] == "FAILED" or int(data.get("ATTEMPTS", 0)) > 10:
        return "FLAGGED"
    else:
        return "OK"

raw_records = [
    " SRC=10.0.0.5, ATTEMPTS=12, RESULT=FAILED",
          " SRC=10.0.0.5, ATTEMPTS=20, RESULT=SUCCESS",
      " src=100.16.0.7, ATTEMPTS=2, RESULT=success"
       " SRC=170.09.50.5, attempts=12, RESULT=FAILED"

 " src=100.0.0.1, attempts=1, result=success"
]

for record in raw_records:
    cleaned_data = parse_line(record)
    status = status_of(cleaned_data)
    print(cleaned_data, status)

