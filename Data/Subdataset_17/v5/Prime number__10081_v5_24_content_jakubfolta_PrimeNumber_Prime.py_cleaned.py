def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True
print(is_prime(21))
print(is_prime(18))
print(is_prime(15))
print(is_prime(2))
print(is_prime(3))
print(is_prime(17))
