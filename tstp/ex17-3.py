import re

line = "The ghost that says boo haunts the loo."

m = re.findall(".oo", line)

print(m)
