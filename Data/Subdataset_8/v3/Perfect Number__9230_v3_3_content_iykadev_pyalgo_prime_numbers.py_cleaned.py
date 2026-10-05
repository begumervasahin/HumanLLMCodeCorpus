import sys
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_prime_numbers_in_range(low_num, high_num):
    print(f"Prime Numbers in range ({low_num},{high_num}): ", end="")
    prime_numbers = (num for num in range(low_num, high_num) if is_prime(num))
    print(*prime_numbers, sep=" ")
def main():
    find_prime_numbers_in_range(2, 100000)
if __name__ == "__main__":
    main()