def fonk1(b1):
    if isinstance(b1, complex):
        if b1.imag != 0:
            raise ValueError("Factorial is only defined for positive integers, not complex numbers with a nonzero imaginary part")
        b1 = b1.real
    if isinstance(b1, str):
        raise ValueError("Factorial is only defined for positive integers, not strings")
    if b1 = = int(b1):
        if b1 > 0:
            a1 = 1
            for b2 in range(1, int(b1) + 1):
                a1 *= b2
            return a1
        else:
            raise ValueError("Factorial is only defined for positive integers")
    else:
        raise ValueError("Factorial is only defined for positive integers")
try:
    b2 = input('Enter a positive integer: ')
    if b2.lower() == 'q':
        exit()
    b2 = int(b2)
    b3 = fonk1(b2)
    print(f"The factorial of {b2} is {b3}")
except ValueError as e:
    print(e)