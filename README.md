# CyberLog AI

Intelligent Security Log Analyzer

CyberLog AI is a Blue Team, SOC automation, and threat intelligence platform designed to analyze security logs, detect suspicious activity, assess incident risk, extract Indicators of Compromise (IOCs), map attacks to MITRE ATT&CK, enrich incidents with threat intelligence, and generate security reports through an interactive SOC dashboard.

The project provides a practical Security Operations Center environment for security monitoring, incident analysis, investigation, threat detection, and automated reporting.

## Project Goal

CyberLog AI transforms raw security logs into structured and actionable security incidents.

text
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
      +---- IOC Extraction
      |
      +---- MITRE ATT&CK Mapping
      |
      +---- Threat Intelligence
      |
      v
Security Reports
      |
      v
SOC Dashboard


## Features

### Security Log Analysis

CyberLog AI parses security-related log files and converts raw log entries into structured events.

Supported log sources include:

- SSH authentication logs
- Web server logs
- System logs

The parser extracts information such as:

- Timestamp
- Hostname
- Process
- Process ID
- Username
- Source IP
- Port
- Protocol
- Event type
- Log type

### Threat Detection

The detection engine identifies suspicious activity using security detection rules.

Current detection capabilities include:

- SSH Brute Force
- Failed Web Login
- Admin Page Access Attempt
- SQL Injection Attempt
- XSS
- Path Traversal

Detected events are converted into structured security incidents.

### Risk Analysis

CyberLog AI evaluates detected incidents using risk scoring and severity classification.

Supported severity levels:

- LOW
- MEDIUM
- HIGH
- CRITICAL

Each incident can contain:

- Threat name
- Severity
- Risk score
- Source IP
- Attack category
- Detection information
- Security analysis
- Recommended actions

### IOC Extraction

The platform extracts Indicators of Compromise from detected incidents.

Supported IOC information includes:

- Source IP addresses
- URLs
- Attack categories
- Log types
- HTTP information
- Usernames when available

IOC information can be exported as CSV for further analysis.

### MITRE ATT&CK Mapping

Detected incidents can be mapped to MITRE ATT&CK techniques and tactics.

Examples include:

- T1110 — Brute Force
- T1190 — Exploit Public-Facing Application
- T1083 — File and Directory Discovery

MITRE information is displayed directly within the SOC dashboard.

### Threat Intelligence

CyberLog AI provides local threat intelligence enrichment for detected incidents.

Threat intelligence information can include:

- Reputation
- Confidence
- Intelligence source
- Malicious or clean classification

The current implementation uses a local threat intelligence database and analysis logic.

## SOC Dashboard

CyberLog AI includes a Flask-based SOC dashboard designed to provide centralized visibility into security incidents.

The dashboard provides:

- SOC system status
- Incident overview
- Severity distribution
- Risk statistics
- Incident trends
- Attack statistics
- Incident investigation
- IOC visualization
- MITRE ATT&CK information
- Threat intelligence
- Audit logs
- Mean Time To Resolution (MTTR)
- Recent SOC activity

### Current Dashboard Status

The dashboard monitors the status of the main CyberLog AI components:

- Log Parser
- Threat Detection Engine
- AI Analyzer
- Report Generator

The dashboard also displays:

- Total incidents
- Critical incidents
- High severity incidents
- Medium severity incidents
- Average risk score
- Mean Time To Resolution

## Incident Management

CyberLog AI provides an incident investigation workflow for SOC analysis.

Analysts can:

- View incident details
- Assign incidents
- Change incident status
- Add investigation notes
- Mark incidents as resolved
- Review investigation history

Supported incident states:

- NEW
- INVESTIGATING
- RESOLVED

Status changes are recorded in the audit log.

## Audit Logs

The platform records incident status changes and investigation activity.

Audit information includes:

- Timestamp
- Analyst
- Action
- Previous status
- New status
- Investigation details

This provides a basic audit trail for SOC investigation workflows.

## Mean Time To Resolution

CyberLog AI calculates Mean Time To Resolution (MTTR) for resolved incidents.

The calculation follows this workflow:

text
Incident Creation Time
        |
        v
Incident Resolution Time
        |
        v
Resolution Duration
        |
        v
Average MTTR


MTTR is displayed directly in the SOC dashboard.

## Attack Statistics

The dashboard provides attack statistics based on detected incident categories.

This allows analysts to identify the most frequently detected attack types and understand the distribution of security events.

## Incident Trends

CyberLog AI provides incident trend visualization based on incident creation dates.

This helps analysts understand:

- Incident frequency
- Detection activity
- Changes in attack volume
- Security event distribution over time

## Security Reports

CyberLog AI generates multiple security report formats.

Supported outputs include:

- JSON
- HTML
- PDF
- CSV IOC reports
- Sigma rules
- YARA rules
- STIX exports

Generated reports are stored in the reports/ directory.

Example outputs:

text
reports/security_report.json
reports/security_report.html
reports/security_report.pdf
reports/iocs.csv
reports/sigma/ssh_brute_force.yml
reports/yara/ssh_brute_force.yar
reports/stix/ssh_brute_force_stix.json


## Testing

The project has been validated through manual component smoke tests and pipeline execution.

Tested components include:

- Log parser
- Threat detection engine
- AI analyzer
- Web attack detection
- Security report generation
- PDF report generation
- Main processing pipeline
- Python compilation

The project also passes Python compilation checks:

bash
python3 -m compileall -q dashboard src main.py realtime


The current test scripts are primarily manual smoke-test scripts rather than a pytest-based automated test suite.

## Project Structure

```text
CyberLog-AI/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
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
│
├── database/
│   └── database.py
│
├── logs/
│   └── input/
│       ├── apache.log
│       ├── auth.log
│       └── syslog
│
├── realtime/
│   ├── pipeline.py
│   ├── watcher.py
│   └── ...
│
├── reports/
│   ├── iocs.csv
│   ├── security_report.html
│   ├── security_report.pdf
│   ├── sigma/
│   ├── yara/
│   └── stix/
│
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
│
└── tests/
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application and security analysis |
| Flask | SOC Dashboard and API |
| SQLite | Incident and audit-log storage |
| JavaScript | Dashboard interactivity |
| Chart.js | Security analytics and charts |
| ReportLab | PDF report generation |
| MITRE ATT&CK | Attack technique and tactic mapping |
| Sigma | Detection rule generation |
| YARA | Security rule generation |
| STIX | Threat intelligence data export |
| Git | Version control |

## Installation

Clone the repository:

bash
git clone https://github.com/chakir-ouarda/CyberLog-AI.git
cd CyberLog-AI


Create a Python virtual environment:

bash
python3 -m venv .venv


Activate the virtual environment:

bash
source .venv/bin/activate


Install the required dependencies:

bash
pip install -r requirements.txt


## Usage

Run the main security analysis pipeline:

bash
python3 main.py


The pipeline performs:

text
Load Logs
   |
   v
Parse Logs
   |
   v
Detect Threats
   |
   v
Analyze Incidents
   |
   v
Generate Reports


Start the SOC dashboard:

bash
python3 dashboard/app.py


The dashboard is available locally at:

text
http://127.0.0.1:5000


## Example Detection Results

Example incidents detected by CyberLog AI include:

| Incident | Severity | Risk Score |
|---|---|---:|
| SQL Injection Attempt | CRITICAL | 95 |
| SSH Brute Force | HIGH | 85 |
| Admin Page Access Attempt | MEDIUM | 55 |
| Failed Web Login | MEDIUM | 40 |

These examples are intended for demonstration and security testing purposes.

## Security Scope

CyberLog AI is designed for defensive cybersecurity and security research purposes.

The project is intended for:

- SOC training
- Blue Team laboratories
- Security monitoring
- Security log analysis
- Incident investigation
- Threat detection research
- Security automation
- Cybersecurity education

The included logs and indicators are intended for testing and demonstration purposes.

## Roadmap

### v1.0 — Core Security Pipeline

Completed:

- Log parsing
- Threat detection
- Risk analysis
- MITRE mapping
- IOC extraction
- Security reports

### v2.0 — SOC Platform

Completed:

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

### v3.0 — Advanced AI Security

Planned future enhancements:

- Ollama integration
- Qwen-based security analysis
- RAG knowledge base
- Advanced AI incident investigation
- Automated incident summarization
- Context-aware threat intelligence
- AI-assisted SOC recommendations

## Project Status

CyberLog AI v2.0 is completed and operational.

The current version has been validated through:

- Manual component smoke tests
- Main pipeline execution
- Security report generation
- PDF report generation
- Dashboard verification
- Python compilation checks
- Git version control

The project is currently available on GitHub.

## Author

Chakir Ouarda

Cybersecurity Graduate
Interested in SOC Analysis, Blue Team, Security Automation and Threat Intelligence.

## Connect

LinkedIn: https://www.linkedin.com/in/chakir-ouarda

GitHub: https://github.com/chakir-ouarda

## License

This project is intended for educational, research, and defensive cybersecurity purposes.
