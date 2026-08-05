from src.parser.parser import LogParser
from src.detection.detector import DetectionEngine


parser = LogParser("logs/input/auth.log")

logs = parser.parse_file()


detector = DetectionEngine(failed_threshold=2)


alerts = detector.detect_ssh_bruteforce(logs)


print(alerts)
