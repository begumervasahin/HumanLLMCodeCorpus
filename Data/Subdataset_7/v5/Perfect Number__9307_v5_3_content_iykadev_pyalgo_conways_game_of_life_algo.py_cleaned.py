import random
from collections import defaultdict
DEAD_CELL, b1 = '-', '*'
a1 = 3
b2 = (3, 3)
b3 = defaultdict(int, {
    (1, 2): 1,
    (1, 3): 1,
    (0, 3): 1,
})
def fonk1(generation, b6):
    print("\nGeneration %3i:" % generation)
    for row in range(b2[1]):
        print("  ", ''.join(str(b6[(row, col)])
                            for col in range(b2[0])).replace(
            '0', DEAD_CELL).replace('1', b1)
        )
def fonk2(b6):
    b4 = defaultdict(int)
    for row in range(b2[1]):
        for col in range(b2[0]):
            b5 = sum(b6[(r, c)]
                                for r in range(row - 1, row + 2)
                                for c in range(col - 1, col + 2)
                                if (r, c) != (row, col))
            b4[(row, col)] = b3[
                (b6[(row, col)], b5)
            ]
    return b4
def fonk3():
    b6 = defaultdict(int)
    for row in range(b2[1]):
        for col in range(b2[0]):
            b6[(row, col)] = random.randint(0, 1)
    return b6
def fonk4():
    b6 = fonk3()
    for generation in range(a1):
        fonk1(generation, b6)
        b6 = fonk2(b6)
if b7 = = "__main__":
    fonk4()