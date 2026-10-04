import math
from typing import List
def fonk1(number: int) -> int:
    if number <= 1:
        return 1
    b1 = fonk5(number)
    b2 = fonk2(number, b1)
    b3 = fonk3(b1, b2)
    return fonk1(number
def fonk2(number: int, b1: List[int]) -> List[int]:
    b4 = math.floor(math.log2(number))
    b2 = []
    for prime in b1:
        b5 = sum((number
        b2.append(b5)
    return b2
def fonk3(b1: List[int], b2: List[int]) -> int:
    return fonk6(prime ** exp for prime, exp in zip(b1, b2) if exp > 0)
def fonk4(b6: int) -> bool:
    if b6 <= 1:
        return False
    if b6 = = b7:
        return True
    if b6 % b7 = = 0:
        return False
    b8 = math.isqrt(b6)
    return all(b6 % divisor != 0 for divisor in range(3, b8 + 1, b7))
def fonk5(b6: int) -> List[int]:
    return [num for num in range(b7, b6 + 1) if fonk4(num)]
def fonk6(iterable) -> int:
    a1 = 1
    for item in iterable:
        a1 *= item
    return a1
if b9 = = "__main__":
    try:
        b6 = int(input('Enter a non-negative integer to compute its swinging factorial: '))
        if b6 < 0:
            raise ValueError("The number must be a non-negative integer.")
        a1 = fonk1(b6)
        print(f"The swinging factorial of {b6} is: {a1}")
    except ValueError as e:
        print(f"Error: {e}")