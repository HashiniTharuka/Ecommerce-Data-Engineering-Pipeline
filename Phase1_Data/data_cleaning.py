import pandas as pd
import os

# Read original data
orders = pd.read_csv("orders.csv")

print("Original rows:", len(orders))

# Step 1: Remove duplicate Order IDs
orders = orders.drop_duplicates(
    subset=["order_id"],
    keep="first"
)

# Step 2: Convert order_date into date format
orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)

# Step 3: Remove invalid dates
orders = orders.dropna(subset=["order_date"])

# Step 4: Remove negative quantities and amounts
orders = orders[
    (orders["quantity"] > 0) &
    (orders["amount_lkr"] > 0)
]

# Step 5: Create processed folder
os.makedirs("processed", exist_ok=True)

# Step 6: Save cleaned data
orders.to_csv(
    "processed/cleaned_orders.csv",
    index=False
)

print("Cleaned rows:", len(orders))
print("Data cleaning completed!")
print(orders)

# STEP 7: Clean Customers Dataset

# Read original customers CSV
customers = pd.read_csv("customers.csv")

print("\nOriginal Customers:")
print(customers)

# Check missing emails
print("\nMissing Emails:")
print(customers[customers["email"].isna()])

# Replace missing email with Unknown
customers["email"] = customers["email"].fillna("Unknown")

# Save cleaned customers dataset
customers.to_csv(
    "processed/cleaned_customers.csv",
    index=False
)

print("\nCleaned Customers:")
print(customers)

print("\nCustomer cleaning completed!")

# STEP 8: Final Data Validation

# Read cleaned datasets
clean_orders = pd.read_csv("processed/cleaned_orders.csv")
clean_customers = pd.read_csv("processed/cleaned_customers.csv")

print("\n--- FINAL DATA VALIDATION ---")

# Validate Orders
print("\nOrders Validation:")
print("Total rows:", len(clean_orders))
print("Duplicate Order IDs:", clean_orders["order_id"].duplicated().sum())
print("Invalid dates:", pd.to_datetime(
    clean_orders["order_date"], errors="coerce"
).isna().sum())
print("Negative quantities:", (clean_orders["quantity"] < 0).sum())
print("Negative amounts:", (clean_orders["amount_lkr"] < 0).sum())

# Validate Customers
print("\nCustomers Validation:")
print("Total rows:", len(clean_customers))
print("Missing emails:", clean_customers["email"].isna().sum())
print("Unknown emails:", (clean_customers["email"] == "Unknown").sum())

print("\nFinal validation completed!")