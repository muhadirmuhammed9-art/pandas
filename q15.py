import pandas as pd
df=pd.read_csv("dummy.csv")
result=df.groupby("Category")["Quantity"].sum()
print("Total Quantity Sold For Each Category:")
print(result)
