import pandas as pd

df = pd.read_csv("data/raw/06_industry_folio_count.csv")

df = df.drop_duplicates()

df['month'] = pd.to_datetime(
    df['month'],
    errors='coerce'
)

cols = [
    'total_folios_crore',
    'equity_folios_crore',
    'debt_folios_crore',
    'hybrid_folios_crore',
    'others_folios_crore'
]

for col in cols:
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )

df.to_csv(
    "data/processed/industry_folio_count_clean.csv",
    index=False
)

print("Industry folio cleaned:", len(df))