import pandas as pd
df = pd.read_csv("dummy.csv")
result = df[(df["Category"] == "Electronics") & (df["Quantity"] > 2)]
print(result)