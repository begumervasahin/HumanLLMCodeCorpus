import os
import math
import matplotlib.pyplot as plt
from skimage import io
def fonk1(b6):
    b1 = b6.mean()
    b2 = math.sqrt(((b6 - b1) ** 2).mean())
    return b1, b2
def fonk2(directory):
    b3 = []
    b4 = []
    for image_name in os.listdir(directory):
        b5 = os.path.join(directory, image_name)
        b6 = io.imread(b5, as_gray=True)
        b1, b2 = fonk1(b6)
        b3.append(b1)
        b4.append(b2)
    return b3, b4
b7 = ['D:/fonts/class/0/', 'D:/fonts/class/1/', 'D:/fonts/class/2/']
b8 = [fonk2(directory) for directory in b7]
b9 = ['r', 'b', 'y']
b10 = ['Class 0', 'Class 1', 'Class 2']
for cluster, color, label in zip(b8, b9, b10):
    plt.scatter(cluster[0], cluster[1], b11 = color, label=label)
plt.xlabel('Mean Intensity')
plt.ylabel('Variance')
plt.legend()
plt.show()