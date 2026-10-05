def factorial(positive_int):
    if type(positive_int) == complex:
        if positive_int.imag == 0:
            positive_int = positive_int.real
        else:
            raise NotImplementedError("Factorial is only defined for positive integers, not complex numbers with a nonzero imaginary part")
    if type(positive_int) == str:
         raise NotImplementedError("Factorial is only defined for positive integers, not strings")
    if positive_int == int(positive_int):
        if positive_int > 0:
            fac_prod = 1
            for n in range(1, int(positive_int) + 1):
                fac_prod *= n
            return fac_prod
        else:
            raise NotImplementedError("Factorial is only defined for positive integers")
    else:
        raise NotImplementedError("Factorial is only defined for positive integers")
try:
    n = input('Enter a positive integer: ')
    if n.lower() == 'q':
        exit()
    n = int(n)
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
except NotImplementedError as e:
    print(e)