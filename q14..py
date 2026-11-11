import pandas as pd
df = pd.read_csv("dummy.csv")
highest = df["Price"].max()
lowest = df["Price"].min()
print("Highest Price:", highest)
print("Lowest Price:", lowest)