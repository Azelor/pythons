def divide(x, y):
    try:
        result = x / y
    except zeroDivisionError:
        print("Division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

xx = input("Number to divide:  ")
yy = input("Number to divide with:  ")

divide(float(xx), float(yy))
