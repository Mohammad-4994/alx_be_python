import unittest 

from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # Create an instance of SimpleCalculator to use in tests
        self.calc = SimpleCalculator()

    def test_add(self):
        # Test basic addition
        self.assertEqual(self.calc.add(1, 1), 2)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        # Test basic multiplication
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        # Test basic division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(7, 7), 1)

        # Test divide by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
