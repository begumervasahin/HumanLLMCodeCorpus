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
    b5 = []
    for prime in b1:
        a1 = 0
        for i in range(1, b4 + 1):
            a1 += number
        b5.append(a1)
    return b5
def fonk3(b1: List[int], b5: List[int]) -> int:
    a2 = 1
    for prime, a1 in zip(b1, b5):
        if a1 > 0:
            a2 *= prime ** a1
    return a2
def fonk4(b6: int) -> bool:
    if b6 <= 1:
        return False
    if b6 = = b7:
        return True
    if b6 % b7 = = 0:
        return False
    b8 = math.isqrt(b6)
    for b9 in range(3, b8 + 1, b7):
        if b6 % b9 = = 0:
            return False
    return True
def fonk5(b6: int) -> List[int]:
    return [num for num in range(b7, b6 + 1) if fonk4(num)]
if b10 = = "__main__":
    try:
        b6 = int(input('Enter a non-negative integer to compute its swinging factorial: '))
        if b6 < 0:
            raise ValueError("The number must be a non-negative integer.")
        print(f"The swinging factorial of {b6} is: {fonk1(b6)}")
    except ValueError as e:
        print(f"Error: {e}")