import sys
import numpy as np
import matplotlib.pyplot as plt
a1 = 24
a2 = 2
if len(sys.argv) > 1:
    a2 = int(sys.argv[1])
if len(sys.argv) > 2:
    a1 = int(sys.argv[2])
b1 = a2 * a1
def fonk1(n):
    if n < 2:
        return []
    b2 = np.ones(n
    for i in range(1, int(n**0.5)
        if b2[i]:
            b2[2*i*(i+1)::2*i+1] = False
    return [2] + [2*i+1 for i in range(1, n
b3 = fonk1(b1)
b4 = len(b3)
if a2 < 5:
    print(b3)
b5 = np.arange(1, b1 + 1)
b6 = np.repeat(np.arange(1, a2 + 1), a1)
b7 = np.tile(np.linspace(0, 2 * np.pi, a1, endpoint=False), a2)
b8 = np.array([n for n in b3 if n <= b1])
b9 = b6[np.isin(b5, b8)]
b10 = b7[np.isin(b5, b8)]
b11 = plt.figure(figsize=(10, 10))
b12 = b11.add_subplot(111, projection="polar")
b13 = 100 if a2 <= 10 else 50 if a2 <= 30 else 10
b14 = 12 if a2 <= 10 else 6 if a2 <= 30 else 0
b12.scatter(b7, b6, b15 = "gray", s=b13)
if a2 < 30:
    for x, y, n in zip(b7, b6, b5):
        b12.text(x, y, f'{n}', b16 = b14)
b12.scatter(b10, b9, b15 = "red", s=b13)
if a2 < 30:
    for x, y, n in zip(b10, b9, b8):
        b12.text(x, y, f'{n}', b16 = b14)
b12.set_rticks([])
b12.set_thetagrids(range(0, 360, int(360 / a1)), b17 = [''] * a1)
if a2 > 1:
    b12.set_rgrids(np.arange(1, a2 + 1), b17 = [''] * a2)
b12.grid(True)
plt.savefig(f"primes_r{a1}_c{a2}.jpg")
plt.show()