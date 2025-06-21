import unittest
from src.config import config

class TestConfig(unittest.TestCase):
    def test_config_loaded(self):
        self.assertIsInstance(config, dict)

    def test_thresholds(self):
        self.assertIn('threshold', config)
        self.assertIsInstance(config['threshold'], int)

    def test_time_window(self):
        self.assertIn('time_window', config)
        self.assertIsInstance(config['time_window'], int)

    def test_email_credentials(self):
        self.assertIn('email', config)
        self.assertIn('password', config['email'])
        self.assertIsInstance(config['email']['password'], str)

    def test_log_file_path(self):
        self.assertIn('log_file_path', config)
        self.assertIsInstance(config['log_file_path'], str)

if __name__ == '__main__':
    unittest.main()