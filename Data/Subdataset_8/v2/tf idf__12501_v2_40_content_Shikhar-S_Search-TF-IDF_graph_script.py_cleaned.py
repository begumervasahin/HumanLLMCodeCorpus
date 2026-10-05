import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def func(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d
def getData(folder):
    x_data = []
    y_data = []
    cwd = os.getcwd()
    folder_path = os.path.join(cwd, folder)
    for filename in os.listdir(folder_path):
        if filename != '.DS_Store':
            with open(os.path.join(folder_path, filename), 'r') as file:
                for line in file:
                    precision, recall = map(float, line.split())
                    x_data.append(recall)
                    y_data.append(precision)
    params, _ = curve_fit(func, x_data, y_data)
    a, b, c, d = params
    x_final = []
    y_final = []
    i = 0
    while i <= 1:
        x_final.append(i)
        y_final.append(func(i, a, b, c, d))
        i += 0.2
    return x_final, y_final
p_v, q_v = getData('Vector_Space_Model')
p_f, q_f = getData('Fuzzy_Retrieval_Model')
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
