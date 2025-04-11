import os
import argparse
from log_parser import LogParser
from alert_system import AlertSystem

def monitor_logs(log_path, alert_path, threshold=5):
    """Monitor logs for critical errors and generate alerts.
    
    Args:
        log_path: Path to the log file to monitor
        alert_path: Path to save alert logs
        threshold: Number of errors that trigger alert
        
    Returns:
        Tuple of (alert_count, threshold_exceeded)
    """
    parser = LogParser()
    alert_system = AlertSystem(threshold)
    
    # Extract critical logs
    critical_logs = parser.parse_log(log_path)
    
    # Save alerts to file
    alert_system.save_alerts(critical_logs, alert_path)
    
    # Check threshold and notify if needed
    threshold_exceeded = alert_system.check_threshold(critical_logs)
    if threshold_exceeded:
        alert_system.send_notification(len(critical_logs))
    
    return len(critical_logs), threshold_exceeded

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor server logs for critical errors")
    parser.add_argument("--log", default="server.log", help="Path to server log file")
    parser.add_argument("--alert", default="alerts.log", help="Path to save alerts")
    parser.add_argument("--threshold", type=int, default=5, help="Alert threshold")
    
    args = parser.parse_args()
    
    alert_count, threshold_exceeded = monitor_logs(
        args.log, args.alert, args.threshold
    )
    
    print(f"Found {alert_count} critical log entries")
    if not threshold_exceeded:
        print(f"Threshold of {args.threshold} not exceeded")