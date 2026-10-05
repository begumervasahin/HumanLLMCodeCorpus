import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
all_time = []
with open('all_time', 'r+') as file:
    for line in file.readlines():
        time = float(line.strip())
        all_time.append(time)
incremental_time = [all_time[0]]
for idx in range(1, len(all_time)):
    time_interval = all_time[idx]
    incremental_time_value = incremental_time[-1] + time_interval
    incremental_time.append(incremental_time_value)
incremental_time_ms = [t * 1000 for t in incremental_time]
with open('incremental_time.csv', 'w+') as file:
    for time_ms in incremental_time_ms:
        file.write(str(time_ms) + '\n')
sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
x_values = list(range(1, len(incremental_time_ms) + 1))
plot = sns.pointplot(x=x_values, y=incremental_time_ms)
plt.xlabel('Cumulative Accounts Number')
plt.ylabel('Cumulative Time (ms)')
plt.savefig('incremental_time.pdf')
plt.show()