"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def multi_table(num):
    """The function multi_table creates a multiplication table of size num by
    num.

    Args:
        num (integer): the size of the multiplication table

    Returns:
        list: list of lists of the rows in the multiplication table
    """
    table = []
    for i in range(1, num + 1):
        row = [i*j for j in range(1, num + 1)]
        table.append(row)
    return table
# mult_table = multi_table(999)

# palindrome = 0

# for i in range(len(mult_table)):
#     for num in mult_table[i]:
#         if str(num) == str(num)[::-1] and num > palindrome:
#             palindrome = num

# print(palindrome)

def largest_palindrome(digit):
    """function that finds the largest palindrome made of the product of at
    most the square of digit. Depends on the multi_table() function to create
    all the products.

    Args:
        digit (integer): the upper limit of the product

    Returns:
        integer: the largest palindrome found
    """
    table = multi_table(digit)
    palindrome = 0
    for i in range(len(table)):
        for num in table[i]:
            if str(num) == str(num)[::-1] and num > palindrome:
                palindrome = num
    return palindrome

print(largest_palindrome(999))
