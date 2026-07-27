import sys
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

def load_and_clean_data(sales_df, customers_df):
    # قراءة الملفين وتنظيف القيم المفقودة والتكرارات والتواريخ
    sales_df = pd.read_csv("sales.csv")
    customers_df = pd.read_csv("customers.csv")
    sales_df = sales_df.drop_duplicates()
    sales_df["Quantity"] = sales_df["Quantity"].fillna(1)
    sales_df["Price"] = sales_df["Price"].fillna(sales_df["Price"].mean())
    sales_df["Date"] = pd.to_datetime(sales_df["Date"])
    return sales_df, customers_df

def merge_and_analyze(sales_df, customers_df):
    # دمج الجدولين + حساب Total_Amount واستخراج المبيعات حسب المدينة والشهر
    merged_df = pd.merge(sales_df , customers_df , on="Customer_ID", how="inner")
    merged_df["Total_Amount"] = merged_df["Quantity"] * merged_df["Price"]
    merged_df["Month"] = merged_df["Date"].dt.month
    print("--- المبيعات حسب المدينة ---")
    print(merged_df.groupby("City") ["Total_Amount"].sum())
    print("--المبيعات حسب الشهر---")
    print(merged_df.groupby("Month") ["Total_Amount"].sum())

    return merged_df


def export_report(final_df):
    # تصدير التقرير إلى final_sales_report.csv
   
    final_df.to_csv("final_sales_report.csv", index=False)
    print("\nتم تصدير التقرير بنجاح إلى final_sales_report.csv")
    return final_df

# --- التشغيل ---

sales_df, customers_df = load_and_clean_data("sales.csv", "customers.csv")
final_df = merge_and_analyze(sales_df, customers_df)
export_report(final_df)
print(sales_df, customers_df)
print(final_df)