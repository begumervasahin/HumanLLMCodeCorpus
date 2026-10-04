import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
all_time = []
with open('all_time','r+') as f:
    for line in f.readlines():
        time = float(line.strip())
        all_time.append(time)
incremental_time = [all_time[0]]
for idx in range(1,len(all_time)):
    time_interval = all_time[idx]
    incrementalT = incremental_time[-1]+time_interval
    incremental_time.append(incrementalT)
incremental_time = [t*1000 for t in incremental_time]
with open('incrementa_time.csv','w+') as f:
    for t in incremental_time:
        f.write(str(t))
        f.write('\n')
sns.set_style("darkgrid", {'font.family':'serif','font.serif':'Times New Roman'})
x = list(range(1, len(incremental_time)+1))
plot = sns.pointplot(x=x, y=incremental_time)
plt.xlabel('Cumulative Accounts Number')
plt.ylabel('Cumulative Time (ms)')
plt.savefig('incremental_time.pdf')
plt.show()