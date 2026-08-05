from src.mitre.mapping import MITRE_MAPPING
from src.ai.risk_engine import RiskEngine
from src.ioc.extractor import IOCExtractor
from src.threat_intel.threat_db import ThreatDatabase

class AIAnalyzer:

    def __init__(self):
        self.risk_engine = RiskEngine()
        self.ioc_extractor = IOCExtractor()
        self.threat_db = ThreatDatabase()


    def analyze(self, alert):
        """
        Analyze security alert
        """

        threat = alert.get("threat")
        ip = alert.get("source_ip")
        attempts = alert.get("attempts")

        risk = self.risk_engine.calculate(alert)

        severity = self.risk_engine.get_severity(risk)

        mitre = MITRE_MAPPING.get(threat, {})
        ioc = self.ioc_extractor.extract(alert)
        threat_intel = self.threat_db.lookup_ip(ip)


        analysis = {
        "incident": threat,
        "severity": severity,
        "source_ip": ip,
        "attempts": attempts,
        "risk_score": risk,
        "ioc": ioc,
        "threat_intelligence": threat_intel,
        "mitre": mitre,
        "analysis": self.generate_analysis(alert),
        "recommendations": self.generate_recommendations(alert)
    }

        return analysis


    def generate_analysis(self, alert):

        threat = alert.get("threat")

        if threat == "SSH Brute Force":
            return (
                "Multiple failed SSH login attempts were detected from the same "
                "source IP. This behavior is consistent with a brute force attack "
                "targeting SSH authentication."
            )

        elif threat == "SQL Injection Attempt":
            return (
                "The request contains SQL Injection patterns that may allow an "
                "attacker to manipulate database queries and access sensitive data."
            )

        elif threat == "Failed Web Login":
            return (
                "Multiple failed authentication attempts were observed on the web "
                "application. This may indicate password guessing or credential abuse."
            )

        elif threat == "Admin Page Access Attempt":
            return (
                "An unauthorized attempt to access a restricted administrative page "
                "was detected."
            )

        elif threat == "Cross Site Scripting (XSS)":
            return (
                "The request contains JavaScript code that may execute inside a "
                "victim's browser and compromise user sessions."
            )

        elif threat == "Path Traversal Attempt":
            return (
                "The request attempts to access files outside the intended web "
                "directory using directory traversal techniques."
            )

        elif threat == "Command Injection Attempt":
            return (
                "The request contains operating system command execution patterns. "
                "Successful exploitation could lead to remote code execution."
            )

        return "Unknown security event detected."



    def generate_recommendations(self, alert):

        threat = alert.get("threat")

        if threat == "SSH Brute Force":
            return [
                "Block the source IP",
                "Enable Multi-Factor Authentication (MFA)",
                "Review SSH configuration",
                "Monitor authentication logs"
            ]

        elif threat == "SQL Injection Attempt":
            return [
                "Use parameterized SQL queries",
                "Validate and sanitize user input",
                "Deploy a Web Application Firewall (WAF)",
                "Review database access logs"
            ]

        elif threat == "Failed Web Login":
            return [
                "Enable account lockout policy",
                "Monitor authentication attempts",
                "Enforce strong passwords",
                "Enable Multi-Factor Authentication"
            ]

        elif threat == "Admin Page Access Attempt":
            return [
                "Restrict admin page access",
                "Review firewall rules",
                "Enable IP allow-listing",
                "Monitor privileged access"
            ]

        elif threat == "Cross Site Scripting (XSS)":
            return [
                "Sanitize user input",
                "Encode HTML output",
                "Enable Content Security Policy (CSP)",
                "Validate all client input"
            ]

        elif threat == "Path Traversal Attempt":
            return [
                "Validate file paths",
                "Restrict filesystem permissions",
                "Use allow-listed directories",
                "Monitor file access logs"
            ]

        elif threat == "Command Injection Attempt":
            return [
                "Avoid shell command execution",
                "Validate all input parameters",
                "Run services with least privilege",
                "Monitor command execution logs"
            ]

        return [
            "Investigate the activity",
            "Collect additional logs",
            "Review affected systems"
        ]
