"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""
_cache = {}
def fibonacci(n):
    """function that computes the nth number of the Fibonacci sequence of
    numbers

    Args:
        n (integer): number in the Fibonacci sequence to compute, counting from
        0

    Returns:
        integer: the nth number of the Fibonacci sequence
    """
    if n in _cache:
        return _cache[n]
    elif n < 2:
        _cache[n] = n
        return n
    else:
        _cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return _cache[n]

n = 1
sum = 0

while fibonacci(n) < 4000000:
    if fibonacci(n) % 2 == 0:
        sum += fibonacci(n)
    n += 1

print('The sum of the even Fibonacci terms smaller than 4,000,000 is: ', sum)

