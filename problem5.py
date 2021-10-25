"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# num = 2520
# check = True


# while check == True:
#     count = 0
#     for i in range(1,21):
#         if count < 20:
#             if num % i == 0:
#                 count += 1
#             else:
#                 count += 21
#     if count == 20:
#         check = False
#         print(num)
#     num += 20

"""
More efficient solution utilising the fact that the prime factorisation of
the number has to contain the least amount of prime factors smaller than or
equal to the largest divisible number, k.
"""

def all_primes(num):
    """function that returns all primes up until num

    Args:
        num (integer): upper limit of numbers to find primes in

    Returns:
        list: list containing all the primes from 2 to num
    """
    cand_list = list(range(3, num+1))
    prime_list = [2,]
    for j in prime_list:
        for i in cand_list:
            if i % j == 0:
                cand_list.pop(cand_list.index(i))
        if cand_list:
            prime_list.append(cand_list[0])
    return prime_list

def smallest_multiple(k):
    """function to find the smallest multiple of the numbers from 2..k.
    Finds the primes in the range 2..k and then represents all the numbers
    from 2..k using the least amount of primes by calculating the exponents.
    Dependence on the all_primes() function.

    Args:
        k (integer): the upper limit in the range from 2..k

    Returns:
        integer: the smallest multiple of the numbers from 2..k
    """
    primes = all_primes(k)
    powers = [0] * len(primes)
    poly = 1
    j = 0
    for prime in primes:
        i = 1
        while prime**i <= k:
            powers[j] = powers[j] + 1
            i += 1
        j += 1
    for i in range(len(primes)):
        poly *= primes[i]**powers[i]
    return poly

print(smallest_multiple(20))