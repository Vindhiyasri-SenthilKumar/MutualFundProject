import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

df = df.drop_duplicates()

df['launch_date'] = pd.to_datetime(
    df['launch_date'],
    errors='coerce'
)

df['expense_ratio_pct'] = pd.to_numeric(
    df['expense_ratio_pct'],
    errors='coerce'
)

df['exit_load_pct'] = pd.to_numeric(
    df['exit_load_pct'],
    errors='coerce'
)

df = df[df['amfi_code'].notna()]

df.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

print("Fund Master cleaned:", len(df))