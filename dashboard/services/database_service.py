import sqlite3
import json
import os
from datetime import datetime

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


def get_audit_logs(limit=10):

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM audit_logs
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    logs = []

    for row in rows:
        logs.append(dict(row))

    conn.close()

    return logs

def get_mttr():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT created_at, resolved_at
        FROM incidents
        WHERE resolved_at IS NOT NULL
        AND created_at IS NOT NULL
        """
    )

    rows = cursor.fetchall()

    conn.close()

    if not rows:
        return 0

    total_seconds = 0
    valid_incidents = 0

    for created_at, resolved_at in rows:

        try:
            created = datetime.strptime(
                created_at,
                "%Y-%m-%d %H:%M:%S"
            )

            resolved = datetime.strptime(
                resolved_at,
                "%Y-%m-%d %H:%M:%S"
            )

            if resolved >= created:

                total_seconds += (
                    resolved - created
                ).total_seconds()

                valid_incidents += 1

        except (ValueError, TypeError):
            continue

    if valid_incidents == 0:
        return 0

    return round(
        total_seconds / valid_incidents / 60,
        1
    )
