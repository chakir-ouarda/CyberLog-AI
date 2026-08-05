class ThreatDatabase:

    def __init__(self):

        self.malicious_ips = {

            "192.168.1.10": {
                "confidence": "HIGH",
                "source": "CyberLog AI Threat DB"
            },

            "192.168.1.50": {
                "confidence": "HIGH",
                "source": "CyberLog AI Threat DB"
            },

            "10.10.10.5": {
                "confidence": "MEDIUM",
                "source": "CyberLog AI Threat DB"
            }

        }

    def lookup_ip(self, ip):

        if ip in self.malicious_ips:

            return {
                "malicious": True,
                "confidence": self.malicious_ips[ip]["confidence"],
                "source": self.malicious_ips[ip]["source"]
            }

        return {
            "malicious": False
        }
