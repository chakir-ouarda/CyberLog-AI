import re


class XSSDetector:


    def __init__(self):

        self.patterns = [

            r"<script.*?>",
            r"javascript:",
            r"onerror=",
            r"onload=",
            r"alert\("

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

                        "threat": "Cross Site Scripting (XSS)",
                        "severity": "HIGH",
                        "source_ip": ip,
                        "url": url,
                        "type": "WEB_ATTACK"

                    })

                    break


        return alerts
