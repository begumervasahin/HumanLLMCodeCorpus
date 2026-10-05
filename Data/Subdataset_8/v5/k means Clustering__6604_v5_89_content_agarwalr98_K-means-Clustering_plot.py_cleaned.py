import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
print("========== K MEANS CLUSTERING ===========\n")
class_colors = ['red', 'blue', 'green']
def read_data(file_path):
    data = []
    with open(file_path) as file:
        next(file)
        for line in file:
            data.append([float(val) for val in line.split()])
    return np.array(data)
data = read_data("Data/NonLinear/group03.txt")
for index, point in enumerate(data):
    if index < 300:
        plt.plot(point[0], point[1], "o", color=class_colors[0])
    elif 300 <= index < 800:
        plt.plot(point[0], point[1], "o", color=class_colors[1])
    else:
        plt.plot(point[0], point[1], "o", color=class_colors[2])
legend_handles = [Line2D([0], [0], color=color) for color in class_colors]
class_labels = ['Class 1', 'Class 2', 'Class 3']
plt.legend(legend_handles, class_labels)
plt.show()