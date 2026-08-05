from src.ai.analyzer import AIAnalyzer


alert = {
    "threat": "SSH Brute Force",
    "severity": "HIGH",
    "source_ip": "192.168.1.10",
    "attempts": 3,
    "risk_score": 50
}


analyzer = AIAnalyzer()


result = analyzer.analyze(alert)


print(result)
