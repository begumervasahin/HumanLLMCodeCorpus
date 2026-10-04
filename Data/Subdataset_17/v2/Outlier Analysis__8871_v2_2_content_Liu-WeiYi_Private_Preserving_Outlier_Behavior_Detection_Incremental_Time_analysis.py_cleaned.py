import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
all_time = []
with open('all_time', 'r') as file:
    for line in file:
        time = float(line.strip())
        all_time.append(time)
incremental_time = [all_time[0]]
for idx in range(1, len(all_time)):
    incremental_time.append(incremental_time[-1] + all_time[idx])
incremental_time = [t * 1000 for t in incremental_time]
with open('incremental_time.csv', 'w') as file:
    for t in incremental_time:
        file.write(f"{t}\n")
sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
x_values = list(range(1, len(incremental_time) + 1))
plt.figure(figsize=(10, 6))
sns.pointplot(x=x_values, y=incremental_time)
plt.xlabel('Cumulative Accounts Number')
plt.ylabel('Cumulative Time (ms)')
plt.title('Cumulative Time vs. Cumulative Accounts Number')
plt.savefig('incremental_time.pdf')
plt.show()