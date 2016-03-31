import math

def is_prime(n):
    "Checks if an entered number is a prime (with sqrt)"
    for i in range(2,int(math.sqrt(n))):
        print(i)
        if n % i == 0:
            return False
    else:
        return True

