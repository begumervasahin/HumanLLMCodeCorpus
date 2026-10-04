def fonk1(b1):
    if isinstance(b1, complex):
        if b1.imag != 0:
            raise ValueError("Factorial is only defined for positive integers, not complex values with non-zero imaginary parts.")
        b1 = b1.real
    if isinstance(b1, str):
        raise ValueError("Factorial is only defined for positive integers, not strings.")
    if not isinstance(b1, (int, float)) or b1 != int(b1):
        raise ValueError("Factorial is only defined for positive integers.")
    b1 = int(b1)
    if b1 <= 0:
        raise ValueError("Factorial is only defined for positive integers.")
    a1 = 1
    for n in range(1, b1 + 1):
        a1 *= n
    return a1
if b2 = = "__main__":
    try:
        a2 = 5
        print(f"Factorial of {a2} is {fonk1(a2)}")
    except ValueError as e:
        print(e)