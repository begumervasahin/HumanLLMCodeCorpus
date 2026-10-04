def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for x in range(2, int(number ** 0.5) + 1):
            if number % x == 0:
                return False
        return True
print(is_prime(21))
print(is_prime(18))
print(is_prime(15))
print(is_prime(2))
print(is_prime(3))
print(is_prime(17))
