def factorial(value):
    if isinstance(value, complex):
        if value.imag == 0:
            value = value.real
        else:
            raise ValueError("Factorial is only defined for positive integers, not complex values with non-zero imaginary parts.")
    if isinstance(value, str):
        raise ValueError("Factorial is only defined for positive integers, not strings.")
    if isinstance(value, (int, float)) and value == int(value):
        value = int(value)
        if value > 0:
            result = 1
            for n in range(1, value + 1):
                result *= n
            return result
        else:
            raise ValueError("Factorial is only defined for positive integers.")
    else:
        raise ValueError("Factorial is only defined for positive integers.")
if __name__ == "__main__":
    try:
        num = 5
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(e)