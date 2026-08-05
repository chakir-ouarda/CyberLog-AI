from pathlib import Path


class YaraGenerator:

    def __init__(self, output_dir="reports/yara"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, analysis):

        incident = analysis.get("incident", "Unknown")
        source_ip = analysis.get("source_ip", "")
        attack = (
            analysis.get("ioc", {})
            .get("attack_category", "")
        )

        file_name = (
            incident.lower()
            .replace(" ", "_")
            .replace("/", "_")
            + ".yar"
        )

        file_path = self.output_dir / file_name

        yara_rule = f'''rule {incident.replace(" ", "_")}
{{
    meta:
        author = "CyberLog AI"
        description = "Automatically generated YARA rule"
        severity = "{analysis.get("severity", "LOW")}"

    strings:
        $ip = "{source_ip}"
        $attack = "{attack}"

    condition:
        any of them
}}
'''

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(yara_rule)

        return file_path
