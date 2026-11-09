\# L1 Production Support Troubleshooting Checklist



\## 1. Airflow Monitoring



\- \[ ] Open Airflow UI.

\- \[ ] Check DAG status.

\- \[ ] Identify failed DAG runs.

\- \[ ] Identify failed task instances.



\## 2. Log Investigation



\- \[ ] Open failed task logs.

\- \[ ] Identify the error message and error code.

\- \[ ] Record the failure time.

\- \[ ] Identify the affected dataset or process.



\## 3. Common Failure Checks



\- \[ ] Verify source CSV file availability.

\- \[ ] Verify expected file paths.

\- \[ ] Check CSV headers and row counts.

\- \[ ] Identify Snowflake connection failures.

\- \[ ] Check Snowflake load task status.



\## 4. Incident Handling



\- \[ ] Record incident details.

\- \[ ] Document the observed error.

\- \[ ] Identify the possible root cause.

\- \[ ] Escalate configuration or credential issues to the authorized team.

\- \[ ] Verify recovery after resolution.



\## 5. Security



\- \[ ] Never share passwords or access tokens.

\- \[ ] Never expose connection secrets in logs or reports.

\- \[ ] Follow authorized access procedures.

