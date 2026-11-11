import pandas as pd

                                # Load CSV file
df = pd.read_csv("dummy.csv")

                                # Remove spaces from column names
df.columns = df.columns.str.strip()

                                  # Display column names
print("Available columns:", df.columns.tolist())

                                  # Display first 5 rows

print(df.head())

                                    # Count unique values in each column

print(df.nunique())