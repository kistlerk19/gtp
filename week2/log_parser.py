import re
from datetime import datetime

class LogParser:
    def __init__(self, severity_levels=None):
        """Initialize with severity levels to track.
        
        Args:
            severity_levels: List of severity levels to extract (default: ["ERROR", "CRITICAL"])
        """
        self.severity_levels = severity_levels or ["ERROR", "CRITICAL"]
        
    def extract_critical_logs(self, log_content):
        """Extract logs matching critical severity levels.
        
        Args:
            log_content: String containing log entries
            
        Returns:
            List of log lines containing critical entries
        """
        critical_logs = []
        
        for line in log_content.splitlines():
            if any(level in line for level in self.severity_levels):
                critical_logs.append(line)
                
        return critical_logs
    
    def parse_log(self, log_path):
        """Parse log file and extract critical entries.
        
        Args:
            log_path: Path to the log file
            
        Returns:
            List of critical log entries
        """
        try:
            with open(log_path, 'r') as f:
                log_content = f.read()
            return self.extract_critical_logs(log_content)
        except FileNotFoundError:
            print(f"Error: Log file '{log_path}' not found")
            return []