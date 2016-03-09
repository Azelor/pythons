def is_prime(n):
    "Is n a prime number?"
    if n<2:
        return False
    for divider in range(2, n//2 + 1):
        print(divider)
        if (n % divider) == 0:
            return False
    return True
