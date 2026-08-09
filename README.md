CyberLog AI

Intelligent Security Log Analyzer

CyberLog AI is a Blue Team, SOC automation, and threat intelligence platform designed to analyze security logs, detect suspicious activity, assess incident risk, extract Indicators of Compromise (IOCs), map attacks to MITRE ATT&CK, enrich incidents with threat intelligence, and generate security reports through an interactive SOC dashboard.

The project provides a practical Security Operations Center (SOC) environment for security monitoring, incident analysis, investigation, and automated reporting.

Project Goal

CyberLog AI transforms raw security logs into structured and actionable security incidents.

Security Logs
     |
     v
Log Parser
     |
     v
Threat Detection Engine
     |
     v
Risk Engine / AI Analyzer
     |
     +-- IOC Extraction
     +-- MITRE ATT&CK Mapping
     +-- Threat Intelligence
     |
     v
Security Reports
     |
     v
SOC Dashboard

Features

Security Log Analysis

- Parse authentication and web server logs
- Extract structured security events
- Support SSH and web attack detection
- Convert raw log entries into normalized security events

Threat Detection

The detection engine currently identifies attacks such as:

- SSH Brute Force
- Failed Web Login
- Admin Page Access Attempt
- SQL Injection
- XSS
- Path Traversal
- Other suspicious web activity

Risk Analysis

Each detected incident receives a risk score and severity classification.

Threat| Severity| Risk Score
SQL Injection Attempt| CRITICAL| 95
SSH Brute Force| HIGH| 85
Admin Page Access Attempt| MEDIUM| 55
Failed Web Login| MEDIUM| 40

MITRE ATT&CK Mapping

CyberLog AI maps detected incidents to MITRE ATT&CK techniques.

Incident| Technique| ID| Tactic
SQL Injection Attempt| Exploit Public-Facing Application| T1190| Initial Access
SSH Brute Force| Brute Force| T1110| Credential Access
Admin Page Access Attempt| File and Directory Discovery| T1083| Discovery

IOC Extraction

The platform extracts Indicators of Compromise from detected incidents.

Currently supported IOC information includes:

- Source IP
- URL
- Username
- HTTP Method
- HTTP Status Code
- Attack Category
- Log Type

Example:

Source IP:       192.168.1.50
URL:             /login.php?id=1%20UNION%20SELECT%20password%20FROM%20users
Attack Category: SQL_INJECTION
Log Type:        WEB_ATTACK

Threat Intelligence

CyberLog AI includes a local Threat Intelligence layer that enriches detected incidents with:

- Malicious or Clean reputation
- Confidence level
- Threat intelligence source
- Incident context

SOC Dashboard

The project includes a Flask-based SOC dashboard providing a centralized view of security activity.

Dashboard capabilities include:

- SOC system status
- Total incidents
- Critical, High, Medium, and Low severity
- Average risk score
- Mean Time To Resolution
- Incident management
- Incident investigation
- Analyst assignment
- Investigation notes
- Incident status management
- Audit logs
- Attack timeline
- IOC overview
- MITRE ATT&CK mapping
- Threat Intelligence
- Severity distribution
- Incident trends
- Attack statistics
- Recent SOC activity

Current Dashboard Status

SOC ONLINE

Log Parser                ONLINE
Threat Detection Engine  ONLINE
AI Analyzer              ONLINE
Report Generator         ONLINE

Current test environment:

Total Incidents:       5
Critical Severity:     2
High Severity:         1
Medium Severity:       2
Average Risk:          75
MTTR:                  672.6 min

Incident Management

Each incident can be investigated through a dedicated incident page.

The analyst can manage:

- Incident status
- Assigned analyst
- Investigation notes
- Resolution timestamp
- Investigation history

Supported statuses:

NEW
INVESTIGATING
RESOLVED

Changes to incident status are recorded through the SOC audit log.

Security Reports

CyberLog AI automatically generates multiple security report formats:

JSON
HTML
PDF
CSV
Sigma
YARA
STIX

Examples:

reports/security_report.json
reports/security_report.html
reports/security_report.pdf
reports/iocs.csv

reports/sigma/ssh_brute_force.yml
reports/yara/ssh_brute_force.yar
reports/stix/ssh_brute_force_stix.json

Testing

The project includes manual smoke tests for the main components.

python3 test_parser.py
python3 test_detection.py
python3 test_ai.py
python3 test_report.py
python3 test_pdf_report.py
python3 test_web_detection.py

The complete security analysis pipeline can be executed with:

python3 main.py

Example output:

[+] Loading logs...
[+] Parsed logs: 13
[+] Detecting threats...
[+] Threats detected: 4
[+] AI analyzing incidents...
[+] Generating report...

CyberLog AI completed successfully

The project also passes Python compilation checks:

python3 -m compileall -q dashboard src main.py realtime

Project Structure

CyberLog-AI/
|
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
|
├── dashboard/
│   ├── app.py
│   ├── services/
│   │   └── database_service.py
│   ├── static/
│   │   ├── charts.js
│   │   ├── dashboard.js
│   │   └── style.css
│   └── templates/
│       ├── index.html
│       └── incident.html
|
├── database/
│   └── database.py
|
├── logs/
│   └── input/
│       ├── apache.log
│       ├── auth.log
│       └── syslog
|
├── realtime/
│   ├── pipeline.py
│   ├── watcher.py
│   └── ...
|
├── reports/
│   ├── iocs.csv
│   ├── security_report.html
│   ├── security_report.pdf
│   ├── sigma/
│   ├── yara/
│   └── stix/
|
├── src/
│   ├── ai/
│   ├── detection/
│   ├── export/
│   ├── ioc/
│   ├── mitre/
│   ├── parser/
│   ├── reporting/
│   ├── threat_intel/
│   └── utils/
|
└── tests/

Technology Stack

Technology| Purpose
Python| Core application and security analysis
Flask| SOC Dashboard and API
SQLite| Incident and audit-log storage
JavaScript| Dashboard interactivity
Chart.js| Security analytics and charts
ReportLab| PDF report generation
MITRE ATT&CK| Attack technique mapping
Sigma| Detection rule generation
YARA| Detection rule generation
STIX| Threat intelligence export
Git| Version control
Kali Linux| Development and security environment

Installation

Clone the repository:

git clone https://github.com/chakir-ouarda/CyberLog-AI.git
cd CyberLog-AI

Create a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Usage

Run the main security analysis pipeline:

python3 main.py

Start the SOC Dashboard:

python3 dashboard/app.py

Then open:

http://127.0.0.1:5000

Security Scope

CyberLog AI is designed for:

- Defensive security monitoring
- SOC training
- Blue Team laboratories
- Security log analysis
- Incident investigation
- Threat detection research
- Security automation

The included logs and indicators are intended for testing and demonstration purposes.

Roadmap

v1.0 - Core Security Pipeline

- Log parsing
- Threat detection
- Risk analysis
- MITRE mapping
- IOC extraction
- Security reports

v2.0 - SOC Platform

- SOC Dashboard
- Incident Management
- Investigation workflow
- Analyst assignment
- Investigation notes
- Audit Logs
- MTTR
- Attack Statistics
- Incident Trends
- Threat Intelligence
- IOC visualization
- MITRE ATT&CK visualization

v3.0 - Advanced AI Security

Planned future enhancements:

- Ollama integration
- Qwen-based security analysis
- RAG knowledge base
- Advanced AI incident investigation
- Automated incident summarization
- Context-aware threat intelligence
- AI-assisted SOC recommendations

Project Status

CyberLog AI v2.0 is completed and operational.

The current version has been tested through:

- Manual component smoke tests
- Main pipeline execution
- Report generation
- Dashboard verification
- Python compilation checks
- Git version control

Author

Chakir Ouarda

Cybersecurity Graduate

Interested in SOC Analysis, Blue Team, Security Automation and Threat Intelligence.

Connect

- LinkedIn: https://www.linkedin.com/in/chakir-ouarda
- GitHub: https://github.com/chakir-ouarda
- Project: https://github.com/chakir-ouarda/CyberLog-AI

License

This project is intended for educational, research, and defensive cybersecurity purposes.
