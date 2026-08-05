import re


class CommandDetector:


    def __init__(self):

        self.patterns = [

            r";\s*(ls|cat|whoami|id|uname|pwd)",
            r"\|\s*(ls|cat|whoami|id|uname|pwd)",
            r"&&\s*(ls|cat|whoami|id|uname|pwd)",
            r"\$\(",
            r"`[^`]+`"

        ]


    def detect(self, logs):

        alerts = []


        for log in logs:

            if log.get("log_type") != "apache":
                continue


            url = log.get("url", "")
            ip = log.get("ip")


            for pattern in self.patterns:

                if re.search(pattern, url, re.IGNORECASE):

                    alerts.append({

                        "threat": "Command Injection Attempt",
                        "severity": "CRITICAL",
                        "source_ip": ip,
                        "url": url,
                        "type": "WEB_ATTACK",
                        "attack_category": "COMMAND_INJECTION"

                    })

                    break


        return alerts
