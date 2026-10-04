import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit
def cubic_function(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d
def read_data_from_folder(folder):
    x_data, y_data = [], []
    folder_path = os.path.join(os.getcwd(), folder)
    for filename in os.listdir(folder_path):
        if filename == '.DS_Store':
            continue
        print(f"Processing file: {filename}")
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            for line in file:
                values = line.split()
                y_data.append(float(values[0]))
                x_data.append(float(values[1]))
    return x_data, y_data
def fit_cubic_function(x_data, y_data):
    params, _ = curve_fit(cubic_function, x_data, y_data)
    a, b, c, d = params
    x_fit = [i/100 for i in range(0, 101, 20)]
    y_fit = [cubic_function(x, a, b, c, d) for x in x_fit]
    return x_fit, y_fit
def plot_precision_vs_recall(x1, y1, x2, y2):
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision vs Recall')
    plt.plot(x1, y1, label='Vector Space Model', marker='s', linestyle='-')
    plt.plot(x2, y2, label='Fuzzy Retrieval Model', marker='^', linestyle='-')
    plt.legend()
    plt.axis([0.0, 1.0, 0.0, 1.0])
    plt.show()
def main():
    folder1 = input('Folder name for Vector Space Model:\n')
    x_data1, y_data1 = read_data_from_folder(folder1)
    x_fit1, y_fit1 = fit_cubic_function(x_data1, y_data1)
    folder2 = input('Folder name for Fuzzy Retrieval Model:\n')
    x_data2, y_data2 = read_data_from_folder(folder2)
    x_fit2, y_fit2 = fit_cubic_function(x_data2, y_data2)
    plot_precision_vs_recall(x_fit1, y_fit1, x_fit2, y_fit2)
if __name__ == "__main__":
    main()