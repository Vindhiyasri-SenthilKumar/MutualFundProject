import pandas as pd

df = pd.read_csv("data/raw/05_category_inflows.csv")

df = df.drop_duplicates()

df['month'] = pd.to_datetime(
    df['month'],
    errors='coerce'
)

df['net_inflow_crore'] = pd.to_numeric(
    df['net_inflow_crore'],
    errors='coerce'
)

df['category'] = df['category'].str.strip()

df.to_csv(
    "data/processed/category_inflows_clean.csv",
    index=False
)

print("Category inflows cleaned:", len(df))