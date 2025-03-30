# app/src/tests/test_integration.py
import unittest
from main import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_multiply_integration(self):
        response = self.app.get('/multiply/4/5')
        self.assertEqual(response.data, b"20")

if __name__ == '__main__':
    unittest.main()

