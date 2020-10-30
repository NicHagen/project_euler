"""
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

"""
Number of lattice paths in a m*n grid can be determined as the binomial
coefficient binom(n+m, m)
"""

from scipy.special import binom

d = 20
n = d + d
k = d

print(int(binom(n,k)))
