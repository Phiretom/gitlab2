import unittest
from rectangle import area,perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0, 13)
        self.assertEqual(res, 0)

    def test_one_mul(self):
        res = area(10, 13)
        self.assertEqual(res, 130)

    def test_two_mul(self):
        res = area(67.5, 3.5)
        self.assertEqual(res, 236.25)

    def test_three_mul(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_four_mul(self):
        res = perimeter(10, 54)
        self.assertEqual(res, 128)

    def test_five_mul(self):
        res = perimeter(67.636, 42.364)
        self.assertEqual(res, 220)