import unittest
from mock import patch
import RedDefineBot

class TestBot(unittest.TestCase):
    def test_auth_called(self,mock):
        self.assertTrue(mock.called)
    def test_auth_notcalled(self,mock):
        self.assertFalse(mock.called)

if __name__ == '__main__':
    unittest.main()
