import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def fonk1(x, a, b, c, b7):
    return a * x**3 + b * x**2 + c * x + b7
def fonk2(folder):
    x_data, b1 = [], []
    b2 = os.path.join(os.getcwd(), folder)
    for b3 in os.listdir(b2):
        if b3 = = '.DS_Store':
            continue
        print(f"Processing file: {b3}")
        b4 = os.path.join(b2, b3)
        with open(b4, 'r') as file:
            for line in file:
                b5 = line.split()
                b1.append(float(b5[0]))
                x_data.append(float(b5[1]))
    return x_data, b1
def fonk3(x_data, b1):
    params, b6 = curve_fit(cubic_function, x_data, b1)
    a, b, c, b7 = params
    b8 = [i/100 for i in range(0, 101, 20)]
    b9 = [fonk1(x, a, b, c, b7) for x in b8]
    return b8, b9
def fonk4(x1, y1, x2, y2):
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision vs Recall')
    plt.plot(x1, y1, b10 = 'Vector Space Model', marker='s', linestyle='-')
    plt.plot(x2, y2, b10 = 'Fuzzy Retrieval Model', marker='^', linestyle='-')
    plt.legend()
    plt.axis([0.0, 1.0, 0.0, 1.0])
    plt.show()
def fonk5():
    b11 = input('Folder name for Vector Space Model:\n')
    x_data1, b12 = fonk2(b11)
    x_fit1, b13 = fonk3(x_data1, b12)
    b14 = input('Folder name for Fuzzy Retrieval Model:\n')
    x_data2, b15 = fonk2(b14)
    x_fit2, b16 = fonk3(x_data2, b15)
    fonk4(x_fit1, b13, x_fit2, b16)
if b17 = = "__main__":
    fonk5()