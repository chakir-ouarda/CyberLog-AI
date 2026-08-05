from src.parser.parser import LogParser


parser = LogParser("logs/input/auth.log")


line = "Jul 30 18:22:51 ubuntu sshd[12345]: Failed password for root from 192.168.1.10 port 53214 ssh2"


result = parser.parse_line(line)


print(result)
