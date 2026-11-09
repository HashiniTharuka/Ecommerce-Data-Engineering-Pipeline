
import pandas as pd
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

files = {
    "Orders": "processed/cleaned_orders.csv",
    "Customers": "processed/cleaned_customers.csv",
    "Products": "products.csv"
}

report = []

report.append("E-COMMERCE PIPELINE MONITORING REPORT")
report.append(f"Execution Time: {datetime.now()}")
report.append("=" * 45)

for name, path in files.items():
    report.append(f"\nDataset: {name}")

    try:
        df = pd.read_csv(path)

        report.append("Status: SUCCESS")
        report.append(f"Rows: {len(df)}")
        report.append(f"Columns: {list(df.columns)}")

        if name == "Orders":
            issues = (
                df["order_id"].duplicated().sum()
                + df["order_date"].isna().sum()
                + (df["quantity"] < 0).sum()
                + (df["amount_lkr"] < 0).sum()
            )
            report.append(f"Data Quality Issues: {issues}")

        elif name == "Customers":
            issues = (
                df["customer_id"].isna().sum()
                + df["email"].isna().sum()
            )
            report.append(f"Data Quality Issues: {issues}")

        elif name == "Products":
            issues = (
                df["product_id"].duplicated().sum()
                + df["product_name"].isna().sum()
                + df["category"].isna().sum()
            )
            report.append(f"Data Quality Issues: {issues}")

    except Exception as e:
        report.append("Status: FAILED")
        report.append(f"Error: {e}")

report.append("\nEND OF REPORT")

output = "\n".join(report)

print(output)

with open("logs/pipeline_monitoring_report.txt", "w") as f:
    f.write(output)

print("\nMonitoring report saved successfully!")
