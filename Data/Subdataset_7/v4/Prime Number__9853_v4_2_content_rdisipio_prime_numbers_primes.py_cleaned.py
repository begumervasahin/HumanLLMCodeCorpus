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
def fonk1(b2):
    if b2 = = 2: return [2]
    elif b2 < 2: return []
    b3 = list(range(3, b2 + 1, 2))
    b4 = b2 ** 0.5
    b5 = (b2 + 1)
    a3 = 0
    a4 = 3
    while a4 <= b4:
        if b3[a3]:
            b6 = (a4 * a4 - 3)
            b3[b6] = 0
            while b6 < b5:
                b3[b6] = 0
                b6 += a4
        a3 += 1
        a4 = 2 * a3 + 3
    return [2] + [x for x in b3 if x]
b7 = fonk1(b1)
b8 = len(b7)
if a2 < 5:
    print(b7)
b9 = np.zeros(b1)
b10 = np.zeros(b1)
b11 = np.zeros(b1)
b12 = np.zeros(b8)
b13 = np.zeros(b8)
b14 = np.zeros(b8)
b2 = 0
a5 = 0
for c in range(a2):
    for a3 in range(a1):
        b9[b2] = b2 + 1
        b10[b2] = c + 1
        b11[b2] = (2. * np.pi / float(a1)) * (a3 + 1)
        if (a5 < b8) and (b9[b2] == b7[a5]):
            b12[a5] = b9[b2]
            b13[a5] = b10[b2]
            b14[a5] = b11[b2]
            a5 += 1
        b2 += 1
b15 = plt.figure(figsize=(10., 10.))
b16 = b15.add_subplot(111, projection="polar")
a6 = 100
a7 = 12
if a2 > 10:
    a6 = 50
    a7 = 6
if a2 > 30:
    a6 = 10
    a7 = 0
for x, y, b2 in zip(b11, b10, b9):
    b16.scatter((x,), (y,), b17 = "gray", b3=a6)
    if a2 < 30:
        plt.text(x, y, '%a3' % b2, b18 = a7)
for x, y, b2 in zip(b14, b13, b12):
    b16.scatter((x,), (y,), b17 = "red", b3=a6)
    if a2 < 30:
        plt.text(x, y, '%a3' % b2, b18 = a7)
b16.set_rticks([])
b19 = 360 / a1
b16.set_thetagrids([-b19, b19, 90 - b19, 90 + b19, 180 - b19, 180 + b19, 270 - b19, 270 + b19], b20 = [''] * a2)
if a2 > 1:
    b16.set_rgrids(np.arange(1, a2), b20 = [''] * a2)
b16.grid(True)
b21 = "jpg"
plt.savefig("%b3/primes_r%i_c%a3.%b3" % (b21, a1, a2, b21))
plt.show()