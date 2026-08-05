from collections import defaultdict


class SSHDetector:

    def __init__(self, failed_threshold=3):
        self.failed_threshold = failed_threshold


    def detect(self, logs):

        failed_attempts = defaultdict(int)
        alerts = []


        for log in logs:

            if (
                log.get("log_type") == "ssh"
                and log.get("event") == "Failed password"
            ):

                ip = log.get("ip")
                failed_attempts[ip] += 1


        for ip, count in failed_attempts.items():

            if count >= self.failed_threshold:

                alerts.append({
                    "threat": "SSH Brute Force",
                    "severity": "HIGH",
                    "source_ip": ip,
                    "attempts": count,
                    "type": "SSH_ATTACK"
                })


        return alerts
