import numpy as np
import glob
import matplotlib.pyplot as plt
from collections import deque
a1 = 200
a2 = 600
def fonk1(b9, b10):
    b1 = [1, 0, -1, 0]
    b2 = [0, 1, 0, -1]
    b3 = set(b10)
    b4 = deque(b10)
    b5 = np.zeros_like(b9, dtype=np.uint8)
    b5[b9 < a1] = 255
    while b4:
        x, b6 = b4.popleft()
        for dx, dy in zip(b1, b2):
            nx, b7 = x + dx, b6 + dy
            if (0 <= nx < b9.shape[0] and 0 <= b7 < b9.shape[1] and
                    b9[nx, b7] < a2 and (nx, b7) not in b3):
                b3.add((nx, b7))
                b5[nx, b7] = 255
                b4.append((nx, b7))
    return b5
def fonk2():
    b8 = glob.glob("*.npy")
    for idx, filename in enumerate(b8):
        b9 = np.load(filename)
        b10 = np.argwhere(b9 < a1).tolist()
        b5 = fonk1(b9, b10)
        plt.subplot(231 + idx)
        plt.imshow(b5, b11 = "gray")
        plt.title(filename)
    plt.show()
if b12 = = "__main__":
    fonk2()