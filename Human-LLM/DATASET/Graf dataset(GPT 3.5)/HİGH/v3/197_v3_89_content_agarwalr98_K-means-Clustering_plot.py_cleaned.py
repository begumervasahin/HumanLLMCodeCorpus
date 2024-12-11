import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
def fonk1(file_path):
    b1 = []
    with open(file_path) as file:
        next(file)
        for line in file:
            b2 = line.split()
            b1.append([float(value) for value in b2])
    return np.array(b1)
def fonk2(b1, b6):
    for index, point in enumerate(b1):
        a1 = 0
        if index >= 300 and index < 800:
            a1 = 1
        elif index >= 800:
            a1 = 2
        plt.plot(point[0], point[1], "o", b3 = b6[a1])
def fonk3(b6, b7):
    b4 = [Line2D([0], [0], b3=b3, marker='o', linestyle='None')
                       for b3 in b6]
    plt.legend(b4, b7)
def fonk4():
    print("========== K MEANS b5 = ==========\n")
    b6 = ['red', 'blue', 'green']
    b7 = ['Class 1', 'Class 2', 'Class 3']
    b1 = fonk1("Data/NonLinear/group03.txt")
    fonk2(b1, b6)
    fonk3(b6, b7)
    plt.show()
if b8 = = "__main__":
    fonk4()