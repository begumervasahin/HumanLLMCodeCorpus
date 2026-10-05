import sys
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def print_prime_numbers(low, high):
    prime_nums = [str(num) for num in range(low, high) if is_prime(num)]
    prime_str = ' '.join(prime_nums)
    sys.stdout.write(f"Prime Numbers in range ({low}, {high}): {prime_str}\n")
def main():
    print_prime_numbers(2, 100000)
if __name__ == "__main__":
    main()