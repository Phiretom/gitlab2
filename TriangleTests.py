import unittest
from triangle import area,perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0, 2)
        self.assertEqual(res, 0)

    def test_one_mul(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_two_mul(self):
        res = area(7.5, 3.5)
        self.assertEqual(res, 13.125)

    def test_three_mul(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_four_mul(self):
        res = perimeter(10, 4, 8)
        self.assertEqual(res, 22)

    def test_five_mul(self):
        res = perimeter(34.23, 42.34, 23.43)
        self.assertEqual(res, 100)