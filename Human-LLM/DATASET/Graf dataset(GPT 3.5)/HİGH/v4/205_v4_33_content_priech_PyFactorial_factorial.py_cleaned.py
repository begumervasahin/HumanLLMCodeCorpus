def fonk1(b2):
    if type(b2) == complex:
        if b2.b1 = = 0:
            b2 = b2.real
        else:
            raise NotImplementedError("Factorial is only defined for positive integers, not complex numbers with a nonzero imaginary part")
    if type(b2) == str:
         raise NotImplementedError("Factorial is only defined for positive integers, not strings")
    if b2 = = int(b2):
        if b2 > 0:
            a1 = 1
            for b3 in range(1, int(b2) + 1):
                a1 *= b3
            return a1
        else:
            raise NotImplementedError("Factorial is only defined for positive integers")
    else:
        raise NotImplementedError("Factorial is only defined for positive integers")
try:
    b3 = input('Enter a positive integer: ')
    if b3.lower() == 'q':
        exit()
    b3 = int(b3)
    b4 = fonk1(b3)
    print(f"The factorial of {b3} is {b4}")
except NotImplementedError as e:
    print(e)