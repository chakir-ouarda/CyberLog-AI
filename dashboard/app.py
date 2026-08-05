from flask import Flask, render_template
import json
import os

app = Flask(__name__)

REPORT_PATH = "../reports/security_report.json"


def load_report():
    with open(REPORT_PATH, "r") as file:
        return json.load(file)


@app.route("/")
def dashboard():

    report = load_report()

    incidents = report.get("data", [])

    total = len(incidents)

    high = len(
        [i for i in incidents if i["severity"] == "HIGH"]
    )
    
    critical = len(
    [i for i in incidents if i["severity"] == "CRITICAL"]
    )

    medium = len(
        [i for i in incidents if i["severity"] == "MEDIUM"]
    )

    low = len(
        [i for i in incidents if i["severity"] == "LOW"]
    )

    avg_risk = int(
        sum(i["risk_score"] for i in incidents) / total
    )

    return render_template(
        "index.html",
        incidents=incidents,
        timeline=report["attack_timeline"],
        mitre_data=incidents,
        ioc_data=incidents,
        total=total,
        critical=critical,
        high=high,
        medium=medium,
        low=low,
        avg_risk=avg_risk
    )


if __name__ == "__main__":
    app.run(debug=True)
