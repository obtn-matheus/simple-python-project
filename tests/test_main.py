import unittest
from app.main import greet

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("Python"), "Hello, Python!")

if __name__ == "__main__":
    unittest.main()
