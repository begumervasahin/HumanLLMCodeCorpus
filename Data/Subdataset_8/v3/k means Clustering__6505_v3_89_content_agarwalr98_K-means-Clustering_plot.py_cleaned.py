import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
def read_data(file_path):
    data = []
    with open(file_path) as file:
        next(file)
        for line in file:
            values = line.split()
            data.append([float(value) for value in values])
    return np.array(data)
def plot_data(data, colors):
    for index, point in enumerate(data):
        color_index = 0
        if index >= 300 and index < 800:
            color_index = 1
        elif index >= 800:
            color_index = 2
        plt.plot(point[0], point[1], "o", color=colors[color_index])
def create_legend(colors, labels):
    legend_elements = [Line2D([0], [0], color=color, marker='o', linestyle='None')
                       for color in colors]
    plt.legend(legend_elements, labels)
def main():
    print("========== K MEANS CLUSTERING ===========\n")
    colors = ['red', 'blue', 'green']
    labels = ['Class 1', 'Class 2', 'Class 3']
    data = read_data("Data/NonLinear/group03.txt")
    plot_data(data, colors)
    create_legend(colors, labels)
    plt.show()
if __name__ == "__main__":
    main()