from src.parser.parser import LogParser


parser = LogParser("logs/input/auth.log")


results = parser.parse_file()


print("Total parsed logs:", len(results))

for log in results:
    print(log)
