# Failed Login Attempt Monitor and Notifier for Windows Systems

## Overview

This tool monitors Windows Security Event Logs for failed login attempts (Event ID 4625), detects suspicious patterns (such as brute-force attacks), and notifies administrators via log files and console alerts. It is designed for security automation and can be configured for different thresholds, time windows, and alerting mechanisms.

---

## Table of Contents

- [Features](#features)
- [Team](#team)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules Explained](#modules-explained)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Extending the Tool](#extending-the-tool)
- [License](#license)
- [Authors](#authors)

---

## Features

- **Real-time monitoring** of Windows Security Event Logs for failed logins (Event ID 4625)
- **Detection of repeated failed attempts** from the same user or IP within a configurable time window
- **Alerting** via log file and console output (optional email alerting can be added)
- **Configurable thresholds** and monitoring intervals
- **Modular design** for easy extension and maintenance
- **Tested on Windows 10/11** (requires Administrator privileges)

---

## Team

- **John Brilhart:** Core script logic, log parsing, detection
- **Kent Peralta:** Alerting mechanism, cross-environment testing, documentation

---

## Requirements

- Python 3.8+
- Windows OS (with access to Security Event Log)
- Administrator privileges to read Security logs
- Python packages:
  - `pywin32`

---

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/yourusername/failed-login-attempt-monitor.git
    cd failed-login-attempt-monitor
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

---

## Configuration

Edit `src/config/__init__.py` to set your preferences:

- `THRESHOLD`: Number of failed attempts to trigger an alert (e.g., 3)
- `TIME_WINDOW_MINUTES`: Time window for counting failed attempts (e.g., 5)
- `LOG_FILE`: Path to the alert log file (e.g., `failed_login_attempts.log`)
- `monitoring_interval`: How often (in seconds) to check the logs (e.g., 60)
- `EMAIL`: (Optional) Email alert settings

Example:
```python
config = {
    "THRESHOLD": 3,
    "TIME_WINDOW_MINUTES": 5,
    "EMAIL": {
        "ENABLED": False,
        "SMTP_SERVER": "smtp.example.com",
        "PORT": 587,
        "USERNAME": "your@email.com",
        "PASSWORD": "yourpassword",
        "TO": "admin@email.com"
    },
    "LOG_FILE": "failed_login_attempts.log",
    "monitoring_interval": 60
}
```

---

## Usage

1. **Navigate to the `src` directory:**
    ```
    cd src
    ```

2. **Run the script as Administrator:**
    ```
    python main.py
    ```
    or
    ```
    py main.py
    ```

3. **Trigger failed login attempts** (e.g., by entering a wrong password at the lock screen or using `runas` with a wrong password).

4. **Check alerts:**
    - Console output
    - Log file (`failed_login_attempts.log` by default)

---

## Project Structure

```
src/
  config/
  log_reader/
  failed_attempt_tracker/
  notifier/
  logging_module/
  integration/
  main.py
tests/
requirements.txt
README.md
```

---

## Modules Explained

### 1. **Log Reader Module**
   - **Purpose:** Scans the Windows Security Event Logs for Event ID 4625 and extracts relevant fields (timestamp, username, IP address, failure reason).
   - **Integration:** Supplies failed login data to the tracker.

### 2. **Failed Attempt Tracker**
   - **Purpose:** Tracks repeated failed attempts from the same user/IP within a specified time window.
   - **Integration:** Determines if the alert threshold is met.

### 3. **Notifier Module**
   - **Purpose:** Sends an email alert or triggers a desktop/console notification when a threshold is exceeded.
   - **Integration:** Called by the integration module when suspicious activity is detected.

### 4. **Scheduler/Background Execution**
   - **Purpose:** Ensures the script runs periodically, either through a persistent loop with sleep intervals or via Task Scheduler.
   - **Integration:** Main loop in `integration` module.

### 5. **Logging Module**
   - **Purpose:** Saves triggered alerts to a local log file with timestamped entries and relevant context.
   - **Integration:** Called whenever an alert is triggered.

### 6. **Configuration Module**
   - **Purpose:** Central location for configurable parameters (thresholds, time windows, email credentials, log file paths).
   - **Integration:** Imported by all other modules.

### 7. **Testing Module**
   - **Purpose:** Contains scripts and functions to simulate failed logins or read from saved event data to validate functionality.
   - **Integration:** Used during development and QA.

---

## Testing

- **Unit Tests:** Located in the `tests/` directory. Run with:
    ```
    python -m unittest discover ../tests
    ```
- **Manual Testing:** Trigger failed logins as described in [Usage](#usage) and verify alerts are generated.

---

## Troubleshooting

- **No alerts/logs?**
  - Ensure you are running as Administrator.
  - Lower the threshold and time window for testing.
  - Confirm Event ID 4625 is being generated (check Event Viewer).

- **Permission error?**
  - Always run the script as Administrator to access Security logs.

- **Log file not created?**
  - Check the log file path in your config.
  - Test the logging module directly.

---

## Extending the Tool

- Add email alerting by configuring the `EMAIL` section in `config/__init__.py` and implementing the notifier module.
- Integrate with SIEM or other monitoring tools as needed.
- Add support for additional event IDs or custom detection logic.

---

## License

This project is for educational and internal use. Contact the authors for other uses.

---

## Authors

- John Brilhart
- Kent Peralta