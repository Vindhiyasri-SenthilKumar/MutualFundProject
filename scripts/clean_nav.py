import pandas as pd

# Load data
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Sort data
df = df.sort_values(
    by=['amfi_code', 'date']
)

# Forward fill missing NAV values
df['nav'] = df.groupby(
    'amfi_code'
)['nav'].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Keep only valid NAV values
df = df[df['nav'] > 0]

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV cleaning completed")
print("Rows:", len(df))