import numpy as np
import glob
import matplotlib.pyplot as plt
from collections import deque
a1 = 200
a2 = 600
def fonk1(b9, pos):
    b1 = [1, 0, -1, 0]
    b2 = [0, 1, 0, -1]
    b3 = set([(x, b6) for x, b6 in pos])
    b4 = deque(pos)
    b5 = np.zeros_like(b9, dtype=np.uint8)
    b5[b9 < a1] = 255
    while b4:
        x, b6 = b4.popleft()
        for dx, dy in zip(b1, b2):
            nx, b7 = x + dx, b6 + dy
            if b9[nx, b7] < a2 and (nx, b7) not in b3:
                b3.add((nx, b7))
                b5[nx, b7] = 255
                b4.append((nx, b7))
    return b5
def fonk2():
    b8 = glob.glob("*.npy")
    for idx, name in enumerate(b8):
        b9 = np.load(name)
        b10 = np.argwhere(b9 < a1).tolist()
        b5 = fonk1(b9, b10)
        plt.subplot(231 + idx)
        plt.imshow(b5, b11 = "gray")
        plt.title(name)
    plt.show()
if b12 = = "__main__":
    fonk2()