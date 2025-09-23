# arrange
import unittest
from src.greetings import greet

class TestGreeting(unittest.TestCase):
    def test_greets_hello_world(self):
        self.assertEqual("Hello, World", greet())

# act

# assert
