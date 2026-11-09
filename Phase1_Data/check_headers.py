import pandas as pd

files = [
    "processed/cleaned_customers.csv",
    "processed/cleaned_orders.csv",
    "products.csv"
]

for file in files:
    df = pd.read_csv(file)
    print(file, "->", list(df.columns))