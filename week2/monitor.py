# 24/7 System Monitoring Script
import time
import os
from mailjet_rest import Client
import psutil


# Get your environment Mailjet keys
api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_PRIVATE']

mailjet = Client(auth=(api_key, api_secret), version='v3.1')
# Thresholds
CPU_THRESHOLD = 80     # percent
RAM_THRESHOLD = 80     # percent
DISK_THRESHOLD = 50    # percent free


def send_alert(subject, message):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "ishmael.gyamfi@amalitechtraining.org",
                    "Name": "24/7 SysMon"
                },
                "To": [
                    {
                        "Email": "kistlerk19@gmail.com",
                        "Name": "Admin"
                    },
                    {
                        "Email": "felix.frimpong@amalitechtraining.org",
                        "Name": "Admin"
                    },
                    {
                        "Email": "robert.amoah@amalitechtraining.org",
                        "Name": "Admin"
                    },
                    {
                        "Email": "ishmael.gyamfi@amalitechtraining.org",
                        "Name": "Admin"
                    },
                    {
                        "Email": "paul.mensah@amalitech.com",
                        "Name": "Admin"
                    },
                ],
                "Subject": subject,
                "HTMLPart": f"<h3>{message}</h3>"
            }
        ]
    }

    try:
        result = mailjet.send.create(data=data)
        print(f"Email sent: Status {result.status_code}")
        print(f"Response: {result.json()}")
        return result.status_code == 200
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False


def monitor_system(cpu_threshold=CPU_THRESHOLD, memory_threshold=RAM_THRESHOLD, disk_threshold=DISK_THRESHOLD, interval=60):
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_used = psutil.disk_usage('/').percent
        disk_free = 100 - disk_used

        print(f"[{current_time}] CPU: {cpu_usage}% | Memory: {memory_usage}% | Disk Free: {disk_free}%")

        if cpu_usage > cpu_threshold:
            send_alert("🚨 High CPU Usage Alert", f"CPU usage is at {cpu_usage}%, above threshold {cpu_threshold}%")

        if memory_usage > memory_threshold:
            send_alert("🚨 High Memory Usage Alert", f"Memory usage is at {memory_usage}%, above threshold {memory_threshold}%")

        if disk_free < disk_threshold:
            send_alert("🚨 Low Disk Space Alert", f"Disk free space is at {disk_free}%, below threshold {disk_threshold}%")

        time.sleep(interval)


if __name__ == "__main__":
    # Send test email
    send_alert("✅ Mailjet Test Alert", "This is a test email from your Python monitoring script. If you see this, it worked!")
    
    # Start monitoring
    monitor_system()