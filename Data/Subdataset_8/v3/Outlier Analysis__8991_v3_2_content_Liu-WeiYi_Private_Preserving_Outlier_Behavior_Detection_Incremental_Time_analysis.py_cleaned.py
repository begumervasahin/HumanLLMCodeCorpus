import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def read_time_data(filename):
    with open(filename, 'r+') as file:
        return [float(line.strip()) for line in file.readlines()]
def calculate_incremental_time(all_time):
    incremental_time = [all_time[0]]
    for idx in range(1, len(all_time)):
        time_interval = all_time[idx]
        incremental_time_value = incremental_time[-1] + time_interval
        incremental_time.append(incremental_time_value)
    return incremental_time
def save_to_csv(data, filename):
    with open(filename, 'w+') as file:
        for item in data:
            file.write(f"{item}\n")
def plot_incremental_time(x_values, incremental_time_ms):
    sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
    plt.plot(x_values, incremental_time_ms, marker='o')
    plt.xlabel('Cumulative Accounts Number')
    plt.ylabel('Cumulative Time (ms)')
    plt.savefig('incremental_time.pdf')
    plt.show()
all_time = read_time_data('all_time')
incremental_time = calculate_incremental_time(all_time)
incremental_time_ms = [t * 1000 for t in incremental_time]
save_to_csv(incremental_time_ms, 'incremental_time.csv')
x_values = list(range(1, len(incremental_time_ms) + 1))
plot_incremental_time(x_values, incremental_time_ms)