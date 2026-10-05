import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import random
print("========== K MEANS b1 = ==========\n")
b2 = ['red', 'blue', 'green']
a1 = 0
with open("b3/NonLinear/group03.txt") as myfile:
    next(myfile)
    for b4 in myfile:
        a1 = a1 + 1
a2 = 0
b3 = np.zeros(shape = (int(a1), int(2)), dtype = float)
with open("b3/NonLinear/group03.txt") as myfile:
    next(myfile)
    for b4 in myfile:
        b4 = b4.split()
        b3[a2][0] = float(b4[0])
        b3[a2][1] = float(b4[1])
        a2 = a2 + 1
a2 = 0
for b4 in b3:
    if a2<300:
        plt.plot(float(b4[0]), float(b4[1]), "o", b5 = b2[0])
    elif a2 >=300 and a2 <800:
        plt.plot(float(b4[0]), float(b4[1]),  "o", b5 = b2[1])
    else:
        plt.plot(float(b4[0]), float(b4[1]), "o",b5 = b2[2])
    a2 = a2 + 1
b6 = [Line2D([0], [0], b5=c) for c in b2]
b7 = ['Class 1', 'Class 2', 'Class 3']
plt.legend(b6, b7)
plt.show()