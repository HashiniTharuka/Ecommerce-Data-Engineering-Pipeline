# E-Commerce Data Engineering Project — Phase 1

## Business scenario
An e-commerce company receives daily order, customer, and product data.
The project will later ingest, validate, transform, load, monitor, and support this data pipeline.

## Files
- orders.csv: transaction/order records
- customers.csv: customer master data
- products.csv: product master data

## Important
These are intentionally RAW sample files. They include a few data-quality issues for later practice:
- orders.csv: invalid order date, negative quantity/amount, duplicate order_id
- customers.csv: one missing email value

Do not clean these files yet. In a real pipeline, raw source data should be retained so we can compare it with transformed data.

## Key terms
- Source data: data received from an upstream system/file
- Row: one record
- Column: one attribute/field
- Header: the column names
- Data type: the kind of value stored (integer, decimal, text, date)
- Raw data: original data before transformation
