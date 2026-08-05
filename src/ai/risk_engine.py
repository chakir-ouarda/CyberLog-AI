class RiskEngine:

    def calculate(self, alert):

        threat = alert.get("threat")

        scores = {
            "SSH Brute Force": 85,
            "Failed Web Login": 40,
            "Admin Page Access Attempt": 55,
            "SQL Injection Attempt": 95,
            "Cross Site Scripting (XSS)": 80,
            "Path Traversal Attempt": 90,
            "Command Injection Attempt": 100
        }

        return scores.get(threat, 25)


    def get_severity(self, score):

        if score >= 90:
            return "CRITICAL"

        elif score >= 70:
            return "HIGH"

        elif score >= 40:
            return "MEDIUM"

        else:
            return "LOW"
