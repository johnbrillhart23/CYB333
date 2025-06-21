import unittest
from src.notifier import send_alert

class TestNotifier(unittest.TestCase):

    def test_send_alert(self):
        # Test sending a simple alert message
        message = "Test alert: Multiple failed login attempts detected."
        result = send_alert(message)
        self.assertTrue(result)  # Assuming send_alert returns True on success

if __name__ == '__main__':
    unittest.main()