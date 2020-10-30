import numpy as np

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""
#brute-force by calculating every chain length

# N = 1000000

# def even(n):
#     return n/2

# def odd(n):
#     return 3*n + 1

# countMax = 0

# for n in range(1, N,):
#     count = 1
#     temp = n
#     while n != 1:
#         if n%2 == 0:
#             n = even(n)
#             count += 1
#         else:
#             n = odd(n)
#             count += 1
#     if count > countMax:
#         countMax = count
#         number = temp

# print(number, countMax)

"""
Implement a cache of values to avoid calculating the length of the chain from
already known values.

Additionally,

Collatz(n) = Collatz(n/2) + 1,

therefore Collatz(2k) > Collatz(k) and it is not necessary to calculate the
chain for values below N/2.

Furthermore, if n is odd, then 3n + 1 is even and it follows,

Collatz(n) = Collatz(3n + 1) + 1 = Collatz((3n + 1)/2) + 2.
"""

def chainLength(n):
    if n in _cache:
        return _cache[n]
    elif n%2 == 0:
        _cache[n] = 1 + chainLength(n/2)
    else:
        _cache[n] = 2 + chainLength((3*n + 1)/2)
    return _cache[n]

N = 1000000
longest = 0
_cache = {1: 1}
number = 1
for i in range(N//2,N):
    if chainLength(i) > longest:
        longest = chainLength(i)
        number = i

print(number, _cache[number])



