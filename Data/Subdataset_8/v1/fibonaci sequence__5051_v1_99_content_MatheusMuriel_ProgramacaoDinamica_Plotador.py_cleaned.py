import matplotlib.pyplot as plt
import numpy as np
def plot_simple(x, y, label):
    xx = np.array(x)
    yy = np.array(y)
    fig, ax = plt.subplots()
    ax.plot(xx, yy)
    ax.set(xlabel='Size N', ylabel='Execution Time',
           title=label)
    ax.grid()
    plt.show()
def plot_double(start, end, y1, label1, y2, label2):
    yy1 = np.array(y1)
    yy2 = np.array(y2)
    max_time = max(max(y1), max(y2))
    x = range(start, end+1)
    y = range(0, int(max_time) + 1)
    fig, ax = plt.subplots()
    ax.plot(x, yy1, label=label1)
    ax.plot(x, yy2, label=label2)
    ax.set(xlabel='Size N', ylabel='Execution Time',
           title="{} vs {}".format(label1, label2))
    plt.legend()
    plt.show()
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 20, 25, 30]
y2_values = [8, 13, 18, 23, 28]
plot_simple(x_values, y_values, "Simple Plot")
plot_double(0, 5, y_values, "First Line", y2_values, "Second Line")