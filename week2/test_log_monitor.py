import unittest
import os
import tempfile
from log_parser import LogParser
from alert_system import AlertSystem
from log_monitor import monitor_logs

class TestLogParser(unittest.TestCase):
    def test_extract_critical_logs(self):
        parser = LogParser()
        
        test_logs = """2023-10-15 12:01:23 [INFO] Server started
2023-10-15 12:05:42 [ERROR] Database connection failed
2023-10-15 12:10:15 [INFO] User login
2023-10-15 12:15:33 [CRITICAL] Disk space low
2023-10-15 12:20:11 [WARNING] High memory usage"""
        
        critical_logs = parser.extract_critical_logs(test_logs)
        
        self.assertEqual(len(critical_logs), 2)
        self.assertIn("[ERROR]", critical_logs[0])
        self.assertIn("[CRITICAL]", critical_logs[1])
        
    def test_custom_severity_levels(self):
        parser = LogParser(severity_levels=["WARNING"])
        
        test_logs = """2023-10-15 12:01:23 [INFO] Server started
2023-10-15 12:05:42 [ERROR] Database connection failed
2023-10-15 12:10:15 [INFO] User login
2023-10-15 12:15:33 [WARNING] High memory usage"""
        
        critical_logs = parser.extract_critical_logs(test_logs)
        
        self.assertEqual(len(critical_logs), 1)
        self.assertIn("[WARNING]", critical_logs[0])

class TestAlertSystem(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False).name
        
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            
    def test_save_alerts(self):
        alerts = [
            "2023-10-15 12:05:42 [ERROR] Database connection failed",
            "2023-10-15 12:15:33 [CRITICAL] Disk space low"
        ]
        
        system = AlertSystem()
        success = system.save_alerts(alerts, self.test_file)
        
        self.assertTrue(success)
        
        # Verify file content
        with open(self.test_file, 'r') as f:
            content = f.read()
            
        self.assertIn("Database connection failed", content)
        self.assertIn("Disk space low", content)
        
    def test_threshold_check(self):
        system = AlertSystem(threshold=3)
        
        # Below threshold
        alerts = ["Error 1", "Error 2", "Error 3"]
        self.assertFalse(system.check_threshold(alerts))
        
        # Above threshold
        alerts = ["Error 1", "Error 2", "Error 3", "Error 4"]
        self.assertTrue(system.check_threshold(alerts))

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.log_file = tempfile.NamedTemporaryFile(delete=False).name
        self.alert_file = tempfile.NamedTemporaryFile(delete=False).name
        
        # Create sample log file
        with open(self.log_file, 'w') as f:
            f.write("""2023-10-15 12:01:23 [INFO] Server started
2023-10-15 12:05:42 [ERROR] Database connection failed
2023-10-15 12:10:15 [INFO] User login
2023-10-15 12:15:33 [CRITICAL] Disk space low
2023-10-15 12:20:11 [WARNING] High memory usage
2023-10-15 12:25:42 [ERROR] Network timeout
2023-10-15 12:30:15 [INFO] Backup completed
2023-10-15 12:35:33 [CRITICAL] System overheating
2023-10-15 12:40:11 [ERROR] Authentication failed""")
        
    def tearDown(self):
        for file in [self.log_file, self.alert_file]:
            if os.path.exists(file):
                os.remove(file)
                
    def test_monitor_logs_with_threshold_exceeded(self):
        count, exceeded = monitor_logs(self.log_file, self.alert_file, threshold=3)
        
        self.assertEqual(count, 5)  # 3 ERROR + 2 CRITICAL
        self.assertTrue(exceeded)
        
        # Verify alert file content
        with open(self.alert_file, 'r') as f:
            content = f.readlines()
            
        self.assertEqual(len(content), 5)
        
    def test_monitor_logs_threshold_not_exceeded(self):
        count, exceeded = monitor_logs(self.log_file, self.alert_file, threshold=10)
        
        self.assertEqual(count, 5)
        self.assertFalse(exceeded)

if __name__ == '__main__':
    unittest.main()