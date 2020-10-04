"""
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def square_sum_difference(k):
    """function that calculates the difference between the square of a sum and
    the sum of the squares. Utilises the rule that the square of a sum is equal
    to the sum of the squares of all the summands plus the sum of all the 
    double products of the summands in twos.  

    Args:
        k (integer): the upper bound of the summands in 1..k

    Returns:
        integer: the difference between square of sum and sum of squares
    """
    square_sum = 0
    sum_square = 0
    for i in range(1, k + 1):
        sum_square += i**2
        for j in range(i + 1, k + 1):
            square_sum += 2 * i * j
    square_sum += sum_square
    return square_sum - sum_square

print(square_sum_difference(100))
