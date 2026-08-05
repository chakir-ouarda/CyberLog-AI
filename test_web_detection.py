from src.parser.parser import LogParser
from src.detection.detector import DetectionEngine

parser = LogParser("logs/input/apache.log")
logs = parser.parse_file()

detector = DetectionEngine()

alerts = detector.detect_web_attacks(logs)

print(f"Web attacks found: {len(alerts)}")

for alert in alerts:
    print(alert)
