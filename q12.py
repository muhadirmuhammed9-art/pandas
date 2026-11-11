import pandas as pd
df = pd.read_csv("dummy.csv")
df["Total_Amount"] = df["Quantity"] * df["Price"]
total_sales = df["Total_Amount"].sum()
print("Total Sales Amount:", total_sales)