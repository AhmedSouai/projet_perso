# app/src/tests/test_performance.py
import time
import unittest
from main import app

class TestPerformance(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_performance(self):
        start_time = time.time()
        for _ in range(1000):  # simulate multiple requests
            self.app.get('/multiply/2/3')
        end_time = time.time()
        self.assertTrue(end_time - start_time < 1)  # We expect all 1000 requests to take less than 1 second

if __name__ == '__main__':
    unittest.main()

