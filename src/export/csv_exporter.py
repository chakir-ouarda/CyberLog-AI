import csv
from pathlib import Path


class CSVExporter:

    def __init__(self, output_dir="reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def export_iocs(self, analyses):

        file_path = self.output_dir / "iocs.csv"

        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "Source IP",
                "URL",
                "Attack Category",
                "Log Type",
                "Risk Score",
                "Severity"
            ])

            for analysis in analyses:

                ioc = analysis.get("ioc", {})

                writer.writerow([
                    ioc.get("source_ip"),
                    ioc.get("url"),
                    ioc.get("attack_category"),
                    ioc.get("log_type"),
                    analysis.get("risk_score"),
                    analysis.get("severity")
                ])

        return file_path
