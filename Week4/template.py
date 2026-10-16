"""
RECORD CHECK  -  my version
===========================

Name  :mkhokheli neville mpofu
Lane  :  AI / Cyber / IT      (delete two)
Date  :15/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
''' Storing the code'''
def check_record(value, limit):
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    print(f"Lable: {label}")
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference:.2f}")
    print(f"Percent: {percent:.2f}")
    print(f"Status: {status}")


# ====================================================================== STORE
records = [{"label": "Maths", "value": 45, "limit": 100},
           {"label": "English", "value": 80, "limit": 100},
            {"label": "something", "value": 90, "limit": 200}
            ]


# =============================================================== PROCESS + OUTPUT
''' loopoing the code the printing it'''
for record in records:
    label = record["label"]
    value = record["value"]
    limit = record["limit"]

    difference, percent = check_record(value, limit)
    if value > limit:
        status = "over limit"
    else:
        status = "Excellent"
    print_report(label, value, limit, difference, percent, status)
