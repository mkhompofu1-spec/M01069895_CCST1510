# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120, 95] #Value error. the objects in value and label should be the same amount
})

print(df) #there should be a print statement here to print the dataframe