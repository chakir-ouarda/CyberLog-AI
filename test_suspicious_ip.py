from src.parser.parser import LogParser
from src.detection.detector import DetectionEngine


parser = LogParser("logs/input/auth.log")

logs = parser.parse_file()


detector = DetectionEngine()


result = detector.detect_suspicious_ips(logs)


print(result)
