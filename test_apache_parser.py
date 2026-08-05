from src.parser.parser import LogParser

parser = LogParser("logs/input/apache.log")

logs = parser.parse_file()

print(f"Total logs: {len(logs)}")

for log in logs:
    print(log)
