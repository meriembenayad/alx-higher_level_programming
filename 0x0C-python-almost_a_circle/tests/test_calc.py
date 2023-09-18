#!/usr/bin/python3
""" Import module """
import unittest
import calc
""" class Test Calc """


class TestCalc(unittest.TestCase):
    """ test Add method """

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    """ test Sub method """

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, 1), -2)
        self.assertEqual(calc.sub(-1, -1), 0)

    """ test Mul method """

    def test_mul(self):
        result = calc.mul(10, 5)
        self.assertEqual(result, 50)

    """ test Div method """

    def test_div(self):
        result = calc.div(5, 2)
        self.assertEqual(result, 2.5)
        self.assertRaises(ValueError, calc.div, 10, 0)

    """ test Mod method """

    def test_mod(self):
        result = calc.mod(10, 5)
        self.assertEqual(result, 0)
        with self.assertRaises(ValueError):
            calc.mod(10, 0)
