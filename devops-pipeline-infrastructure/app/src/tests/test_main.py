# app/src/tests/test_main.py
import unittest
from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b"Hello, World!")

    def test_multiply(self):
        response = self.app.get('/multiply/2/3')
        self.assertEqual(response.data, b"6")

if __name__ == '__main__':
    unittest.main()

