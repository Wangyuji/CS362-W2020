# Final Project
# Author: Yujie Wang
# Course: CS362
# Date: 2020/3/12

import math


# Note: According to the previous email,
# this final project only include function 2, 3 and 4.

# Calculator
class Calculator:
    def _init_(self):
        pass

    def division(self, x, y):
        if y != 0:
            return x / y   # the denominator cant be zero

    def square_root(self, x):
        if x >= 0:
            return math.sqrt(x)   # the input number cant be negative

    def x_square(self, x):  # x^2
        return x * x
