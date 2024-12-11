def fonk1(b1):
    if isinstance(b1, complex):
        if b1.imag != 0:
            raise ValueError("Factorial is not defined for complex numbers with non-zero imaginary part.")
        b1 = b1.real
    if not isinstance(b1, (int, float)):
        raise ValueError("Factorial is not defined for non-integer data types.")
    if b1 != int(b1) or b1 < 0:
        raise ValueError("Factorial is not defined for non-positive integers.")
    a1 = 1
    for b2 in range(1, int(b1) + 1):
        a1 *= b2
    return a1
try:
    b2 = input('Enter a positive integer: ')
    if b2.lower() == 'q':
        exit()
    b2 = int(b2)
    b3 = fonk1(b2)
    print(f"The factorial of {b2} is {b3}")
except ValueError as e:
    print(e)