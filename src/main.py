from log_reader import read_failed_logins
from failed_attempt_tracker import FailedAttemptTracker
from notifier import send_alert
from scheduler import start_scheduler
from logging_module import log_alert
from config import config
from integration import run_monitoring

def main():
    time_window = config["TIME_WINDOW_MINUTES"]
    threshold = config["THRESHOLD"]
    # Initialize the failed attempt tracker
    tracker = FailedAttemptTracker(time_window, threshold)

    # Start the monitoring process
    run_monitoring(tracker)

if __name__ == "__main__":
    main()