 Mutual Fund Analytics Platform

 Project Overview

The Mutual Fund Analytics Platform was developed as part of the Bluestock Fintech Data Analyst Internship. The project integrates multiple mutual fund datasets, performs ETL processing, calculates risk and performance metrics, and provides interactive Power BI dashboards for investment analysis.

The platform enables users to analyze industry trends, evaluate fund performance, compare risk-adjusted returns, and understand investor behavior through data-driven insights.

 Technologies Used

* Python
* Pandas
* NumPy
* SciPy
* PostgreSQL
* SQL
* Power BI
* Git & GitHub


 Project Structure

```text
MUTUALFUNDPROJECT/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── ETL.ipynb
│   ├── EDA_Analysis.ipynb
│   ├── EDA_Findings.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
│
├── sql/
│
├── dashboard/
│   └── Mutual_Fund_Dashboard.pbix
│
├── run_pipeline.py
│
└── README.md
```



 Data Sources

The project uses the following datasets:

* Fund Master Data
* NAV History
* Benchmark Indices
* Category Inflows
* Investor Transactions
* Industry Folio Count



 ETL Process

The ETL pipeline performs the following operations:

1. Extract raw CSV datasets
2. Clean and validate data
3. Handle missing values and duplicates
4. Standardize formats and data types
5. Create derived metrics and features
6. Store processed datasets for analytics



 How to Run the Project

 Clone Repository

```bash
git clone <repository-url>
cd MUTUALFUNDPROJECT
```

 Install Dependencies

```bash
pip install pandas numpy scipy matplotlib seaborn
```

 Run Pipeline

```bash
python run_pipeline.py
```


 Performance Metrics Calculated

* CAGR (Compound Annual Growth Rate)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Tracking Error

---

 Dashboard Modules

 Dashboard 1 – Industry Overview

* Total AUM
* SIP Inflows
* Investor Folios
* Scheme Analysis

 Dashboard 2 – SIP & Market Trends

* Category-wise Inflows
* Market Trend Analysis

 Dashboard 3 – Fund Performance Analytics

* Risk & Return Metrics
* Fund Scorecard
* Benchmark Comparison

 Dashboard 4 – Investor Analytics

* Transaction Analysis
* Age Group Distribution
* Geographic Analysis



 How to Open Dashboard

1. Open Power BI Desktop
2. Open `Mutual_Fund_Dashboard.pbix`
3. Refresh data if required
4. Navigate through dashboard pages using tabs



 Key Insights

* Total AUM Analyzed: ₹62.74 Lakh Crore
* SIP Inflows: ₹15.90 Lakh Crore
* Highest Category Inflow: Liquid Fund (₹4,51,275 Crore)
* Highest Sharpe Ratio: ICICI Pru Liquid Fund (7.68)
* Highest 3-Year Return: SBI Small Cap Fund (23.39%)
* Highest AUM Fund: Mirae Asset Emerging Bluechip Fund (₹49,046 Crore)



 