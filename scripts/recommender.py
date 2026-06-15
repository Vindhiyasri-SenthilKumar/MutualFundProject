# ==========================================================
# TASK 5 - FUND RECOMMENDATION ENGINE
# ==========================================================
# Objective:
# Input  : Investor Risk Appetite
# Output : Top 3 Funds by Sharpe Ratio
# Method : Create Risk Grades using Max Drawdown
# ==========================================================

import pandas as pd
from pathlib import Path

# ----------------------------------------------------------
# Project Paths
# ----------------------------------------------------------

PROJECT_DIR = Path(
    r"C:\Users\ELCOT\Documents\MutualFundProject"
)

DATA_DIR = PROJECT_DIR / "data" / "processed"

# ----------------------------------------------------------
# Load Fund Scorecard
# ----------------------------------------------------------

funds_df = pd.read_csv(
    DATA_DIR / "fund_scorecard.csv"
)

# ----------------------------------------------------------
# Create Risk Grades
# ----------------------------------------------------------
# Lowest Drawdown  -> Low Risk
# Medium Drawdown  -> Moderate Risk
# Highest Drawdown -> High Risk
# ----------------------------------------------------------

funds_df["risk_grade"] = pd.qcut(
    funds_df["max_drawdown"],
    q=3,
    labels=["Low", "Moderate", "High"]
)

# ----------------------------------------------------------
# Recommendation Function
# ----------------------------------------------------------

def recommend_funds(risk_appetite):

    filtered_funds = (
        funds_df[
            funds_df["risk_grade"]
            .astype(str)
            .str.lower()
            ==
            risk_appetite.lower()
        ]
    )

    recommendations = (
        filtered_funds
        .sort_values(
            by="sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return recommendations[
        [
            "amfi_code",
            "risk_grade",
            "sharpe_ratio",
            "fund_score_100"
        ]
    ]

# ----------------------------------------------------------
# Display Available Categories
# ----------------------------------------------------------

print("\nRisk Grade Distribution")
print(
    funds_df["risk_grade"]
    .value_counts()
)

# ----------------------------------------------------------
# User Input
# ----------------------------------------------------------

risk_appetite = input(
    "\nEnter Risk Appetite (Low/Moderate/High): "
)

# ----------------------------------------------------------
# Generate Recommendations
# ----------------------------------------------------------

recommended_funds = recommend_funds(
    risk_appetite
)

# ----------------------------------------------------------
# Display Output
# ----------------------------------------------------------

print("\n" + "=" * 60)
print(f"TOP 3 FUND RECOMMENDATIONS ({risk_appetite.upper()} RISK)")
print("=" * 60)

if len(recommended_funds) == 0:

    print("No matching funds found.")

else:

    print(
        recommended_funds.to_string(
            index=False
        )
    )