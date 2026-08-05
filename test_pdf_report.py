from src.reporting.report_generator import ReportGenerator


report_data = {
    "incident": "SSH Brute Force",
    "severity": "HIGH",
    "source_ip": "192.168.1.10",
    "risk_score": 50,
    "analysis": "Multiple failed SSH login attempts were detected from the same source IP.",
    "recommendations": [
        "Block the source IP",
        "Enable Multi-Factor Authentication",
        "Review SSH configuration",
        "Monitor authentication logs"
    ]
}


generator = ReportGenerator()

pdf_file = generator.generate_pdf_report(report_data)

print("PDF Report created:", pdf_file)
