import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def read_time_intervals_from_file(filename):
    time_intervals = []
    with open(filename, 'r') as file:
        for line in file:
            time_interval = float(line.strip())
            time_intervals.append(time_interval)
    return time_intervals
def calculate_cumulative_time_intervals(time_intervals):
    cumulative_intervals = [time_intervals[0]]
    for interval in time_intervals[1:]:
        cumulative_intervals.append(cumulative_intervals[-1] + interval)
    return [t * 1000 for t in cumulative_intervals]
def save_to_csv(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')
def plot_cumulative_time_intervals(x_values, y_values):
    sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Cumulative Accounts Number')
    plt.ylabel('Cumulative Time (ms)')
    plt.savefig('cumulative_time.pdf')
    plt.show()
if __name__ == "__main__":
    all_time_intervals = read_time_intervals_from_file('all_time')
    cumulative_time_intervals = calculate_cumulative_time_intervals(all_time_intervals)
    save_to_csv('cumulative_time.csv', cumulative_time_intervals)
    x_values = list(range(1, len(cumulative_time_intervals) + 1))
    plot_cumulative_time_intervals(x_values, cumulative_time_intervals)