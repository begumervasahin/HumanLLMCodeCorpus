import matplotlib.pyplot as plt
import numpy as np
def plot_simple(x, y, title):
    x_values = np.array(x)
    y_values = np.array(y)
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, marker='o', linestyle='-')
    ax.set_xlabel('Tamanho N')
    ax.set_ylabel('Tempo de execução')
    ax.set_title(title)
    ax.grid(True)
    plt.show()
def plot_double(start, end, y1, label1, y2, label2):
    x_values = range(start, end + 1)
    y1_values = np.array(y1)
    y2_values = np.array(y2)
    fig, ax = plt.subplots()
    ax.plot(x_values, y1_values, marker='o', linestyle='-', label=label1)
    ax.plot(x_values, y2_values, marker='s', linestyle='--', label=label2)
    ax.set_xlabel('Tamanho N')
    ax.set_ylabel('Tempo de execução')
    ax.set_title(f"{label1} vs {label2}")
    ax.legend()
    ax.grid(True)
    plt.show()
if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y_simple = [2, 3, 5, 7, 11]
    plot_simple(x, y_simple, "Simple Plot")
    y1_double = [1, 4, 9, 16, 25]
    y2_double = [2, 6, 12, 20, 30]
    plot_double(1, 5, y1_double, "Quadratic", y2_double, "Linear")