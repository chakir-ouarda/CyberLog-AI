import re
from pathlib import Path


class LogParser:

    LOG_PATTERN = re.compile(
        r'^(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+'
        r'(?P<hostname>\S+)\s+'
        r'(?P<process>\w+)\[(?P<pid>\d+)\]:\s+'
        r'(?P<event>Failed password|Accepted password)\s+'
        r'for\s+(?P<username>\S+)\s+from\s+'
        r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+'
        r'port\s+(?P<port>\d+)\s+'
        r'(?P<protocol>\S+)$'
    )

    APACHE_PATTERN = re.compile(
    r'^(?P<ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+'
    r'\[(?P<timestamp>[^\]]+)\]\s+'
    r'"(?P<method>\w+)\s+(?P<url>\S+)\s+\S+"\s+'
    r'(?P<status>\d+)\s+'
    r'(?P<size>\d+)$'
    )

    def __init__(self, log_file):
        self.log_file = Path(log_file)

    def read_logs(self):
        if not self.log_file.exists():
            raise FileNotFoundError(f"Log file not found: {self.log_file}")

        with open(self.log_file, "r", encoding="utf-8", errors="ignore") as file:
            return file.readlines()

    def parse_line(self, line):
        """
        Parse SSH or Apache log line
        """

        line = line.strip()

        ssh_match = self.LOG_PATTERN.match(line)
        if ssh_match:
            data = ssh_match.groupdict()
            data["log_type"] = "ssh"
            return data

        apache_match = self.APACHE_PATTERN.match(line)
        if apache_match:
            data = apache_match.groupdict()
            data["log_type"] = "apache"
            return data

        return None

    def parse_file(self):
        """
        Parse complete log file
        """

        parsed_logs = []

        logs = self.read_logs()

        for line in logs:
            result = self.parse_line(line)

            if result:
                parsed_logs.append(result)

        return parsed_logs
