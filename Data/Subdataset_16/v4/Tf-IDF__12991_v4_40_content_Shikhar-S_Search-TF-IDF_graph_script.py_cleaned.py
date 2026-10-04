import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def fonk1(b1, a, b, c, b9):
    return a * b1**3 + b * b1**2 + c * b1 + b9
def fonk2():
    b1 = []
    b2 = []
    b3 = os.getcwd()
    b4 = input('Folder name:\n')
    b5 = os.path.join(b3, b4)
    for b6 in os.listdir(b5):
        if b6 = = '.DS_Store':
            continue
        print(b6)
        with open(os.path.join(b5, b6), 'r') as file:
            for line in file:
                b7 = line.split()
                b2.append(float(b7[0]))
                b1.append(float(b7[1]))
    params, b8 = curve_fit(func, b1, b2)
    a, b, c, b9 = params
    b10 = []
    b11 = []
    a1 = 0
    while a1 <= 1:
        b10.append(a1)
        b11.append(fonk1(a1, a, b, c, b9))
        a1 += 0.2
    return b10, b11
x_vsm, b12 = fonk2()
x_fuzzy, b13 = fonk2()
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs Recall')
plt.plot(x_vsm, b12, b14 = 'Vector Space Model')
plt.plot(x_vsm, b12, 'bs')
plt.plot(x_fuzzy, b13, b14 = 'Fuzzy Retrieval Model')
plt.plot(x_fuzzy, b13, 'r^')
plt.legend()
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.show()