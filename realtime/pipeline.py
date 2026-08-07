import json
import sys
import os

sys.path.append(os.path.abspath(".."))

from src.parser.parser import LogParser
from src.detection.engine import DetectionEngine
from src.ai.analyzer import AIAnalyzer
from src.reporting.report_generator import ReportGenerator
from src.reporting.timeline import AttackTimeline
from database.database import get_connection

SSH_LOG = "../logs/input/auth.log"
APACHE_LOG = "../logs/input/apache.log"

def save_incidents(reports):

    conn = get_connection()

    conn.execute("DELETE FROM incidents")

    for report in reports:

        conn.execute(
            """
            INSERT INTO incidents
            (
                incident,
                source_ip,
                severity,
                risk_score,
                category,
                mitre,
                confidence,
                analysis,
                recommendations,
                ioc,
                threat_intelligence
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                report.get("incident"),
                report.get("source_ip"),
                report.get("severity"),
                report.get("risk_score"),
                report.get("ioc", {}).get("attack_category"),
                json.dumps(report.get("mitre", {})),
                report.get("threat_intelligence", {}).get("confidence"),
                report.get("analysis"),
                json.dumps(report.get("recommendations", [])),
                json.dumps(report.get("ioc", {})),
                json.dumps(report.get("threat_intelligence", {}))
            )
        )

    conn.commit()
    conn.close()

    print(f"[+] {len(reports)} incidents saved to database")

def run_pipeline():

    print("[+] Running CyberLog AI Pipeline...")

    ssh_parser = LogParser(SSH_LOG)
    apache_parser = LogParser(APACHE_LOG)

    ssh_logs = ssh_parser.parse_file()
    apache_logs = apache_parser.parse_file()

    logs = ssh_logs + apache_logs

    print(f"[+] Parsed logs: {len(logs)}")


    detector = DetectionEngine()

    alerts = detector.detect(logs)


    print(f"[+] Threats detected: {len(alerts)}")


    if not alerts:
        print("[+] No threats detected")
        return


    analyzer = AIAnalyzer()

    reports = []

    for alert in alerts:
        reports.append(
            analyzer.analyze(alert)
        )

    save_incidents(reports)


    timeline = AttackTimeline()

    attack_timeline = timeline.generate(
        reports
    )


    generator = ReportGenerator()

    generator.generate_json_report(
        reports,
        attack_timeline
    )


    print(
        f"[+] Pipeline completed. {len(reports)} incidents generated."
    )


if __name__ == "__main__":
    run_pipeline()
