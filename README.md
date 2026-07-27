The Sales & Customer Analytics System is a modular Python pipeline developed using Pandas to automate data cleaning, integration, analysis, and reporting for retail sales and customer datasets.

Key Features & Technical Implementation

Data Cleaning & Preprocessing: Identifies and eliminates duplicate records, performs statistical imputation for missing numerical values (mean/default substitution), and converts raw strings into structured pandas datetime objects.

Relational Data Integration: Merges transactional sales logs with demographic customer data using relational key matching (Customer_ID).

Feature Engineering: Derives calculated metrics such as total revenue per transaction (Price * Quantity) and extracts temporal features (Month) for trend evaluation.

Data Aggregation & Insights: Computes sales metrics grouped by geographical distribution (City) and time periods (Month) using groupby() aggregations.

Automated Reporting: Exports the transformed dataset into a clean, structured output file (final_sales_report.csv).

Tech Stack & Architecture

Language & Libraries: Python 3, Pandas

Concepts: ETL (Extract, Transform, Load), Data Imputation, Relational Merging, Modular Programming.
