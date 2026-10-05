def factorial(n):
    if n < 1:
        return 1
    else:
        result = n * factorial(n - 1)
        print(str(n) + '! = ' + str(result))
        return result
factorial(4)