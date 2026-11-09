\# End-to-End E-commerce Data Engineering Project



\## Project Overview



This project demonstrates an end-to-end e-commerce data pipeline using Python, Apache Airflow, and Snowflake.



The main objective is to clean, validate, orchestrate, and load e-commerce data into a Snowflake data warehouse, while practicing monitoring, troubleshooting, and incident management.



\## Architecture



```mermaid

flowchart TD

&#x20;   A\[Source CSV Files] --> B\[Python and Pandas]

&#x20;   B --> C\[Cleaned CSV Files]

&#x20;   C --> D\[Apache Airflow]

&#x20;   D --> E\[CSV Validation]

&#x20;   E --> F\[Snowflake Load]

&#x20;   F --> G\[Snowflake RAW\_DATA]

&#x20;   G --> H\[Data Validation and Analytics]

&#x20;   D -.-> I\[ServiceNow Incident Management]

```



\## Technologies Used



\- Python

\- Pandas

\- Apache Airflow 3.4.0

\- Docker and Docker Compose

\- Snowflake

\- SQL

\- ServiceNow Personal Developer Instance

\- Git and GitHub



\## Project Implementation



\### 1. Data Cleaning

\- Cleaned e-commerce Orders and Customers CSV files using Python and Pandas.

\- Removed duplicate and invalid order records.

\- Handled missing customer email values.

\- Generated cleaned datasets and a data quality report.



\### 2. Monitoring and Troubleshooting

\- Created local Python monitoring scripts.

\- Simulated pipeline failures.

\- Identified missing source file errors.

\- Documented root causes and recovery actions.



\### 3. Snowflake Data Warehouse

\- Created the ECOMMERCE\_DB database and RAW\_DATA schema.

\- Created CUSTOMERS, PRODUCTS, and ORDERS tables.

\- Loaded and validated datasets.

\- Created analytical SQL queries and views.



\### 4. Apache Airflow

\- Set up Apache Airflow using Docker Compose.

\- Developed DAGs for pipeline execution and CSV validation.

\- Implemented retry handling.

\- Integrated Airflow with Snowflake.

\- Loaded CSV data into Snowflake using SnowflakeHook.

\- Tested repeated execution and idempotency.



\### 5. ServiceNow Incident Management

\- Created a training incident in ServiceNow PDI.

\- Practiced incident investigation and resolution.

\- Documented troubleshooting activities and support responsibilities.



\### 6. Production Support

\- Practiced Airflow DAG and task monitoring.

\- Investigated task logs and common errors.

\- Prepared an L1 troubleshooting checklist.

\- Documented incident investigation and recovery.



\## Data Validation Results



| Dataset | Validated Records |

|---|---:|

| Customers | 8 |

| Products | 5 |

| Orders | 8 |

| \*\*Total\*\* | \*\*21\*\* |



All expected record counts were verified in Snowflake. Repeated DAG execution did not increase the record counts.



\## Azure Data Factory – Design Stage



An Azure Data Factory pipeline architecture was designed for CSV ingestion and Azure Data Lake Storage Gen2 integration.



\*\*Note:\*\* Azure Data Factory and ADLS Gen2 deployment was not completed because the Azure subscription was disabled. These components are design-stage only.



\## Project Learning Outcomes



\- Data cleaning and validation

\- ETL pipeline development

\- Workflow orchestration

\- Snowflake data loading and SQL analytics

\- Pipeline monitoring and troubleshooting

\- Incident management

\- L1 production support practices

\- Version control using Git and GitHub



\## Disclaimer



This is a learning and portfolio project. ServiceNow incidents and pipeline failures were created or simulated for practice. No real production outage occurred.

