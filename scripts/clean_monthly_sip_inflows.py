import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

df = df.drop_duplicates()

df['month'] = pd.to_datetime(
    df['month'],
    errors='coerce'
)

numeric_cols = [
    'sip_inflow_crore',
    'active_sip_accounts_crore',
    'new_sip_accounts_lakh',
    'sip_aum_lakh_crore',
    'yoy_growth_pct'
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )

df.to_csv(
    "data/processed/monthly_sip_inflows_clean.csv",
    index=False
)

print("SIP inflows cleaned:", len(df))