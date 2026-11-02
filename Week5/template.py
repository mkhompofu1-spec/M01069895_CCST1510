"""
RECORD CHECK  -  my version
===========================

Name  :Mkhokheli Neville Mpofu
Lane  :  AI / Cyber / IT      (delete two)
Date  :22/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.

#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit
    
    def percent(self):
        """Return value as a percentage of limit."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on percent()."""
        p = self.percent()
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS
# 2. Create your records.
r1 = Record("R-001", 87.0, 100.0)
r2 = Record("R-002", 120.0, 100.0)


# ==================================================================== OUTPUT
# 3. Print a report for each record.
print("=" * 34)
print(r1.label, r1.status())
print(r2.label, r2.status())
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
