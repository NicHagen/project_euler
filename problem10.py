""" 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import numpy as np
from prime import eratosthenes

print(np.sum(eratosthenes(2000000)))

