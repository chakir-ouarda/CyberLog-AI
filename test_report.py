from src.reporting.report_generator import ReportGenerator


report_data = {
    "incident": "SSH Brute Force",
    "severity": "HIGH",
    "source_ip": "192.168.1.10",
    "risk_score": 50
}


generator = ReportGenerator()


file = generator.generate_json_report(report_data)


print("Report created:", file)
