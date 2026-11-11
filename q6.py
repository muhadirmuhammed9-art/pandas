import pandas as pd

# Load the CSV file
df = pd.read_csv("dummy.csv")

# Display the first 5 rows
print("Original Dataset:")
print(df.head())

# Display all Quantity values
print("\nQuantity Values:")
print(df["Quantity"])

# Find the maximum quantity
print("\nMaximum Quantity:")
print(df["Quantity"].max())

# Filter orders where Quantity is greater than 5
result = df[df["Quantity"] > 5]

# Display filtered orders
print("\nOrders where Quantity is greater than 5:")
print(result)

# Count matching orders
print("\nTotal matching orders:", len(result))