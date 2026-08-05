from .ssh_detector import SSHDetector
from .web_detector import WebDetector
from .xss_detector import XSSDetector
from .injection_detector import InjectionDetector
from .traversal_detector import TraversalDetector
from .command_detector import CommandDetector

class DetectionEngine:


    def __init__(self):

        self.detectors = [

        SSHDetector(),
        WebDetector(),
        XSSDetector(),
        InjectionDetector(),
        TraversalDetector(),
        CommandDetector()

    ]


    def detect(self, logs):

        alerts = []


        for detector in self.detectors:

            results = detector.detect(logs)

            alerts.extend(results)


        return alerts
