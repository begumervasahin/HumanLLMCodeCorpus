def factorial(positive_int):
    if isinstance(positive_int, complex):
        if positive_int.imag != 0:
            raise ValueError("Factorial is not defined for complex numbers with non-zero imaginary part.")
        positive_int = positive_int.real
    if not isinstance(positive_int, (int, float)):
        raise ValueError("Factorial is not defined for non-integer data types.")
    if positive_int != int(positive_int) or positive_int < 0:
        raise ValueError("Factorial is not defined for non-positive integers.")
    fac_prod = 1
    for n in range(1, int(positive_int) + 1):
        fac_prod *= n
    return fac_prod
try:
    n = input('Enter a positive integer: ')
    if n.lower() == 'q':
        exit()
    n = int(n)
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
except ValueError as e:
    print(e)