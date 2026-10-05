import numpy as np
import matplotlib.pyplot as plt
def set_axis_ranges(x_data, y_data):
    x_data_list = list(x_data)
    y_data_list = list(y_data)
    axes = plt.gca()
    x_width = max(x_data_list) - min(x_data_list)
    y_width = max(y_data_list) - min(y_data_list)
    buffer_factor = 1/3
    x_buffer = x_width * buffer_factor
    y_buffer = y_width * buffer_factor
    axes.set_xlim([min(x_data_list) - x_buffer, max(x_data_list) + x_buffer])
    axes.set_ylim([min(y_data_list) - y_buffer, max(y_data_list) + y_buffer])
    plt.gca().set_autoscale_on(False)
def plot_data(x_range, y_range, marker='o', color='k', label='Data Points'):
    plt.plot(x_range, y_range, marker, color=color, label=label)
def plot_function(x_data, function, linestyle='-', color='k', label='Function'):
    x_range = np.linspace(min(x_data) - 10, max(x_data) + 10, 1000)
    plt.plot(x_range, function(x_range), linestyle, color=color, label=label)
def show_all(legend_loc='lower right'):
    plt.legend(loc=legend_loc)
    plt.show()
x_data = np.linspace(0, 10, 100)
y_data = np.sin(x_data)
plot_data(x_data, y_data, marker='o', color='blue', label='Data Points')
def quadratic_function(x):
    return x**2 - 5*x + 6
plot_function(x_data, quadratic_function, linestyle='-', color='red', label='Quadratic Function')
set_axis_ranges(x_data, y_data)
show_all()