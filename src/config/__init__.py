config = {
    "THRESHOLD": 1,
    "TIME_WINDOW_MINUTES": 5,
    "EMAIL": {
        "ENABLED": True,
        "SMTP_SERVER": "smtp.example.com",
        "PORT": 587,
        "USERNAME": "your@email.com",
        "PASSWORD": "yourpassword",
        "TO": "admin@email.com"
    },
    "LOG_FILE": "alerts.log",
    "monitoring_interval": 60  # Check every 60 seconds 
}