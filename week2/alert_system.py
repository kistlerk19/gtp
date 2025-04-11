class AlertSystem:
    def __init__(self, threshold=5):
        """Initialize with alert threshold.
        
        Args:
            threshold: Number of errors that trigger an alert (default: 5)
        """
        self.threshold = threshold
        
    def save_alerts(self, alerts, output_path):
        """Save alert logs to output file.
        
        Args:
            alerts: List of alert messages
            output_path: Path to save the alerts
            
        Returns:
            Boolean indicating success
        """
        try:
            with open(output_path, 'w') as f:
                for alert in alerts:
                    f.write(f"{alert}\n")
            return True
        except Exception as e:
            print(f"Error saving alerts: {e}")
            return False
            
    def check_threshold(self, alerts):
        """Check if alerts exceed threshold.
        
        Args:
            alerts: List of alert messages
            
        Returns:
            Boolean indicating if threshold was exceeded
        """
        return len(alerts) > self.threshold
        
    def send_notification(self, alert_count):
        """Send notification when threshold exceeded.
        
        Args:
            alert_count: Number of alerts detected
            
        Returns:
            Notification message
        """
        message = f"ALERT: {alert_count} critical errors detected, exceeding threshold of {self.threshold}"
        print(message)
        return message