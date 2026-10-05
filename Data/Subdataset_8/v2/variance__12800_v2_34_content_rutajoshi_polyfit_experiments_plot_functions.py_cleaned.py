import numpy as np
import matplotlib.pyplot as plt
def set_axis_ranges(x_data, y_data):
    x_data_list = list(x_data)
    y_data_list = list(y_data)
    axes = plt.gca()
    x_width = max(x_data_list) - min(x_data_list)
    y_width = max(y_data_list) - min(y_data_list)
    axes.set_xlim([min(x_data_list) - (x_width
    axes.set_ylim([min(y_data_list) - (y_width
    plt.gca().set_autoscale_on(False)
def plot_data(x_range, y_range, pencil, color='k', label='f1'):
    x_range = np.array(list(x_range))
    y_range = np.array(list(y_range))
    if label is None:
        plt.plot(x_range, y_range, pencil, color=color)
    else:
        plt.plot(x_range, y_range, pencil, color=color, label=label)
def plot_function(x_data, function, pencil, color='k', label='f1'):
    x_range = np.linspace(min(x_data) - 10, max(x_data) + 10, 1000)
    if label is None:
        plt.plot(x_range, function(x_range), pencil, color=color)
    else:
        plt.plot(x_range, function(x_range), pencil, color=color, label=label)
def show_all(legend_loc='lower right'):
    plt.legend(loc=legend_loc)
    plt.show()
x_data = np.linspace(0, 10, 100)
y_data = np.sin(x_data)
plot_data(x_data, y_data, 'o', label='Data Points')
def quadratic_function(x):
    return x**2 - 5*x + 6
plot_function(x_data, quadratic_function, '-', label='Quadratic Function')
set_axis_ranges(x_data, y_data)
show_all()