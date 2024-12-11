def fonk1(b2):
    if isinstance(b2, complex):
        if b2.b1 = = 0:
            b2 = b2.real
        else:
            raise ValueError("The factorial is only defined for positive integers, not complex values with nonzero imaginary part")
    if isinstance(b2, str):
        raise ValueError("The factorial is only defined for positive integers, not strings")
    if b2 = = int(b2):
        if b2 > 0:
            a1 = 1
            for b3 in range(1, int(b2) + 1):
                a1 *= b3
            return a1
        else:
            raise ValueError("The factorial is only defined for positive integers")
    else:
        raise ValueError("The factorial is only defined for positive integers")
try:
    b3 = int(input('Enter a positive integer: '))
    b4 = fonk1(b3)
    print(f"The factorial of {b3} is {b4}")
except ValueError as e:
    print(e)