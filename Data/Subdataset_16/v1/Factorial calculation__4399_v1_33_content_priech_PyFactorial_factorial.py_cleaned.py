def fonk1(b2):
    if isinstance(b2, complex):
        if b2.b1 = = 0:
            b2 = b2.real
        else:
            raise NotImplementedError("The factorial is only defined for positive integers, not complex values with non-zero imaginary parts.")
    if isinstance(b2, str):
        raise NotImplementedError("The factorial is only defined for positive integers, not strings.")
    if isinstance(b2, (int, float)) and b2 = = int(b2):
        b2 = int(b2)
        if b2 > 0:
            a1 = 1
            for n in range(1, b2 + 1):
                a1 *= n
            return a1
        else:
            raise NotImplementedError("The factorial is only defined for positive integers.")
    else:
        raise NotImplementedError("The factorial is only defined for positive integers.")
if b3 = = "__main__":
    try:
        a2 = 5
        print(f"Factorial of {a2} is {fonk1(a2)}")
    except NotImplementedError as e:
        print(e)