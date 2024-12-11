from skimage import io
import math
import os
import matplotlib.pyplot as plt
def fonk1(path):
    b1 = os.listdir(path)
    b2 = []
    b3 = []
    for filename in b1:
        b4 = os.path.join(path, filename)
        b5 = io.imread(b4, as_gray=True)
        row, b6 = b5.shape
        b7 = b5.sum()
        b8 = b7 / (row * b6)
        b2.append(b8)
        b9 = ((b5 - b8) ** 2).sum()
        b10 = math.sqrt(b9 / (row * b6))
        b3.append(b10)
    return b2, b3
b11 = 'D:/fonts/class/0/'
b12 = 'D:/fonts/class/1/'
b13 = 'D:/fonts/class/2/'
b14 = fonk1(b11)
plt.scatter(b14[0], b14[1], b15 = 'r', label='Class 0')
b16 = fonk1(b12)
plt.scatter(b16[0], b16[1], b15 = 'b', label='Class 1')
b17 = fonk1(b13)
plt.scatter(b17[0], b17[1], b15 = 'y', label='Class 2')
plt.xlabel('Mean')
plt.ylabel('Variance')
plt.legend()
plt.title('Scatter plot of Mean vs Variance for Different Classes')
plt.show()