def is_prime(digit):
    if digit < 2:
        return False
    for number in range(2, int(digit ** 0.5) + 1):
        if digit % number == 0:
            return False
    return True
def print_and_check_prime(number):
    if number < 2:
        return False
    for x in range(2, number):
        print(x)
        if number % x == 0:
            return False
    return True
def check_if_prime(number):
    if number < 2:
        return False
    for x in range(2, int(number ** 0.5) + 1):
        if number % x == 0:
            return False
    return True
print(is_prime(21))
print(print_and_check_prime(18))
print(check_if_prime(15))
