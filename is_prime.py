def is_prime(n):
    "Tests if an entered integer is a prime"
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True
