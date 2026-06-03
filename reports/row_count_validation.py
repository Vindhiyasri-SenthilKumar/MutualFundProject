import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

tables = [
    "fund_master",
    "nav_history",
    "aum_by_fund_house",
    "monthly_sip_inflows",
    "category_inflows",
    "industry_folio_count",
    "scheme_performance",
    "investor_transactions",
    "portfolio_holdings",
    "benchmark_indices"
]

for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table}",
        engine
    )

    print(table, count["cnt"][0])