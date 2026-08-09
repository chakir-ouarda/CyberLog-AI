import sys
import os
from datetime import datetime
import sqlite3

sys.path.append(os.path.abspath(".."))

from flask import Flask, render_template, jsonify, request, redirect, abort
from services.database_service import get_incidents, get_audit_logs, get_mttr
from src.reporting.timeline import AttackTimeline

app = Flask(__name__)


@app.route("/")
def dashboard():

    incidents = get_incidents()

    audit_logs = get_audit_logs()

    mttr = get_mttr()

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
        avg_risk=avg_risk,
        audit_logs=audit_logs,
        mttr=mttr
    )


@app.route("/api/incidents")
def api_incidents():

    incidents = get_incidents()

    return jsonify(
        [dict(i) for i in incidents]
    )

@app.route("/api/attack-statistics")
def attack_statistics():

    incidents = get_incidents()

    statistics = {}

    for incident in incidents:

        category = (
            incident.get("category")
            or incident.get("ioc", {}).get("attack_category")
            or "UNKNOWN"
        )

        statistics[category] = (
            statistics.get(category, 0) + 1
        )

    return jsonify({
        "labels": list(statistics.keys()),
        "data": list(statistics.values())
    })

@app.route("/api/incident-trends")
def incident_trends():

    incidents = get_incidents()

    trends = {}

    for incident in incidents:

        created_at = incident.get("created_at")

        if not created_at:
            continue

        date = created_at.split(" ")[0]

        if date not in trends:
            trends[date] = 0

        trends[date] += 1

    return jsonify({
        "labels": list(trends.keys()),
        "data": list(trends.values())
    })

@app.route("/incident/<int:incident_id>", methods=["GET", "POST"])
def incident_details(incident_id):

    incidents = get_incidents()

    incident = next(
        (i for i in incidents if i["id"] == incident_id),
        None
    )

    if incident is None:
        abort(404)

    old_status = incident["status"]

    if request.method == "POST":

        status = request.form.get("status")
        assigned_to = request.form.get("assigned_to")
        investigation_notes = request.form.get("investigation_notes")
        resolved_at = None

        if status == "RESOLVED":
            resolved_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("../database/cyberlog.db")

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE incidents
            SET status = ?,
                assigned_to = ?,
                investigation_notes = ?,
                resolved_at = ?
            WHERE id = ?
            """,
            (
                status,
                assigned_to,
                investigation_notes,
                resolved_at,
                incident_id
            )
        )

        if old_status != status:

            cursor.execute(
                """
                INSERT INTO audit_logs
                (
                    incident_id,
                    username,
                    action,
                    old_status,
                    new_status,
                    details,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    incident_id,
                    assigned_to,
                    "UPDATE_STATUS",
                    old_status,
                    status,
                    "Incident status updated",
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            )

        conn.commit()

        conn.close()

        return redirect(f"/incident/{incident_id}")

    conn = sqlite3.connect("../database/cyberlog.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, incident_id, username, action,
               old_status, new_status, details, created_at
        FROM audit_logs
        WHERE incident_id = ?
        ORDER BY id DESC
        """,
        (incident_id,)
    )

    audit_logs = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return render_template(
        "incident.html",
        incident=incident,
        audit_logs=audit_logs
    )

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
