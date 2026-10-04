def is_prime_number(num):
    if num < 2:
        return False
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True
def get_prime_numbers(n):
    if n < 2:
        return "Number should be greater than or equal to 2"
    prime_numbers = [num for num in range(2, n + 1) if is_prime_number(num)]
    return prime_numbers
def main():
    n = 10
    print(f"Prime numbers up to {n}: {get_prime_numbers(n)}")
if __name__ == "__main__":
    main()