import unittest
from src.logging_module import log_alert

class TestLoggingModule(unittest.TestCase):

    def setUp(self):
        self.test_message = "Test alert message"
        self.log_file_path = "path/to/log_file.log"  # Update with actual log file path if needed

    def test_log_alert(self):
        log_alert(self.test_message)
        with open(self.log_file_path, 'r') as log_file:
            logs = log_file.readlines()
            self.assertIn(self.test_message, logs[-1])  # Check if the last log entry contains the test message

if __name__ == '__main__':
    unittest.main()