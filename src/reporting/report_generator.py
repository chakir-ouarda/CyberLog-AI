import json
from datetime import datetime
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


class ReportGenerator:

    def __init__(self, output_dir="reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)


    def generate_json_report(self, data, timeline=None):
        """
        Generate JSON security report
        """

        report = {
        "report_name": "CyberLog AI Security Report",
        "generated_at": datetime.now().isoformat(),
        "attack_timeline": timeline if timeline else [],
        "data": data
    }


        file_path = self.output_dir / "security_report.json"


        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                report,
                file,
                indent=4,
                ensure_ascii=False
            )


        return file_path

    def generate_html_report(self, data):
        """
        Generate HTML security report
        """

        file_path = self.output_dir / "security_report.html"

        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>CyberLog AI Security Report</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
        }}

        .container {{
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 10px;
        }}

        .high {{
            color: red;
            font-weight: bold;
        }}

        li {{
            margin: 5px;
        }}
    </style>

</head>

<body>

<div class="container">

<h1>CyberLog AI Security Report</h1>

<h2>Incident</h2>
<p>{data.get("incident")}</p>


<h2>Severity</h2>
<p class="high">{data.get("severity")}</p>


<h2>Source IP</h2>
<p>{data.get("source_ip")}</p>


<h2>Risk Score</h2>
<p>{data.get("risk_score")}</p>


<h2>Analysis</h2>
<p>{data.get("analysis")}</p>


<h2>Recommendations</h2>

<ul>
"""

        for item in data.get("recommendations", []):
            html += f"<li>{item}</li>"


        html += """
</ul>

</div>

</body>
</html>
"""


        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html)


        return file_path

    def generate_pdf_report(self, data):
        """
        Generate PDF security report
        """

        file_path = self.output_dir / "security_report.pdf"

        doc = SimpleDocTemplate(
            str(file_path),
            pagesize=letter
        )

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "CyberLog AI Security Report",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 20))

        elements.append(
            Paragraph(
                f"<b>Incident:</b> {data.get('incident')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Severity:</b> {data.get('severity')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Source IP:</b> {data.get('source_ip')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Risk Score:</b> {data.get('risk_score')}",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 15))

        elements.append(
            Paragraph(
                "<b>Analysis</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                data.get("analysis"),
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 15))

        elements.append(
            Paragraph(
                "<b>Recommendations</b>",
                styles["Heading2"]
            )
        )

        for recommendation in data.get("recommendations", []):
            elements.append(
                Paragraph(
                    f"• {recommendation}",
                    styles["Normal"]
                )
            )

        doc.build(elements)

        return file_path
