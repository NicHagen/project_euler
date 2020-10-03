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

# print(all_primes(20))