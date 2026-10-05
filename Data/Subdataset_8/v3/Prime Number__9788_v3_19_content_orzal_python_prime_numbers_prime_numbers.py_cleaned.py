def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def print_prime_factors(n):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n
            break
if __name__ == "__main__":
    print("Prime numbers from 2 to 99:")
    for num in range(2, 100):
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print_prime_factors(num)