def is_prime_number(num):
    if num < 2:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
def get_prime_numbers(n):
    if n < 2:
        return "Number should be greater than or equal to 2"
    prime_numbers = []
    for num in range(2, n + 1):
        if is_prime_number(num):
            prime_numbers.append(num)
    return prime_numbers
if __name__ == "__main__":
    print(get_prime_numbers(10))