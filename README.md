# Namaa Market Sales Analytics

A practical Pandas and Excel analytics project for **Namaa Market**, a fictional Jordanian e-commerce company.

## Project contents

- `analysis.py` — reproducible cleaning, enrichment, KPI, and reporting pipeline.
- `customers.csv`, `products.csv`, `orders.csv` — synthetic training data.
- `BRIEF.md` — business case and management questions.
- `reports/Namaa_Market_Final_Report.xlsx` — completed Excel dashboard and insights report.

## What the analysis covers

- Data-quality checks and duplicate handling.
- Customer and product joins.
- Revenue, discounts, cost, gross profit, and profit margin.
- Analysis by city, month, product, category, payment method, and order status.
- Excel dashboard with charts and management recommendations.

## Run locally

```bash
python -m pip install pandas openpyxl
python analysis.py
```

The script generates `Namaa_Market_Analysis.xlsx` in the project directory. The data is synthetic and created for training only.
