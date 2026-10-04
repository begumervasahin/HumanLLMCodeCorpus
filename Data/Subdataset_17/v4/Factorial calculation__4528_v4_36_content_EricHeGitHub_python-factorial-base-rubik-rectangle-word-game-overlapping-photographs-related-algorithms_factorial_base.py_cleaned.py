from sys import exit
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def list_to_integer(lst):
    result = 0
    power = len(lst) - 1
    for i in lst:
        result += i * (10 ** power)
        power -= 1
    return result
def main():
    number = input('Input a nonnegative integer: ')
    if not number.isdigit() or number == '0':
        print('Incorrect input, giving up...')
        exit()
    number = int(number)
    original_number = number
    max_factorial_index = 1
    while factorial(max_factorial_index) <= number:
        max_factorial_index += 1
    max_factorial_index -= 1
    factorial_digits = []
    while number > 0:
        for i in range(max_factorial_index, 0, -1):
            factor_count = 0
            while (factor_count + 1) * factorial(i) <= number:
                factor_count += 1
            factorial_digits.append(factor_count)
            number -= factor_count * factorial(i)
    factorial_base_number = list_to_integer(factorial_digits)
    print(f'Decimal {original_number} reads as {factorial_base_number} in factorial base.')
if __name__ == "__main__":
    main()