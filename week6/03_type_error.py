# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"value": [87, 120, 45], "limit": [100, 100, 100]}) #type error. the objects in value should be integers not strings

df["percent"] = (df["value"] / df["limit"]) * 100
print(df) #there should be a print statement here to print the dataframe
