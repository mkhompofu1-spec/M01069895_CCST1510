# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

piece = "note=server=east"
key, value = piece.split("=", 1)
#there are too many vaules to unpack so we use 1 to tell python to only unpack 1. or we mcan make 3 values to match the 3 variables

print(key, value)

piece = "note=server=east"
key, value, output = piece.split("=",) #or we can make 3 values to match the 3 variables

print(key, value, output)
