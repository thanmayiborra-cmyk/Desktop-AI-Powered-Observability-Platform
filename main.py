import csv
from datetime import datetime

print("AI Incident Resolution Assistant Started")

incident_count = 0
critical_count = 0
with open("data/observability_data.csv", "r") as file:
    reader = csv.DictReader(file) 
    for row in reader:
            cpu = int(row["cpu_usage"])
            memory = int(row["memory_usage"])
            response = int(row["response_time"].replace("s", ""))

            if cpu > 90 or memory > 90 or response > 300:

                incident_count += 1

                if cpu > 95 and memory > 95:
                    severity = "CRITICAL"
                    critical_count += 1
                elif cpu > 90 or memory > 90:
                    severity = "HIGH"
                else:
                    severity = "MEDIUM"

                print("\nIncident Detected")
                print("Severity :", severity)
                print("CPU Usage :", cpu)
                print("Memory Usage :", memory)
                print("Response Time :", response)
                if response > 400:
                    root_cause = "Application Performance Issue"
                elif memory > 90:
                    root_cause = "Memory Bottleneck"
                elif cpu > 90:
                    root_cause = "High CPU Utilization"
                else:
                    root_cause = "Unknown"

                print("Root Cause :", root_cause)

print("\n========== INCIDENT SUMMARY ==========")
print("Total Incidents :", incident_count)
print("Critical Incidents :", critical_count)
print("Generated At :", datetime.now())
print("Total Incidents :", incident_count)
print("Critical Incidents :", critical_count)
print("Generated At :", datetime.now())
health_score = 100 - (critical_count * 10) - (incident_count * 5)

if health_score < 0:
    health_score = 0

print("System Health Score :", health_score, "%")

if health_score >= 80:
    print("System Status : HEALTHY")
elif health_score >= 50:
    print("System Status : WARNING")
else:
    print("System Status : CRITICAL")
    print("\n========== AI RECOMMENDATIONS ==========")

if critical_count > 0:
    print("Recommendation : Immediate investigation required.")
    print("Recommendation : Scale resources and review application logs.")
elif incident_count > 0:
    print("Recommendation : Monitor system closely.")
    print("Recommendation : Review performance metrics.")
else:
    print("Recommendation : No major issues detected.")

print("\nAI Incident Resolution Assistant Completed")
