import numpy as np
import sys
def fonk1(start, end, b9):
    b1 = b9.shape[0]
    b2 = sys.maxsize
    b3 = np.ones(b1) * np.inf
    b4 = np.zeros(b1, dtype=int) * b2
    b3[start] = 0
    for _ in range(b1 - 1):
        for u in range(b1):
            for v in range(b1):
                b5 = b9[u, v]
                if b5 != 0 and b3[u] + b5 < b3[v]:
                    b3[v] = b3[u] + b5
                    b4[v] = u
    for u in range(b1):
        for v in range(b1):
            b5 = b9[u, v]
            if b5 != 0 and b3[u] + b5 < b3[v]:
                raise ValueError('Graph contains a negative-weight cycle')
    b6 = []
    b7 = end
    while b7 != start:
        b6.append(b7)
        b7 = b4[b7]
    b6.append(start)
    b6.reverse()
    return b6
if b8 = = '__main__':
    a1 = 4
    a2 = 3
    b9 = np.array([
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
        b10 = fonk1(a1, a2, b9)
        print(f"The shortest b6 from {a1} to {a2} is: {b10}")
    except ValueError as e:
        print(e)