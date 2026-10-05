from skimage import io
import math
import os
import matplotlib.pyplot as plt
def fonk1(directory):
    b1 = os.listdir(directory)
    b2 = []
    b3 = []
    for filename in b1:
        b4 = os.path.join(directory, filename)
        b5 = io.imread(b4, as_gray=True)
        rows, b6 = b5.shape
        b7 = b5.sum()
        b8 = b7 / (rows * b6)
        b2.append(b8)
        b9 = ((b5 - b8) ** 2).sum()
        b10 = math.sqrt(b9 / (rows * b6))
        b3.append(b10)
    return b2, b3
b11 = 'D:/fonts/class/0/'
b12 = 'D:/fonts/class/1/'
b13 = 'D:/fonts/class/2/'
class_0_mean, b14 = fonk1(b11)
class_1_mean, b15 = fonk1(b12)
class_2_mean, b16 = fonk1(b13)
plt.scatter(class_0_mean, b14, b17 = 'r', label='Class 0')
plt.scatter(class_1_mean, b15, b17 = 'b', label='Class 1')
plt.scatter(class_2_mean, b16, b17 = 'y', label='Class 2')
plt.xlabel('Mean Brightness')
plt.ylabel('Variance of Brightness')
plt.legend()
plt.title('Scatter plot of Mean vs Variance for Different Classes')
plt.show()