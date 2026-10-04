def factorial(positive_int):
    if isinstance(positive_int, complex):
        if positive_int.imag == 0:
            positive_int = positive_int.real
        else:
            raise NotImplementedError("The factorial is only defined for positive integers, not complex values with non-zero imaginary parts.")
    if isinstance(positive_int, str):
        raise NotImplementedError("The factorial is only defined for positive integers, not strings.")
    if isinstance(positive_int, (int, float)) and positive_int == int(positive_int):
        positive_int = int(positive_int)
        if positive_int > 0:
            fac_prod = 1
            for n in range(1, positive_int + 1):
                fac_prod *= n
            return fac_prod
        else:
            raise NotImplementedError("The factorial is only defined for positive integers.")
    else:
        raise NotImplementedError("The factorial is only defined for positive integers.")
if __name__ == "__main__":
    try:
        num = 5
        print(f"Factorial of {num} is {factorial(num)}")
    except NotImplementedError as e:
        print(e)