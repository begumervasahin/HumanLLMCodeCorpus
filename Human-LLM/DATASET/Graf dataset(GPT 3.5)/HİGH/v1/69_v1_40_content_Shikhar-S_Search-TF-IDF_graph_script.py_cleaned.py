import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def fonk1(b1, a, b, c, b7):
    return a * b1 ** 3 + b * b1 ** 2 + c * b1 + b7
def fonk2(folder):
    b1 = []
    b2 = []
    b3 = os.getcwd()
    b4 = os.path.join(b3, folder)
    for filename in os.listdir(b4):
        if filename != '.DS_Store':
            with open(os.path.join(b4, filename), 'r') as f:
                for b5 in f:
                    b5 = b5.split()
                    b2.append(float(b5[0]))
                    b1.append(float(b5[1]))
    params, b6 = curve_fit(func, b1, b2)
    a, b, c, b7 = params
    b8 = []
    b9 = []
    a1 = 0
    while a1 <= 1:
        b8.append(a1)
        b9.append(fonk1(a1, a, b, c, b7))
        a1 += 0.2
    return b8, b9
p_v, b10 = fonk2('Vector_Space_Model')
p_f, b11 = fonk2('Fuzzy_Retrieval_Model')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs Recall')
plt.plot(p_v, b10, b12 = 'Vector Space Model')
plt.plot(p_v, b10, 'bs')
plt.plot(p_f, b11, b12 = 'Fuzzy Retrieval Model')
plt.plot(p_f, b11, 'r^')
plt.legend()
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.show()