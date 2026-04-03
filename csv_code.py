import pandas as pd

# Load all CSVs
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine them
df = pd.concat([df1, df2, df3], ignore_index=True)

# Filter for Pink Morsels
df = df[df["product"] == "pink morsel"]

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only relevant columns
df = df[["date", "region", "sales"]]

# Optional: ensure date is datetime
df["date"] = pd.to_datetime(df["date"])

# Preview result
print(df.head())