from datetime import datetime


class AttackTimeline:

    def generate(self, incidents):
        timeline = []

        for incident in incidents:
            timeline.append({
                "time": datetime.now().strftime("%H:%M:%S"),
                "incident": incident.get("incident"),
                "severity": incident.get("severity"),
                "source_ip": incident.get("source_ip")
            })

        return timeline
