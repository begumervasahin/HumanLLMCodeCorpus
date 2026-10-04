import matplotlib.pyplot as plt
import os
import sys
from scipy.optimize import curve_fit
import math
def func(x, a, b, c, d):
    return a*x*x*x + b*x*x + c*x + d
def getData(folder):
    x = []
    y = []
    pth = os.path.join(os.getcwd(), folder)
    count = 0
    for filename in os.listdir(pth):
        if filename != '.DS_Store':
            count += 1
            print(filename)
            with open(os.path.join(pth, filename), 'r') as F:
                for line in F:
                    line = line.split()
                    y.append(float(line[0]))
                    x.append(float(line[1]))
    x_final = []
    y_final = []
    params, _ = curve_fit(func, x, y)
    [a, b, c, d] = params
    i = 0
    while i <= 1:
        x_final.append(i)
        y_final.append(func(i, a, b, c, d))
        i += 0.2
    return x_final, y_final
folder1 = input('Folder name for Vector Space Model:\n')
(p_v, q_v) = getData(folder1)
folder2 = input('Folder name for Fuzzy Retrieval Model:\n')
(p_f, q_f) = getData(folder2)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs Recall')
plt.plot(p_v, q_v, label='Vector Space Model')
plt.plot(p_v, q_v, 'bs')
plt.plot(p_f, q_f, label='Fuzzy Retrieval Model')
plt.plot(p_f, q_f, 'r^')
plt.legend()
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.show()