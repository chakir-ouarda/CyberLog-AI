import sqlite3
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DB_PATH = os.path.join(BASE_DIR, "database", "cyberlog.db")


def get_incidents():

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM incidents ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    incidents = []

    for row in rows:

        incident = dict(row)

        incident["ioc"] = json.loads(
            incident["ioc"] or "{}"
        )

        incident["mitre"] = json.loads(
            incident["mitre"] or "{}"
        )

        incident["threat_intelligence"] = json.loads(
            incident["threat_intelligence"] or "{}"
        )

        incident["recommendations"] = json.loads(
            incident["recommendations"] or "[]"
        )

        incidents.append(incident)

    conn.close()

    return incidents
