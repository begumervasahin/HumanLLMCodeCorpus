import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def cubic_function(x, a, b, c, d):
    return a * x * x * x + b * x * x + c * x + d
def get_data():
    x_values = []
    y_values = []
    folder_name = input('Enter the folder name:\n')
    cwd = os.getcwd()
    folder_path = os.path.join(cwd, folder_name)
    count = 0
    for filename in os.listdir(folder_path):
        if filename != '.DS_Store':
            count += 1
            print(filename)
            with open(os.path.join(folder_path, filename), 'r') as file:
                for line in file:
                    data = line.split()
                    y_values.append(float(data[0]))
                    x_values.append(float(data[1]))
    parameters, _ = curve_fit(cubic_function, x_values, y_values)
    a, b, c, d = parameters
    x_final = []
    y_final = []
    i = 0
    while i <= 1:
        x_final.append(i)
        y_final.append(cubic_function(i, a, b, c, d))
        i += 0.2
    return x_final, y_final
recall_v, precision_v = get_data()
recall_f, precision_f = get_data()
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs Recall')
plt.plot(recall_v, precision_v, label='Vector Space Model')
plt.plot(recall_v, precision_v, 'bs')
plt.plot(recall_f, precision_f, label='Fuzzy Retrieval Model')
plt.plot(recall_f, precision_f, 'r^')
plt.legend()
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.show()