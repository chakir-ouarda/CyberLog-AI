class WebDetector:


    def detect(self, logs):

        alerts = []


        for log in logs:

            if log.get("log_type") != "apache":
                continue


            url = log.get("url", "")
            status = log.get("status", "")
            ip = log.get("ip")


            if "/admin" in url and status == "403":

                alerts.append({
                    "threat": "Admin Page Access Attempt",
                    "severity": "MEDIUM",
                    "source_ip": ip,
                    "url": url,
                    "type": "WEB_ATTACK"
                })


            elif status == "401":

                alerts.append({
                    "threat": "Failed Web Login",
                    "severity": "LOW",
                    "source_ip": ip,
                    "url": url,
                    "type": "WEB_ATTACK"
                })


        return alerts
