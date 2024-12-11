import math
from typing import List
def fonk1(b1: int) -> int:
    if b1 = = 1 or b1 == 0:
        return 1
    b2 = fonk5(b1)
    b3 = fonk2(b1, b2)
    b4 = fonk3(b2, b3)
    return fonk1(b1
def fonk2(swing_number: int, b2: List[int]) -> List[int]:
    b5 = math.floor(math.log2(swing_number))
    b3 = []
    for prime in b2:
        a1 = 0
        for i in range(1, b5 + 1):
            a1 += swing_number
        b3.append(a1)
    return b3
def fonk3(b2: List[int], b3: List[int]) -> int:
    b4 = 1
    for prime, a1 in zip(b2, b3):
        if a1 = = 0:
            continue
        b4 *= prime ** a1
    return b4
def fonk4(b6: int) -> bool:
    if b6 = = 1:
        return False
    if b6 = = b7:
        return True
    if b6 > b7 and b6 % b7 = = 0:
        return False
    b8 = math.floor(math.sqrt(b6))
    for b9 in range(3, b8 + 1, b7):
        if b6 % b9 = = 0:
            return False
    return True
def fonk5(b6: int) -> List[int]:
    b2 = []
    for num in range(b7, b6 + 1):
        if fonk4(num):
            b2.append(num)
    return b2
if b10 = = "__main__":
    try:
        b6 = int(input('Factorial of: '))
        if b6 < 0:
            raise ValueError
        else:
            print(fonk1(b6))
    except ValueError:
        print('Please provide a positive integer')