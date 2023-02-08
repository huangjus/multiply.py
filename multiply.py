# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/8/23
# Description: A recursive function that takes two positive integers as parameters
# and returns the product of those two numbers

def multiply(multiplier, multiplicand):

    """
    This function takes two positive integers as parameters and returns the product of those two numbers.
    It finds the result by using addition instead of multiplication.

    multiplier: The first positive integer.
    multiplicand: The second positive integer.

    Returns: The product of the two positive integers.
    """

    if multiplicand == 1:
        return multiplier
    else:
        return multiplier + multiply(multiplier, multiplicand - 1)
