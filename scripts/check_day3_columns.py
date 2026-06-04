
import pandas as pd

files = [
    "data/raw/02_nav_history.csv",
    "data/raw/03_aum_by_fund_house.csv",
    "data/raw/04_monthly_sip_inflows.csv",
    "data/raw/05_category_inflows.csv",
    "data/raw/06_industry_folio_count.csv",
    "data/raw/08_investor_transactions.csv",
    "data/raw/09_portfolio_holdings.csv"
]

for file in files:
    df = pd.read_csv(file)

    print("\n" + "="*50)
    print(file)
    print(df.columns.tolist())