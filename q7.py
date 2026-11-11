import pandas as pd
df = pd.read_csv("dummy.csv")
result = df[df["Price"] > 1000]
print(result)