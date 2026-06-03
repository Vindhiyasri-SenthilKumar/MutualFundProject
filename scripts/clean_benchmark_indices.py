import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

df = df.drop_duplicates()

df['date'] = pd.to_datetime(
    df['date'],
    errors='coerce'
)

df['close_value'] = pd.to_numeric(
    df['close_value'],
    errors='coerce'
)

df.to_csv(
    "data/processed/benchmark_indices_clean.csv",
    index=False
)

print("Benchmark cleaned:", len(df))