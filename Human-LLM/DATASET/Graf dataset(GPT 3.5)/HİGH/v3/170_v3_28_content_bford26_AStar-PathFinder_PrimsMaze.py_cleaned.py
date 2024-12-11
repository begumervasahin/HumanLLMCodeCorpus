import numpy as np
from numpy.random import randint as rand
def fonk1(b1 = 81, height=51, complexity=.75, density=.75):
    b2 = ((height
    b3 = b2[0] * b2[1]
    b4 = int(complexity * (b3
    b5 = int(density * (b3
    b6 = np.zeros(b2, dtype=bool)
    b6[0, :] = b6[-1, :] = 1
    b6[:, 0] = b6[:, -1] = 1
    for _ in range(b5):
        start_x, b7 = rand(0, b2[1]
        b6[b7, start_x] = 1
        for _ in range(b4):
            b8 = []
            for dx, dy in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
                nx, b9 = start_x + dx, b7 + dy
                if 0 < nx < b2[1] and 0 < b9 < b2[0] and b6[b9, nx] == 0:
                    b8.append((b9, nx))
            if b8:
                new_y, b10 = b8[rand(0, len(b8) - 1)]
                b6[new_y, b10] = 1
                b6[b7 + (new_y - b7)
                start_x, b7 = b10, new_y
    return b6
b11 = fonk1()
print(b11)