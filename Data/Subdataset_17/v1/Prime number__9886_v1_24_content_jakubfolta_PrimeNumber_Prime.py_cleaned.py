def is_prime(digit):
    if digit < 2:
        return False
    elif digit == 2:
        return True
    for number in range(2, digit):
        if digit % number == 0:
            return False
    return True
def prime(number):
    if number < 2:
        return False
    elif number == 2:
        return False
    else:
        for x in range(2, number):
            print(x)
            if number % x == 0:
                return False
        return True
def check_if_prime_number(number):
    if number < 2:
        return False
    for x in range(2, number - 1):
        if number % x == 0:
            return False
    return True
print(is_prime(21))
print(prime(18))
print(check_if_prime_number(15))
