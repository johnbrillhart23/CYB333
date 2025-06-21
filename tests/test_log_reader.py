import unittest
from src.log_reader import read_failed_logins

class TestLogReader(unittest.TestCase):

    def test_read_failed_logins(self):
        # Assuming the function returns a list of dictionaries with expected keys
        failed_logins = read_failed_logins()
        self.assertIsInstance(failed_logins, list)
        
        if failed_logins:
            for login in failed_logins:
                self.assertIn('timestamp', login)
                self.assertIn('username', login)
                self.assertIn('ip_address', login)
                self.assertIn('failure_reason', login)

if __name__ == '__main__':
    unittest.main()