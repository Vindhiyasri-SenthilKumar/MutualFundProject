import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

files = {
    "fund_master":"data/processed/fund_master_clean.csv",
    "nav_history":"data/processed/nav_history_clean.csv",
    "aum_by_fund_house":"data/processed/aum_by_fund_house_clean.csv",
    "monthly_sip_inflows":"data/processed/monthly_sip_inflows_clean.csv",
    "category_inflows":"data/processed/category_inflows_clean.csv",
    "industry_folio_count":"data/processed/industry_folio_count_clean.csv",
    "scheme_performance":"data/processed/scheme_performance_clean.csv",
    "investor_transactions":"data/processed/investor_transactions_clean.csv",
    "portfolio_holdings":"data/processed/portfolio_holdings_clean.csv",
    "benchmark_indices":"data/processed/benchmark_indices_clean.csv"
}

for table, file in files.items():
    df = pd.read_csv(file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table} loaded: {len(df)} rows")

print("\nDatabase created successfully")