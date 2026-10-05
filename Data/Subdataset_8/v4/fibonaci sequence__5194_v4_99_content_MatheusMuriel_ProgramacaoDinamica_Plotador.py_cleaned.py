import matplotlib.pyplot as plt
import numpy as np
def plot_simple(x_values, y_values, label):
    x_values = np.array(x_values)
    y_values = np.array(y_values)
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.set(xlabel='Tamanho N', ylabel='Tempo de execução', title=label)
    ax.grid()
    plt.show()
def plot_double(start, end, y1_values, label1, y2_values, label2):
    y1_values = np.array(y1_values)
    y2_values = np.array(y2_values)
    max_time_y1 = max(y1_values)
    max_time_y2 = max(y2_values)
    max_time = max(max_time_y1, max_time_y2)
    x_values = range(start, end + 1)
    y_values = range(0, int(max_time) + 1)
    fig, ax = plt.subplots()
    ax.plot(x_values, y1_values, label=label1)
    ax.plot(x_values, y2_values, label=label2)
    ax.set(xlabel='Tamanho N', ylabel='Tempo de execução',
           title="{} x {}".format(label1, label2))
    plt.legend()
    plt.show()