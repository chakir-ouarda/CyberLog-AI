import sys
import os

sys.path.append(os.path.abspath(".."))

from flask import Flask, render_template, jsonify
from services.database_service import get_incidents
from src.reporting.timeline import AttackTimeline

app = Flask(__name__)


@app.route("/")
def dashboard():

    incidents = get_incidents()

    total = len(incidents)

    critical = len(
        [i for i in incidents if i["severity"] == "CRITICAL"]
    )

    high = len(
        [i for i in incidents if i["severity"] == "HIGH"]
    )

    medium = len(
        [i for i in incidents if i["severity"] == "MEDIUM"]
    )

    low = len(
        [i for i in incidents if i["severity"] == "LOW"]
    )


    avg_risk = 0

    if total:
        avg_risk = int(
            sum(i["risk_score"] for i in incidents) / total
        )


    top_threats = sorted(
        incidents,
        key=lambda x: x["risk_score"],
        reverse=True
    )

    timeline = AttackTimeline().generate(incidents)


    return render_template(
        "index.html",
        incidents=incidents,
        top_threats=top_threats,
        timeline=timeline,
        ioc_data=incidents,
        mitre_data=incidents,
        total=total,
        critical=critical,
        high=high,
        medium=medium,
        low=low,
        avg_risk=avg_risk
    )


@app.route("/api/incidents")
def api_incidents():

    incidents = get_incidents()

    return jsonify(
        [dict(i) for i in incidents]
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
