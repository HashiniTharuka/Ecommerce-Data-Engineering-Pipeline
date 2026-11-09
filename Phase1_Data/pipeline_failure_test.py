
import pandas as pd
from datetime import datetime

file_path = "processed/missing_test_file.csv"

print("PIPELINE FAILURE SIMULATION")
print("=" * 35)

try:
    df = pd.read_csv(file_path)
    print("Status: SUCCESS")

except FileNotFoundError as e:
    print("Status: FAILED")
    print("Error Type: FileNotFoundError")
    print("Root Cause: Source file not found.")
    print("Recovery: Verify source file path and availability.")

    with open("logs/failure_incident_report.txt", "w") as f:
        f.write("INCIDENT REPORT\n")
        f.write(f"Time: {datetime.now()}\n")
        f.write("Severity: Low (Simulation)\n")
        f.write("Error: FileNotFoundError\n")
        f.write("Root Cause: Source file not found.\n")
        f.write("Resolution: Verify file path and availability.\n")
        f.write("Status: Simulated failure documented.\n")

    print("\nIncident report saved successfully.")
