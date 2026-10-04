import math
from typing import List
def divide_swing_and_conquer(number: int) -> int:
    if number <= 1:
        return 1
    primes = all_prime_numbers_up_to(number)
    exponents = prime_exponents_of_swing_number(number, primes)
    swinging_factorial = compute_swinging_factorial(primes, exponents)
    return divide_swing_and_conquer(number
def prime_exponents_of_swing_number(swing_number: int, primes: List[int]) -> List[int]:
    max_power = math.floor(math.log2(swing_number))
    exponents = []
    for prime in primes:
        exponent = 0
        for i in range(1, max_power + 1):
            exponent += swing_number
        exponents.append(exponent)
    return exponents
def compute_swinging_factorial(primes: List[int], exponents: List[int]) -> int:
    result = 1
    for prime, exponent in zip(primes, exponents):
        if exponent > 0:
            result *= prime ** exponent
    return result
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.isqrt(n)
    for divisor in range(3, max_divisor + 1, 2):
        if n % divisor == 0:
            return False
    return True
def all_prime_numbers_up_to(n: int) -> List[int]:
    return [num for num in range(2, n + 1) if is_prime(num)]
if __name__ == "__main__":
    try:
        n = int(input('Enter a number to compute its swinging factorial: '))
        if n < 0:
            raise ValueError("The number must be a non-negative integer.")
        print(f"The swinging factorial of {n} is: {divide_swing_and_conquer(n)}")
    except ValueError as e:
        print(f"Error: {e}")