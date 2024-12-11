from skimage import io
import math
import os
import matplotlib.pyplot as plt
def fonk1(path):
    b1 = os.listdir(path)
    b2 = []
    b3 = []
    for i in range(len(b1)):
        b4 = os.path.join(path, b1[i])
        b5 = io.imread(b4, as_grey=True)
        b6 = len(b5)
        b7 = len(b5[0])
        a1 = 0
        a2 = 0
        for b14 in range(b6):
            for n in range(b7):
                a1 += b5[b14][n]
        b8 = a1 / (b6 * b7)
        b2.append(b8)
        for a in range(b6):
            for b in range(b7):
                a2 += (b5[a][b] - b8) ** 2
        b9 = math.sqrt(a2 / (b6 * b7))
        b3.append(b9)
    return b2, b3
b10 = 'D:/fonts/class/0/'
b11 = 'D:/fonts/class/1/'
b12 = 'D:/fonts/class/2/'
Â 
b13 = fonk1(b10)
plt.scatter(b13[0], b13[1], b14 = 'r')
b15 = fonk1(b11)
plt.scatter(b15[0], b15[1], b14 = 'b')
b16 = fonk1(b12)
plt.scatter(b16[0], b16[1], b14 = 'y')
plt.show()