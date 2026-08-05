class IOCExtractor:

    def extract(self, alert):

        return {

            "source_ip": alert.get("source_ip"),

            "url": alert.get("url"),

            "username": alert.get("username"),

            "http_method": alert.get("method"),

            "status_code": alert.get("status"),

            "attack_category": alert.get("attack_category"),

            "log_type": alert.get("type")

        }
