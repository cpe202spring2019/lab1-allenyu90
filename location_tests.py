import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertNotEqual(repr(loc),"Location('SF', 45.4, -120.7)")

    # Add more tests!

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location('SF', 45.4, -120.7)
        loc3 = loc1
        self.assertEqual(loc1, loc3)
        self.assertNotEqual(loc1, loc2)
        self.assertNotEqual(loc2, loc3)


if __name__ == "__main__":
        unittest.main()
