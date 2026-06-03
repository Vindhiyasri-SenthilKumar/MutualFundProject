import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

df = df.drop_duplicates()

df['portfolio_date'] = pd.to_datetime(
    df['portfolio_date'],
    errors='coerce'
)

numeric_cols = [
    'weight_pct',
    'market_value_cr',
    'current_price_inr'
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )

df.to_csv(
    "data/processed/portfolio_holdings_clean.csv",
    index=False
)

print("Portfolio holdings cleaned:", len(df))