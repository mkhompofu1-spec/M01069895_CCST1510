"""
RECORD CHECK  -  my version
===========================

Name  :Mkhokheli Neville Mpofu
Lane  :  AI / Cyber / IT      (delete two)
Date  :01/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
label = input("Enter a label): ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))



# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = (first - second) 
percent = (first / second) * 100



# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print("=" * 34)
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"label:{label}")
print(f"First Number: {first:>10.2f}")
print(f"Second Number: {second:>10.2f}")
print(f"Difference: {difference:>+10.2f}")
print(f"Percent:{percent:>10.2f}")

print("=" * 34)

# if the total is 0, the error is ZeroDivisionError: float division by zero
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
