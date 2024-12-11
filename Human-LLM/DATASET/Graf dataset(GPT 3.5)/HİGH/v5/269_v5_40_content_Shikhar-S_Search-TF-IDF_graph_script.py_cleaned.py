import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def fonk1(x, a, b, c, b7):
    return a * x ** 3 + b * x ** 2 + c * x + b7
def fonk2():
    b1 = []
    b2 = []
    b3 = input('Enter the folder name:\n')
    b4 = os.path.join(os.getcwd(), b3)
    for filename in os.listdir(b4):
        if filename != '.DS_Store':
            print(f"Processing file: {filename}")
            with open(os.path.join(b4, filename), 'r') as file:
                for line in file:
                    precision, b5 = map(float, line.split())
                    b1.append(b5)
                    b2.append(precision)
    parameters, b6 = curve_fit(cubic_curve, b1, b2)
    a, b, c, b7 = parameters
    b8 = []
    b9 = []
    a1 = 0
    while a1 <= 1:
        b8.append(a1)
        b9.append(fonk1(a1, a, b, c, b7))
        a1 += 0.2
    return b8, b9
recall_vs, b10 = fonk2()
recall_fr, b11 = fonk2()
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs Recall')
plt.plot(recall_vs, b10, b12 = 'Vector Space Model', b13='blue')
plt.scatter(recall_vs, b10, b13 = 'blue')
plt.plot(recall_fr, b11, b12 = 'Fuzzy Retrieval Model', b13='red')
plt.scatter(recall_fr, b11, b13 = 'red')
plt.legend()
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.grid(True)
plt.show()