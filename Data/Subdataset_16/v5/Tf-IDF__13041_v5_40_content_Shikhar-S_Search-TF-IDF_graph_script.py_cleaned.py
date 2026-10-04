import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def fonk1(x, a, b, c, b7):
    return a * x**3 + b * x**2 + c * x + b7
def fonk2(b11):
    x, b1 = [], []
    b2 = os.path.join(os.getcwd(), b11)
    for b3 in os.listdir(b2):
        if b3 = = '.DS_Store':
            continue
        print(f"Processing file: {b3}")
        b4 = os.path.join(b2, b3)
        with open(b4, 'r') as file:
            for line in file:
                b5 = line.split()
                b1.append(float(b5[0]))
                x.append(float(b5[1]))
    return x, b1
def fonk3(x, b1):
    params, b6 = curve_fit(func, x, b1)
    return params
def fonk4(params):
    a, b, c, b7 = params
    b8 = [i for i in range(11)]
    b9 = [fonk1(i / 10, a, b, c, b7) for i in b8]
    b8 = [i / 10 for i in b8]
    return b8, b9
def fonk5(x_vsm, b12, x_fuzzy, b14):
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision vs Recall')
    plt.plot(x_vsm, b12, b10 = 'Vector Space Model')
    plt.plot(x_vsm, b12, 'bs')
    plt.plot(x_fuzzy, b14, b10 = 'Fuzzy Retrieval Model')
    plt.plot(x_fuzzy, b14, 'r^')
    plt.legend()
    plt.axis([0.0, 1.0, 0.0, 1.0])
    plt.show()
def fonk6():
    b11 = input('Folder name:\n')
    x_vsm, b12 = fonk2(b11)
    b13 = fonk3(x_vsm, b12)
    x_vsm, b12 = fonk4(b13)
    x_fuzzy, b14 = fonk2(b11)
    b15 = fonk3(x_fuzzy, b14)
    x_fuzzy, b14 = fonk4(b15)
    fonk5(x_vsm, b12, x_fuzzy, b14)
if b16 = = "__main__":
    fonk6()