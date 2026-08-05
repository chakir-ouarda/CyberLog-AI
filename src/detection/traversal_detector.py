import re


class TraversalDetector:


    def __init__(self):

        self.patterns = [

            r"\.\./",
            r"\.\.\\",
            r"/etc/passwd",
            r"/etc/shadow",
            r"boot\.ini",
            r"windows/win\.ini"

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

                        "threat": "Path Traversal Attempt",
                        "severity": "HIGH",
                        "source_ip": ip,
                        "url": url,
                        "type": "WEB_ATTACK",
                        "attack_category": "PATH_TRAVERSAL"

                    })

                    break


        return alerts
