\# E-commerce Data Engineering Project – Architecture



\## 1. Implemented Architecture



```mermaid

flowchart TD

&#x20;   A\[Source CSV Files] --> B\[Python Data Cleaning]

&#x20;   B --> C\[Cleaned CSV Files]

&#x20;   C --> D\[Apache Airflow]

&#x20;   D --> E\[CSV Validation]

&#x20;   E --> F\[Snowflake Load DAG]

&#x20;   F --> G\[Snowflake RAW\_DATA]

&#x20;   G --> H\[Data Validation]

&#x20;   G --> I\[Analytics Views]



&#x20;   J\[ServiceNow PDI] -.-> K\[Incident Management]

&#x20;   D -.-> K

```



\## 2. Technologies



\- Python and Pandas – Data cleaning

\- Apache Airflow – Workflow orchestration

\- Docker – Local Airflow environment

\- Snowflake – Data warehouse

\- SQL – Data validation and analysis

\- ServiceNow PDI – Incident management

\- Git and GitHub – Version control



\## 3. Planned Azure Architecture



```mermaid

flowchart LR

&#x20;   A\[Local CSV Files] --> B\[Azure Data Factory]

&#x20;   B --> C\[Azure Data Lake Storage Gen2]

&#x20;   C -.-> D\[Future Snowflake Integration]

```



\*\*Note:\*\* Azure Data Factory and ADLS Gen2 are design-stage components. They have not been deployed because the Azure subscription is disabled.



\## 4. Project Status



The local Python, Airflow, Snowflake and ServiceNow components were implemented and tested. Azure integration remains planned.

