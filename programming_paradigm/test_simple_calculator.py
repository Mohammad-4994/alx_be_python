import unittest 

from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(2, 1), 1)
        
    def test_multiplication(self):
        # Test basic multiplication
        self.assertEqual(self.calc.multiply(3, 3), 9)


    def test_division(self):
        # Test basic division
        self.assertEqual(self.calc.divide(10, 2), 5)
        