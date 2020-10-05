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


import numpy as np





def eratosthenes(N):
    """eratosthenes sieve for creating prime numbers

    Args:
        N (integer): the maximum value to create prime numbers within

    Returns:
        numpy.ndarray: numpy array containing all the prime numbers <= N
    """
    eratosthenes = True
    # mask for prime numbers
    mask = np.ones([N], dtype=bool)
    if not eratosthenes:
        # simple prime sieve
        mask[:2] = False
        for j in range(2, int(np.sqrt(N)) + 1):
            mask[j*j::j] = False
    else:
        # Eratosthenes sieve
        mask[:2] = False
        for j in range(2, int(np.sqrt(N)) + 1):
            if mask[j]:
                mask[j*j::j] = False
    return np.nonzero(mask)[0]