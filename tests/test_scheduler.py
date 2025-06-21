import unittest
from src.scheduler import start_scheduler
from unittest.mock import patch
import time

class TestScheduler(unittest.TestCase):

    @patch('time.sleep', return_value=None)  # Mock time.sleep to avoid actual waiting
    def test_start_scheduler(self, mock_sleep):
        interval = 5  # seconds
        start_time = time.time()
        
        # Start the scheduler in a separate thread or process
        # Here we will just simulate the call
        start_scheduler(interval)
        
        # Check if the sleep function was called with the correct interval
        mock_sleep.assert_called_with(interval)
        
        # Ensure that the scheduler runs for a reasonable time
        elapsed_time = time.time() - start_time
        self.assertGreaterEqual(elapsed_time, interval)

if __name__ == '__main__':
    unittest.main()