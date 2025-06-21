def run_monitoring(tracker):
    import time
    from log_reader import read_failed_logins
    from failed_attempt_tracker import FailedAttemptTracker
    from notifier import send_alert
    from logging_module import log_alert
    from config import config

    #tracker = FailedAttemptTracker()

    while True:
        failed_logins = read_failed_logins()
        for login in failed_logins:
            username = login['username']
            ip_address = login['ip_address']
            failure_reason = login['failure_reason']

            tracker.add_attempt(username, ip_address)

            if tracker.check_threshold(username, ip_address):
                message = f"Alert: Multiple failed login attempts detected for user {username} from IP {ip_address}. Reason: {failure_reason}"
                send_alert(message)
                log_alert(message)

        time.sleep(config['monitoring_interval'])  # Sleep for the specified interval before the next check