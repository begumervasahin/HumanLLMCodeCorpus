import matplotlib.pyplot as plt
import os
import sys
from scipy.optimize import curve_fit
import math
def fonk1(b1, a, b, c, d):
    return a*b1*b1*b1 + b*b1*b1 + c*b1 + d
def fonk2(folder):
    b1 = []
    b2 = []
    b3 = os.path.join(os.getcwd(), folder)
    a1 = 0
    for filename in os.listdir(b3):
        if filename != '.DS_Store':
            a1 += 1
            print(filename)
            with open(os.path.join(b3, filename), 'r') as F:
                for b4 in F:
                    b4 = b4.split()
                    b2.append(float(b4[0]))
                    b1.append(float(b4[1]))
    b5 = []
    b6 = []
    params, b7 = curve_fit(func, b1, b2)
    [a, b, c, d] = params
    a2 = 0
    while a2 <= 1:
        b5.append(a2)
        b6.append(fonk1(a2, a, b, c, d))
        a2 += 0.2
    return b5, b6
b8 = input('Folder name for Vector Space Model:\n')
(p_v, q_v) = fonk2(b8)
b9 = input('Folder name for Fuzzy Retrieval Model:\n')
(p_f, q_f) = fonk2(b9)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs Recall')
plt.plot(p_v, q_v, b10 = 'Vector Space Model')
plt.plot(p_v, q_v, 'bs')
plt.plot(p_f, q_f, b10 = 'Fuzzy Retrieval Model')
plt.plot(p_f, q_f, 'r^')
plt.legend()
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.show()