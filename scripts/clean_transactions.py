import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date column
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Keep only positive transaction amounts
df = df[df["amount_inr"] > 0]

# Validate KYC status
valid_kyc = ["Verified", "Pending", "Rejected"]

df = df[df["kyc_status"].isin(valid_kyc)]

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transaction cleaning completed")
print("Rows:", len(df))