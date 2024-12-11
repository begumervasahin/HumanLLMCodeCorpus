import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def fonk1(x, a, b, c, b8):
    return a * x * x * x + b * x * x + c * x + b8
def fonk2():
    b1 = []
    b2 = []
    b3 = input('Enter the folder name:\n')
    b4 = os.getcwd()
    b5 = os.path.join(b4, b3)
    a1 = 0
    for filename in os.listdir(b5):
        if filename != '.DS_Store':
            a1 += 1
            print(filename)
            with open(os.path.join(b5, filename), 'r') as file:
                for line in file:
                    b6 = line.split()
                    b2.append(float(b6[0]))
                    b1.append(float(b6[1]))
    parameters, b7 = curve_fit(cubic_function, b1, b2)
    a, b, c, b8 = parameters
    b9 = []
    b10 = []
    a2 = 0
    while a2 <= 1:
        b9.append(a2)
        b10.append(fonk1(a2, a, b, c, b8))
        a2 += 0.2
    return b9, b10
recall_v, b11 = fonk2()
recall_f, b12 = fonk2()
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs Recall')
plt.plot(recall_v, b11, b13 = 'Vector Space Model')
plt.plot(recall_v, b11, 'bs')
plt.plot(recall_f, b12, b13 = 'Fuzzy Retrieval Model')
plt.plot(recall_f, b12, 'r^')
plt.legend()
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.show()