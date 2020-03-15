from unittest import TestCase
from calculator import Calculator

class TestCalculator(TestCase):
    calculator = Calculator()
    def test_division(self):
        #using aserrtEqual() to test and call the function at the same time
        self.assertEqual(self.calculator.division(12, 4), 3)
        self.assertEqual(self.calculator.division(10, -4), -2.5)
        self.assertEqual(self.calculator.division(-12, -4), 3)
        self.assertEqual(self.calculator.division(-4.8, 4), -1.2)
        self.assertEqual(self.calculator.division(0, 0), "invalid input!")
        self.assertEqual(self.calculator.division(10000, 10), 1000)

    def test_square_root(self):
        #using aserrtEqual() to test and call the function at the same time
        self.assertEqual(self.calculator.square_root(4), 2.0)
        self.assertEqual(self.calculator.square_root(-4), "invalid input!")
        self.assertEqual(self.calculator.square_root(10.89), 3.3)
        self.assertEqual(self.calculator.square_root(0), 0.0)
        self.assertEqual(self.calculator.square_root(10000), 100.0)

    def test_x_square(self):
        #using aserrtEqual() to test and call the function at the same time
        self.assertEqual(self.calculator.x_square(4), 16)
        self.assertEqual(self.calculator.x_square(-4.0), 16.0)
        self.assertEqual(self.calculator.x_square(3.3), 10.89)
        self.assertEqual(self.calculator.x_square(1000), 100000)
        self.assertEqual(self.calculator.x_square(0), 0)