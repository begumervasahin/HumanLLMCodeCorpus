import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def cubic_curve(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d
def get_data():
    x_values = []
    y_values = []
    folder_name = input('Enter the folder name:\n')
    folder_path = os.path.join(os.getcwd(), folder_name)
    for filename in os.listdir(folder_path):
        if filename != '.DS_Store':
            print(f"Processing file: {filename}")
            with open(os.path.join(folder_path, filename), 'r') as file:
                for line in file:
                    precision, recall = map(float, line.split())
                    x_values.append(recall)
                    y_values.append(precision)
    parameters, _ = curve_fit(cubic_curve, x_values, y_values)
    a, b, c, d = parameters
    x_interpolated = []
    y_interpolated = []
    current_recall = 0
    while current_recall <= 1:
        x_interpolated.append(current_recall)
        y_interpolated.append(cubic_curve(current_recall, a, b, c, d))
        current_recall += 0.2
    return x_interpolated, y_interpolated
recall_vs, precision_vs = get_data()
recall_fr, precision_fr = get_data()
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision vs Recall')
plt.plot(recall_vs, precision_vs, label='Vector Space Model', color='blue')
plt.scatter(recall_vs, precision_vs, color='blue')
plt.plot(recall_fr, precision_fr, label='Fuzzy Retrieval Model', color='red')
plt.scatter(recall_fr, precision_fr, color='red')
plt.legend()
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.grid(True)
plt.show()