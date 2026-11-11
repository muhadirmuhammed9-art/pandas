import pandas as pd
df = pd.read_csv("dummy.csv")
df["Total_Amount"] = df["Quantity"] * df["Price"]
print(df)