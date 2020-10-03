"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import numpy as np

def largest_prime_factor(n):
    largest_prime = 0
    while n % 2 == 0:
        largest_prime = 2
        n /= 2
    for i in range(3, int(np.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n /= i
    if n > 2:
        largest_prime = n
    return largest_prime

print(largest_prime_factor(600851475143))