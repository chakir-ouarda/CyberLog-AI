from collections import defaultdict


class DetectionEngine:

    def __init__(self, failed_threshold=3):
        self.failed_threshold = failed_threshold


    def detect_ssh_bruteforce(self, logs):
        """
        Detect multiple failed SSH login attempts from same IP
        """

        failed_attempts = defaultdict(int)
        alerts = []

        for log in logs:
            if log.get("event") == "Failed password":

                ip = log.get("ip")
                failed_attempts[ip] += 1


        for ip, count in failed_attempts.items():

            if count >= self.failed_threshold:

                alerts.append({
                    "threat": "SSH Brute Force",
                    "severity": "HIGH",
                    "source_ip": ip,
                    "attempts": count,
                    "risk_score": self.calculate_risk(count)
                })


        return alerts

    def detect_web_attacks(self, logs):
        """
        Detect common web attacks
        """

        alerts = []

        for log in logs:

            if log.get("log_type") != "apache":
                continue

            url = log.get("url", "")
            status = log.get("status", "")
            ip = log.get("ip")

            if "UNION" in log.get("url", "").upper():
                alerts.append({
                    "threat": "SQL Injection Attempt",
                    "severity": "HIGH",
                    "source_ip": log.get("ip"),
                    "url": log.get("url"),
                    "status": "200"
                })

            if "/admin" in url and status == "403":
                alerts.append({
                    "threat": "Admin Page Access Attempt",
                    "severity": "MEDIUM",
                    "source_ip": ip,
                    "url": url,
                    "status": status
                })

            elif status == "401":
                alerts.append({
                    "threat": "Failed Web Login",
                    "severity": "LOW",
                    "source_ip": ip,
                    "url": url,
                    "status": status
                })

        return alerts


    def calculate_risk(self, attempts):
        """
        Calculate risk score
        """

        if attempts >= 10:
            return 100

        elif attempts >= 5:
            return 75

        elif attempts >= 3:
            return 50

        else:
            return 25


    def detect_suspicious_ips(self, logs):
        """
        Detect IPs with abnormal activity
        """

        activity = defaultdict(int)
        suspicious = []

        for log in logs:

            ip = log.get("ip")

            if ip:
                activity[ip] += 1


        for ip, count in activity.items():

            if count >= 3:

                suspicious.append({
                    "ip": ip,
                    "activity_count": count,
                    "status": "Suspicious"
                })


        return suspicious
