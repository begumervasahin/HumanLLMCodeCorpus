import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
all_time_intervals = []
with open('all_time', 'r+') as file:
    for line in file.readlines():
        time_interval = float(line.strip())
        all_time_intervals.append(time_interval)
cumulative_time_intervals = [all_time_intervals[0]]
for idx in range(1, len(all_time_intervals)):
    current_time_interval = all_time_intervals[idx]
    cumulative_time = cumulative_time_intervals[-1] + current_time_interval
    cumulative_time_intervals.append(cumulative_time)
cumulative_time_intervals = [t * 1000 for t in cumulative_time_intervals]
with open('cumulative_time.csv', 'w+') as file:
    for t in cumulative_time_intervals:
        file.write(str(t))
        file.write('\n')
sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
x_values = list(range(1, len(cumulative_time_intervals) + 1))
plot = sns.pointplot(x=x_values, y=cumulative_time_intervals)
plt.xlabel('Cumulative Accounts Number')
plt.ylabel('Cumulative Time (ms)')
plt.savefig('cumulative_time.pdf')
plt.show()