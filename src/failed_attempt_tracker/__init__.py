class FailedAttemptTracker:
    def __init__(self, time_window, threshold):
        self.attempts = {}
        self.time_window = time_window
        self.threshold = threshold

    def add_attempt(self, username, ip_address):
        from time import time
        current_time = time()
        key = (username, ip_address)

        if key not in self.attempts:
            self.attempts[key] = []

        # Remove attempts that are outside the time window
        self.attempts[key] = [t for t in self.attempts[key] if current_time - t < self.time_window]

        # Add the current attempt
        self.attempts[key].append(current_time)

    def check_threshold(self, username, ip_address):
        key = (username, ip_address)
        if key in self.attempts:
            return len(self.attempts[key]) >= self.threshold
        return False