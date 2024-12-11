import random
from collections import defaultdict
print_dead, b1 = '-', '*'
a1 = 3
b2 = (3, 3)
b3 = defaultdict(int, {
    (1, 2): 1,
    (1, 3): 1,
    (0, 3): 1,
})
b4 = defaultdict(int)
b4[(1, 0)], b4[(1, 1)], b4[(1, 2)] = 1, 1, 1
for generation in range(a1):
    print("\nGeneration %3i:" % generation)
    for row in range(b2[1]):
        print("  ", ''.join(str(b4[(row, col)])
                            for col in range(b2[0])).replace(
            '0', print_dead).replace('1', b1)
        )
    b5 = defaultdict(int)
    for row in range(b2[1]):
        for col in range(b2[0]):
            b6 = sum(b4[(r, c)]
                                for r in range(row - 1, row + 2)
                                for c in range(col - 1, col + 2)
                                if (r, c) != (row, col))
            b5[(row, col)] = b3[
                (b4[(row, col)], b6)
            ]
    b4 = b5