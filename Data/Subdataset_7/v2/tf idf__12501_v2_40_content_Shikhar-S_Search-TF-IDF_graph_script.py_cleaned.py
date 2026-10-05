import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def fonk1(x, a, b, c, b7):
    return a * x ** 3 + b * x ** 2 + c * x + b7
def fonk2(folder):
    b1 = []
    b2 = []
    b3 = os.getcwd()
    b4 = os.path.join(b3, folder)
    for filename in os.listdir(b4):
        if filename != '.DS_Store':
            with open(os.path.join(b4, filename), 'r') as file:
                for line in file:
                    precision, b5 = map(float, line.split())
                    b1.append(b5)
                    b2.append(precision)
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
