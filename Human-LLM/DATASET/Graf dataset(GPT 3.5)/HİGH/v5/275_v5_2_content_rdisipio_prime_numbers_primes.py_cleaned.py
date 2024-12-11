import sys
import numpy as np
import matplotlib.pyplot as plt
a1 = 24
a2 = 2
if len(sys.argv) > 1:
    b1 = int(sys.argv[1])
else:
    b1 = a2
if len(sys.argv) > 2:
    b2 = int(sys.argv[2])
else:
    b2 = a1
b3 = b1 * b2
def fonk1(b4):
    if b4 = = 2:
        return [2]
    elif b4 < 2:
        return []
    b5 = list(range(3, b4 + 1, 2))
    b6 = b4 ** 0.5
    b7 = (b4 + 1)
    a3 = 0
    a4 = 3
    while a4 <= b6:
        if b5[a3]:
            b8 = (a4 * a4 - 3)
            b5[b8] = 0
            while b8 < b7:
                b5[b8] = 0
                b8 += a4
        a3 += 1
        a4 = 2 * a3 + 3
    return [2] + [x for x in b5 if x]
b9 = fonk1(b3)
b10 = len(b9)
if b1 < 5:
    print(b9)
b11 = np.zeros(b3)
b12 = np.zeros(b3)
b13 = np.zeros(b3)
b14 = np.zeros(b10)
b15 = np.zeros(b10)
b16 = np.zeros(b10)
b4 = 0
a5 = 0
for c in range(b1):
    for a3 in range(b2):
        b11[b4] = b4 + 1
        b12[b4] = c + 1
        b13[b4] = (2. * np.pi / float(b2)) * (a3 + 1)
        if (a5 < b10) and (b11[b4] == b9[a5]):
            b14[a5] = b11[b4]
            b15[a5] = b12[b4]
            b16[a5] = b13[b4]
            a5 += 1
        b4 += 1
b17 = plt.figure(figsize=(10., 10.))
b18 = b17.add_subplot(111, projection="polar")
a6 = 100
a7 = 12
if b1 > 10:
    a6 = 50
    a7 = 6
if b1 > 30:
    a6 = 10
    a7 = 0
for x, y, b4 in zip(b13, b12, b11):
    b18.scatter((x,), (y,), b19 = "gray", s=a6)
    if b1 < 30:
        plt.text(x, y, '%a3' % b4, b20 = a7)
for x, y, b4 in zip(b16, b15, b14):
    b18.scatter((x,), (y,), b19 = "red", s=a6)
    if b1 < 30:
        plt.text(x, y, '%a3' % b4, b20 = a7)
b18.set_rticks([])
b21 = 360 / b2
b18.set_thetagrids([-b21, b21, 90 - b21, 90 + b21, 180 - b21, 180 + b21, 270 - b21, 270 + b21], b22 = [''] * b1)
if b1 > 1:
    b18.set_rgrids(np.arange(1, b1), b22 = [''] * b1)
b18.grid(True)
b23 = "jpg"
plt.savefig("%s/primes_r%i_c%a3.%s" % (b23, b2, b1, b23))
plt.show()