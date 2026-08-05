import re


class InjectionDetector:


    def __init__(self):

        self.patterns = [

        r"union(\s|%20|\+)+select",
        r"select(\s|%20|\+)+.*(\s|%20|\+)+from",
        r"or(\s|%20|\+)+1\s*=\s*1",
        r"sleep\s*\(",
        r"benchmark\s*\(",
        r"%20union%20",
        r"--",
        r"/\*",
        r"#"

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

                        "threat": "SQL Injection Attempt",
                        "severity": "HIGH",
                        "source_ip": ip,
                        "url": url,
                        "type": "WEB_ATTACK",
                        "attack_category": "SQL_INJECTION"

                    })

                    break


        return alerts
