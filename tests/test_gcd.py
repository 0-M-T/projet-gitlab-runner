import unittest
from my_arithmetic.gcd import gcd

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 10), 1)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(7, 0), 7)
        self.assertEqual(gcd(0, 5), 5)

if __name__ == "__main__":
    unittest.main()
