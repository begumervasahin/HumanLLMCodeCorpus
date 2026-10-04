import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def fonk1(x, a, b, c, b7):
    return a * x**3 + b * x**2 + c * x + b7
def fonk2(folder):
    x, b1 = [], []
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
                x.append(float(b5[1]))
    params, b6 = curve_fit(func, x, b1)
    a, b, c, b7 = params
    b8 = [i for i in range(0, 101, 20)]
    b9 = [fonk1(i/100, a, b, c, b7) for i in b8]
    return b8, b9
def fonk3():
    b10 = input('Folder name for Vector Space Model:\n')
    p_v, b11 = fonk2(b10)
    b12 = input('Folder name for Fuzzy Retrieval Model:\n')
    p_f, b13 = fonk2(b12)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision vs Recall')
    plt.plot(p_v, b11, b14 = 'Vector Space Model')
    plt.plot(p_v, b11, 'bs')
    plt.plot(p_f, b13, b14 = 'Fuzzy Retrieval Model')
    plt.plot(p_f, b13, 'r^')
    plt.legend()
    plt.axis([0.0, 1.0, 0.0, 1.0])
    plt.show()
if b15 = = "__main__":
    fonk3()