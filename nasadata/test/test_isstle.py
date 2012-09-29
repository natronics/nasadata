import unittest
from nasadata import isstle

class TestIssTle(unittest.TestCase):

    def test_create(self):
        tle = isstle.tle()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
