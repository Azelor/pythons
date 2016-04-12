def factorial(n):
    print("Factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        print("intermediate result: ", n)
        return n * factorial(n-1)

print("faktoriaal on ", factorial(6))
