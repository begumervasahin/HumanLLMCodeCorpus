
PRIMES_UP_TO_2017 = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    1997, 1999, 2003, 2011, 2017
)
def is_prime(n):
    if n < 2 or any(n % prime == 0 for prime in PRIMES_UP_TO_2017):
        return False
    return True
numbers_to_test = [5, 10, 13, 17, 20, 23, 29, 30, 31, 37, 40, 41, 47, 50]
for num in numbers_to_test:
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")