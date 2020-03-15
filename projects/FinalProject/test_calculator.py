from unittest import TestCase
import Calculator


class TestCalculator(TestCase):
    def setUp(self):
        self.Calculator = Calculator.Calculator()

    def test_division(self):
        # using assertEqual() to test and call the function at the same time
        self.assertEqual(self.Calculator.division(12, 4), 3)
        self.assertEqual(self.Calculator.division(10, -4), -2.5)
        self.assertEqual(self.Calculator.division(-12, -4), 3)
        self.assertEqual(self.Calculator.division(-4.8, 4), -1.2)
        self.assertEqual(self.Calculator.division(10000, 10), 1000)

    def test_square_root(self):
        # using assertEqual() to test and call the function at the same time
        self.assertEqual(self.Calculator.square_root(4), 2.0)
        self.assertEqual(self.Calculator.square_root(10.89), 3.3000000000000003)
        self.assertEqual(self.Calculator.square_root(0), 0.0)
        self.assertEqual(self.Calculator.square_root(10000), 100.0)

    def test_x_square(self):
        # using assertEqual() to test and call the function at the same time
        self.assertEqual(self.Calculator.x_square(4), 16)
        self.assertEqual(self.Calculator.x_square(-4.0), 16.0)
        self.assertEqual(self.Calculator.x_square(3.3), 10.889999999999999)
        self.assertEqual(self.Calculator.x_square(1000), 1000000)
        self.assertEqual(self.Calculator.x_square(0), 0)
