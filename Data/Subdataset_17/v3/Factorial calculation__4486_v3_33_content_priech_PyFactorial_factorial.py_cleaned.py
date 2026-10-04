def factorial(value):
    if isinstance(value, complex):
        if value.imag != 0:
            raise ValueError("Factorial is only defined for positive integers, not complex values with non-zero imaginary parts.")
        value = value.real
    if isinstance(value, str):
        raise ValueError("Factorial is only defined for positive integers, not strings.")
    if not isinstance(value, (int, float)) or value != int(value):
        raise ValueError("Factorial is only defined for positive integers.")
    value = int(value)
    if value <= 0:
        raise ValueError("Factorial is only defined for positive integers.")
    result = 1
    for n in range(1, value + 1):
        result *= n
    return result
if __name__ == "__main__":
    try:
        num = 5
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(e)