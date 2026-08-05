from src.parser.parser import LogParser
from src.detection.engine import DetectionEngine
from src.ai.analyzer import AIAnalyzer
from src.reporting.report_generator import ReportGenerator
from src.reporting.timeline import AttackTimeline
from src.export.csv_exporter import CSVExporter
from src.export.sigma_generator import SigmaGenerator
from src.export.yara_generator import YaraGenerator
from src.export.stix_exporter import STIXExporter

def main():

    ssh_log = "logs/input/auth.log"
    apache_log = "logs/input/apache.log"


    print("[+] Loading logs...")

    ssh_parser = LogParser(ssh_log)
    apache_parser = LogParser(apache_log)

    ssh_logs = ssh_parser.parse_file()
    apache_logs = apache_parser.parse_file()

    logs = ssh_logs + apache_logs


    print(f"[+] Parsed logs: {len(logs)}")


    print("[+] Detecting threats...")

    detector = DetectionEngine()

    alerts = detector.detect(logs)


    if not alerts:
        print("[+] No threats detected")
        return


    print(f"[+] Threats detected: {len(alerts)}")


    print("[+] AI analyzing incidents...")

    analyzer = AIAnalyzer()

    analyzed_reports = []

    for alert in alerts:

        analysis = analyzer.analyze(alert)

        analyzed_reports.append(analysis)

    timeline = AttackTimeline()
    attack_timeline = timeline.generate(analyzed_reports)



    print("[+] Generating report...")

    generator = ReportGenerator()
    csv_exporter = CSVExporter()
    sigma_generator = SigmaGenerator()
    yara_generator = YaraGenerator()
    stix_exporter = STIXExporter()

    json_file = generator.generate_json_report(
    analyzed_reports,
    attack_timeline
    )


    html_file = generator.generate_html_report(
    analyzed_reports[0]
    )

    pdf_file = generator.generate_pdf_report(
    analyzed_reports[0]
    )

    sigma_file = sigma_generator.generate(analyzed_reports[0])

    yara_file = yara_generator.generate(analyzed_reports[0])

    stix_file = stix_exporter.generate(analyzed_reports[0])

    csv_file = csv_exporter.export_iocs(analyzed_reports)


    print("\nCyberLog AI completed successfully")
    print("JSON Report:", json_file)
    print("HTML Report:", html_file)
    print("PDF Report :", pdf_file)
    print("Sigma Rule :", sigma_file)
    print(f"YARA Rule  : {yara_file}")
    print(f"STIX Export: {stix_file}")
    print("CSV Report :", csv_file)



if __name__ == "__main__":
    main()
