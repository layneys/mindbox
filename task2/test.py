import unittest
from area.area import circleArea, sign, checkConvexity, shoelaceArea
from math import pi


class TestArea(unittest.TestCase):
    
    def test_sign_empty_input(self):
        with self.assertRaises(TypeError):
            circleArea()

    def test_sign_positive(self):
        self.assertEqual(sign(6), 'positive')

    def test_sign_negative(self):
        self.assertEqual(sign(0), 'zero')

    def test_sign_zero(self):
        self.assertEqual(sign(-6), 'negative')

    def test_circleArea_empty_input(self):
        with self.assertRaises(TypeError):
            circleArea()

    def test_circleArea_radius(self):
        radius=5
        self.assertEqual(circleArea(radius), pi*radius**2)

    def test_circleArea_zero(self):
        radius=0
        self.assertEqual(circleArea(radius), 0)

    def test_circleArea_negative(self):
        radius=-1
        with self.assertRaises(ValueError):
            circleArea(radius)

    def test_checkConvexity_empty_input(self):
        with self.assertRaises(TypeError):
            checkConvexity()

    def test_checkConvexity_convex(self):
        data = [[1,1], [2,3], [4,3], [5,1]]
        self.assertIsNone(checkConvexity(data))

    def test_checkConvexity_zero(self):
        data = [[0,0], [0,0]]
        with self.assertRaises(ValueError):
            checkConvexity(data)

    def test_checkConvexity_not_convex(self):
        data = [[1,1], [2,3], [3,2], [4,3], [5,1]]
        with self.assertRaises(ValueError):
            checkConvexity(data)
    
    def test_shoelaceArea(self):
        data = [[1,1], [2,3], [4,3], [5,1]]
        self.assertEqual(shoelaceArea(data), 6)


if __name__ == '__main__':
    unittest.main()