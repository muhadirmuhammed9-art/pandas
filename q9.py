import pandas as pd
df = pd.read_csv("dummy.csv")
result = df.sort_values("Price", ascending=False).head(10)
print(result)