import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "cyberlog.db")


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        incident TEXT,
        source_ip TEXT,
        severity TEXT,
        risk_score INTEGER,

        category TEXT,

        mitre TEXT,

        confidence TEXT,

        analysis TEXT,

        recommendations TEXT,

        ioc TEXT,

        threat_intelligence TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def clear_incidents():
    conn = get_connection()
    conn.execute("DELETE FROM incidents")
    conn.commit()
    conn.close()


def insert_incident(incident):
    conn = get_connection()

    conn.execute("""
    INSERT INTO incidents (
        incident,
        source_ip,
        severity,
        risk_score,
        category,
        mitre,
        confidence
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        incident.get("incident"),
        incident.get("source_ip"),
        incident.get("severity"),
        incident.get("risk_score"),
        incident.get("ioc", {}).get("attack_category"),
        incident.get("mitre", {}).get("technique_id"),
        incident.get("threat_intelligence", {}).get("confidence")
    ))

    conn.commit()
    conn.close()


def get_incidents():
    conn = get_connection()

    rows = conn.execute("""
        SELECT *
        FROM incidents
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    return [dict(row) for row in rows]


if __name__ == "__main__":
    init_database()
    print("Database initialized successfully.")
