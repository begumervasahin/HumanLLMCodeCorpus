import matplotlib.pyplot as plt
import numpy as np
def plot_simple(x, y, label):
    xx = np.array(x)
    yy = np.array(y)
    fig, ax = plt.subplots()
    ax.plot(xx, yy)
    ax.set(xlabel='Tamanho N', ylabel='Tempo de execução', title=label)
    ax.grid()
    plt.show()
def plot_double(start, end, y1, label1, y2, label2):
    yy1 = np.array(y1)
    yy2 = np.array(y2)
    max_time = max(max(y1), max(y2))
    x = range(start, end + 1)
    fig, ax = plt.subplots()
    ax.plot(x, yy1, label=label1)
    ax.plot(x, yy2, label=label2)
    ax.set(xlabel='Tamanho N', ylabel='Tempo de execução', title=f"{label1} x {label2}")
    plt.legend()
    plt.show()
if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y_simple = [2, 3, 5, 7, 11]
    plot_simple(x, y_simple, "Simple Plot")
    y1_double = [1, 4, 9, 16, 25]
    y2_double = [2, 6, 12, 20, 30]
    plot_double(1, 5, y1_double, "Quadratic", y2_double, "Linear")