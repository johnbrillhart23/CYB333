import unittest
from src.failed_attempt_tracker import FailedAttemptTracker

class TestFailedAttemptTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = FailedAttemptTracker()
        self.username = "test_user"
        self.ip_address = "192.168.1.1"

    def test_add_attempt(self):
        self.tracker.add_attempt(self.username, self.ip_address)
        self.assertIn((self.username, self.ip_address), self.tracker.attempts)

    def test_check_threshold_not_exceeded(self):
        self.tracker.add_attempt(self.username, self.ip_address)
        self.assertFalse(self.tracker.check_threshold(self.username, self.ip_address))

    def test_check_threshold_exceeded(self):
        for _ in range(5):  # Assuming the threshold is set to 3
            self.tracker.add_attempt(self.username, self.ip_address)
        self.assertTrue(self.tracker.check_threshold(self.username, self.ip_address))

    def test_different_user_ip(self):
        self.tracker.add_attempt(self.username, self.ip_address)
        self.assertFalse(self.tracker.check_threshold("other_user", "192.168.1.2"))

if __name__ == '__main__':
    unittest.main()