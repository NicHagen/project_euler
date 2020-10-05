""" 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagorean_triple_product(target, limit=100):
    """function to calculate the product of a*b*c of the pythagorean triple for 
    which, a + b + c = target. All primitive triples (non-scaled) can be
    determined by the representation (m > n):
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2


    Args:
        target (integer): desired sum of the triple
        limit (integer, optional): upper bound for m. Defaults to 100.

    Returns:
        [type]: [description]
    """
    for m in range(limit):
        for n in range(m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if a + b + c == target:
                product = a * b * c
                return product
    return 'Not found in limit or does not exist'
    

print(pythagorean_triple_product(1000))
