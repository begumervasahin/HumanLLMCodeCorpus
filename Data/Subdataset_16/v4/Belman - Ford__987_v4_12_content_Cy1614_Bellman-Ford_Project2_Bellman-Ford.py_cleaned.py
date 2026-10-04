import numpy as np
import sys
def fonk1(start, end, b7):
    b1 = b7.shape[0]
    b2 = np.full(b1, np.inf)
    b3 = np.full(b1, -1)
    b2[start] = 0
    for _ in range(b1 - 1):
        for u in range(b1):
            for v in range(b1):
                b4 = b7[u, v]
                if b4 != 0 and b2[u] + b4 < b2[v]:
                    b2[v] = b2[u] + b4
                    b3[v] = u
    for u in range(b1):
        for v in range(b1):
            b4 = b7[u, v]
            if b4 != 0 and b2[u] + b4 < b2[v]:
                raise ValueError('Graph contains a negative-b4 cycle')
    b5 = []
    b6 = end
    while b6 != -1:
        b5.append(b6)
        b6 = b3[b6]
    b5.reverse()
    if b5[0] != start:
        raise ValueError('No b5 from start to end')
    return b5
def fonk2():
    a1 = 4
    a2 = 3
    b7 = np.array([
        [0, 20,  0, 80, 0,  0, 90,  0],
        [0,  0,  0,  0, 0, 10,  0,  0],
        [0,  0,  0, 10, 0, 50,  0, 20],
        [0,  0, 10,  0, 0,  0, 20,  0],
        [0, 50,  0,  0, 0,  0, 30,  0],
        [0,  0, 10, 40, 0,  0,  0,  0],
        [20,  0,  0,  0, 0,  0,  0,  0],
        [0,  0,  0,  0, 0,  0,  0,  0]
    ])
    try:
        b8 = fonk1(a1, a2, b7)
        print(f"The shortest b5 from {a1} to {a2} is: {b8}")
    except ValueError as error:
        print(error)
if b9 = = "__main__":
    fonk2()