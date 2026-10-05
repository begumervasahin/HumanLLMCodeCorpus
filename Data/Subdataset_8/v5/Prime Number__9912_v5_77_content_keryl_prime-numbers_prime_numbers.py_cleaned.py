def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True
def get_prime_numbers(up_to):
    if up_to < 2:
        return "Error: Number should be greater than or equal to 2"
    primes = [num for num in range(2, up_to + 1) if is_prime(num)]
    return primes
if __name__ == "__main__":
    print(get_prime_numbers(10))