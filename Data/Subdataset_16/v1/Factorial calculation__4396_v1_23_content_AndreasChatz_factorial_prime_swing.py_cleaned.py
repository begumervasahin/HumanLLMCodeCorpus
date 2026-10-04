import math
from typing import List
def fonk1(number: int) -> int:
    if number <= 1:
        return 1
    b1 = fonk5(number)
    b2 = fonk2(number, b1)
    b3 = fonk3(b1, b2)
    return fonk1(number
def fonk2(swing_number: int, b1: List[int]) -> List[int]:
    b4 = math.floor(math.log2(swing_number))
    b2 = []
    for prime in b1:
        a1 = 0
        for i in range(1, b4 + 1):
            a1 += swing_number
        b2.append(a1)
    return b2
def fonk3(b1: List[int], b2: List[int]) -> int:
    a2 = 1
    for prime, a1 in zip(b1, b2):
        if a1 != 0:
            a2 *= prime ** a1
    return a2
def fonk4(b5: int) -> bool:
    if b5 <= 1:
        return False
    if b5 = = b6:
        return True
    if b5 % b6 = = 0:
        return False
    b7 = math.isqrt(b5)
    for b8 in range(3, b7 + 1, b6):
        if b5 % b8 = = 0:
            return False
    return True
def fonk5(b5: int) -> List[int]:
    return [num for num in range(b6, b5 + 1) if fonk4(num)]
if b9 = = "__main__":
    try:
        b5 = int(input('Factorial of: '))
        if b5 < 0:
            raise ValueError
        print(fonk1(b5))
    except ValueError:
        print('Please provide a positive integer.')