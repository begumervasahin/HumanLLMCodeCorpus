import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
print("========== K MEANS b1 = ==========\n")
b2 = ['red', 'blue', 'green']
def fonk1(file_path):
    b3 = []
    with open(file_path) as file:
        next(file)
        for line in file:
            b3.append([float(val) for val in line.split()])
    return np.array(b3)
b3 = fonk1("Data/NonLinear/group03.txt")
for index, point in enumerate(b3):
    if index < 300:
        plt.plot(point[0], point[1], "o", b4 = b2[0])
    elif 300 <= index < 800:
        plt.plot(point[0], point[1], "o", b4 = b2[1])
    else:
        plt.plot(point[0], point[1], "o", b4 = b2[2])
b5 = [Line2D([0], [0], b4=b4) for b4 in b2]
b6 = ['Class 1', 'Class 2', 'Class 3']
plt.legend(b5, b6)
plt.show()