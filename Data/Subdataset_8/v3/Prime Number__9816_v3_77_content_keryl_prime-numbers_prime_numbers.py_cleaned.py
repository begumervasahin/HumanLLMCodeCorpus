def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True
def get_prime_numbers(limit):
    if limit < 2:
        return "Limit should be greater than or equal to 2"
    prime_numbers = []
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
if __name__ == "__main__":
    print(get_prime_numbers(10))