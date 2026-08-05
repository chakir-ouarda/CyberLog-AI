from src.parser.parser import LogParser

parser = LogParser("logs/input/auth.log")

lines = parser.read_logs()

print(f"Total lines: {len(lines)}")

for line in lines:
    print(line.strip())
