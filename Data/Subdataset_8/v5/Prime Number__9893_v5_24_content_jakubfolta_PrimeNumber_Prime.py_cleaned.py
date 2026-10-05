def is_prime(number):
    if number < 2:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True
print(is_prime(21))
def is_prime_v2(number):
    if number < 2:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True
print(is_prime_v2(18))
def is_prime_v3(number):
    if number < 2:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True
print(is_prime_v3(15))