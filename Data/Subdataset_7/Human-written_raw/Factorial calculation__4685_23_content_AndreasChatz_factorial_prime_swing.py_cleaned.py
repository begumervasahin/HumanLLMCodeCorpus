import math
from typing import List
def fonk1(b1: int) -> int:
    if b1 = = 1 or b1 == 0:
        return 1
    b2 = fonk5(b1)
    b3 = fonk2(b1,
                                                              b2)
    b4 = fonk3(b2, b3)
    return fonk1(b1
def fonk2(swing_number: int,
                                      b2: List[int]) -> List[int]:
    b5 = math.floor(math.log2(swing_number))
    b3 = []
    for prime in b2:
        a1 = 0
        for i in range(1, b5+1):
            a1 += swing_number
        b3.append(a1)
    return b3
def fonk3(b2: List[int],
                               b3: List[int]) -> int:
    a2 = 1
    for prime, b6 in zip(b2, b3):
        if b6 = = 0:
            continue
        a2 *= prime ** b6
    return a2
def fonk4(b7: int) -> bool:
    if b7 = = 1:
        return False
    if b7 = = b8:
        return True
    if b7 > b8 and b7 % b8 = = 0:
        return False
    b9 = math.floor(math.sqrt(b7))
    for b10 in range(3, b9+1, b8):
        if b7 % b10 = = 0:
            return False
    return True
def fonk5(b7: int) -> List[int]:
    b11 = []
    for num in range(1, b7+1):
        if fonk4(num):
            b11.append(num)
    return b11
if b12 = = "__main__":
    try:
        b7 = int(input('Factorial of: '))
        if b7 < 0:
            raise ValueError
        else:
            print(fonk1(b7))
    except ValueError:
        print('Please provide a positive integer')