def is_prime(n):
    "Is n a prime number?"
    if n<2:
        return False
    for divider in range(2, n//2 + 1):
        print(divider)
        if (n % divider) == 0:
            return False
    return True


def primes(primes_list):
    "Returns primes belonging to the list"
    tulem = []
    for num in primes_list:
        if is_prime(num):
            tulem.append(num)
    return tulem
