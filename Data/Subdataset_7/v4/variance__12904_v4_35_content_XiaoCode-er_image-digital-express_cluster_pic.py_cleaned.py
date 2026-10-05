import os
import math
import matplotlib.pyplot as plt
from skimage import io
def fonk1(b8):
    b1 = io.imread(b8, as_gray=True)
    rows, b2 = b1.shape
    a1 = 0
    for i in range(rows):
        for j in range(b2):
            a1 += b1[i][j]
    b3 = a1 / (rows * b2)
    a2 = 0
    for i in range(rows):
        for j in range(b2):
            a2 += (b1[i][j] - b3) ** 2
    b4 = math.sqrt(a2 / (rows * b2))
    return b3, b4
def fonk2(directory):
    b5 = os.listdir(directory)
    b6 = []
    b7 = []
    for image_name in b5:
        b8 = os.path.join(directory, image_name)
        b3, b4 = fonk1(b8)
        b6.append(b3)
        b7.append(b4)
    return b6, b7
b9 = 'D:/fonts/class/0/'
b10 = 'D:/fonts/class/1/'
b11 = 'D:/fonts/class/2/'
b12 = fonk2(b9)
b13 = fonk2(b10)
b14 = fonk2(b11)
plt.scatter(b12[0], b12[1], b15 = 'r', label='Class 0')
plt.scatter(b13[0], b13[1], b15 = 'b', label='Class 1')
plt.scatter(b14[0], b14[1], b15 = 'y', label='Class 2')
plt.xlabel('Mean Intensity')
plt.ylabel('Variance')
plt.legend()
plt.show()