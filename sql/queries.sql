-- 1 Top 5 funds by AUM

SELECT
scheme_name,
aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV

SELECT
AVG(nav)
FROM nav_history;

-- 3 Transactions by State

SELECT
state,
COUNT(*)
FROM investor_transactions
GROUP BY state;

-- 4 SIP Transactions

SELECT
COUNT(*)
FROM investor_transactions
WHERE transaction_type='SIP';

-- 5 Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Number of Schemes by Fund House

SELECT
fund_house,
COUNT(*) AS total_schemes
FROM fund_master
GROUP BY fund_house
ORDER BY total_schemes DESC;


-- 7. Number of Schemes by Category

SELECT
category,
COUNT(*) AS total_schemes
FROM fund_master
GROUP BY category
ORDER BY total_schemes DESC;


-- 8. Number of Schemes by Sub Category

SELECT
sub_category,
COUNT(*) AS total_schemes
FROM fund_master
GROUP BY sub_category
ORDER BY total_schemes DESC;


-- 9. Number of Schemes by Risk Category

SELECT
risk_category,
COUNT(*) AS total_schemes
FROM fund_master
GROUP BY risk_category
ORDER BY total_schemes DESC;


-- 10. Average Expense Ratio by Category

SELECT
category,
ROUND(AVG(expense_ratio_pct),2) AS avg_expense_ratio
FROM fund_master
GROUP BY category
ORDER BY avg_expense_ratio DESC;