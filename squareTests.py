import unittest
from square import area,perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_one_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_two_mul(self):
        res = area(7.5)
        self.assertEqual(res, 56.25)

    def test_three_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_four_mul(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_five_mul(self):
        res = perimeter(17.25)
        self.assertEqual(res, 69)
