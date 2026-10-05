import matplotlib.pyplot as plt
import numpy as np
def plot_simple(x_values, y_values, label):
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set(xlabel='Size N', ylabel='Execution Time', title=label)
    ax.grid()
    plt.show()
def plot_double(start, end, y1_values, label1, y2_values, label2):
    fig, ax = plt.subplots()
    ax.plot(range(start, end + 1), y1_values, label=label1)
    ax.plot(range(start, end + 1), y2_values, label=label2)
    ax.set(xlabel='Size N', ylabel='Execution Time', title=f"{label1} vs {label2}")
    plt.legend()
    plt.show()
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 20, 25, 30]
y2_values = [8, 13, 18, 23, 28]
plot_simple(x_values, y_values, "Simple Plot")
plot_double(0, 5, y_values, "First Line", y2_values, "Second Line")