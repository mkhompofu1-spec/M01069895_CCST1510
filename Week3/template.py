"""
RECORD CHECK  -  my version
===========================

Name  :mkhokheli neville mpofu
Lane  :  AI / Cyber / IT      (delete two)
Date  :10/06/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# your function(s) go here
def status_of(percent):
    """Returns status based on percentage"""

    if percent >= 100:
       return "Over Limit"
    elif percent >= 90:
       return "Warning"
    else:
        return "OK"

def check(value, limit):
    """Returns the difference and percentage as two values"""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Prints report"""
    print(label, value, limit, difference, percent, status)




# ==================================================================== INPUT
# 2. Ask for your three values.
label = input("Enter a name:, hostname:, IP:")     
value = float(input("Enter value:"))   
limit = float(input("Enter limit number:")) 

# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
difference = value - limit   
percent = (value / limit) * 100    
status = status_of(percent)         


# =================================================================== OUTPUT
# 4. Print the report.
# your report lines go here
print("=" * 34)
print(f"Lable: {label}")
print(f"Value: {value}")
print(f"Limit: {limit}")
print(f"Difference: {difference:.2f}")
print(f"Percent: {percent:.2f}")
print(f"Status: {status}")
print("=" * 34)

# ==========================================================================
#ZeroDivisionError: float division by zero