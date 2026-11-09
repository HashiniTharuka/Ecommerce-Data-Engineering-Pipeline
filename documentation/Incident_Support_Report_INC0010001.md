\# Incident Support Report – INC0010001



\## 1. Incident Details



\- \*\*Incident ID:\*\* INC0010001

\- \*\*Incident Title:\*\* E-commerce Snowflake Data Load Failure

\- \*\*Category:\*\* Software – Application Error

\- \*\*Priority:\*\* High

\- \*\*Status:\*\* Resolved

\- \*\*Environment:\*\* Apache Airflow and Snowflake

\- \*\*Incident Type:\*\* Training / Simulation



\## 2. Incident Description



The E-commerce data pipeline experienced a simulated failure during the Snowflake data loading process. Investigation was required to identify the possible cause and verify successful pipeline execution.



\## 3. Investigation



The following checks were performed:



\- Reviewed Airflow DAG execution status.

\- Identified failed task instances.

\- Examined Airflow task logs.

\- Investigated the Snowflake connection.

\- Verified CSV source file availability.

\- Re-executed the Snowflake load DAG.



\## 4. Root Cause and Findings



The project included two simulated failure scenarios:



1\. \*\*Missing CSV file:\*\* FileNotFoundError occurred because the expected source CSV file was unavailable.

2\. \*\*Snowflake authentication failure:\*\* Error 390100 (28000) indicated incorrect username or password.



The missing file was restored, and the Snowflake Airflow connection credentials were updated successfully.



\## 5. Resolution and Verification



The Snowflake load DAG was executed successfully.



All four tasks completed successfully:



\- load\_customers

\- load\_products

\- load\_orders

\- validate\_snowflake\_counts



Final Snowflake record counts:



| Table | Records |

|---|---:|

| CUSTOMERS | 8 |

| PRODUCTS | 5 |

| ORDERS | 8 |



The DAG was executed again to test idempotency. Record counts remained unchanged.



\## 6. Preventive Actions



\- Verify source file availability before pipeline execution.

\- Monitor Airflow DAG and task statuses.

\- Review logs when failures occur.

\- Verify connection configuration through authorized procedures.

\- Maintain incident records and troubleshooting documentation.



\## 7. Support Responsibilities



\*\*L1 Support:\*\*

\- Monitor pipeline execution.

\- Identify failed tasks.

\- Review logs and document errors.

\- Perform basic checks and escalate when required.



\*\*L2 Support:\*\*

\- Investigate configuration and integration issues.

\- Support connection and pipeline troubleshooting.



\*\*L3 Support:\*\*

\- Handle complex application or underlying system defects.



\## 8. Final Note



This incident was created in a ServiceNow Personal Developer Instance for training purposes. No actual production outage occurred.



The investigation, recovery verification, and incident documentation were completed successfully.

