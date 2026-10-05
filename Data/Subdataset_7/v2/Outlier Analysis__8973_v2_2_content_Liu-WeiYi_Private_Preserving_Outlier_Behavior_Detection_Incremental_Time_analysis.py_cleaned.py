import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = []
with open('b1', 'r+') as file:
    for line in file.readlines():
        b2 = float(line.strip())
        b1.append(b2)
b3 = [b1[0]]
for idx in range(1, len(b1)):
    b4 = b1[idx]
    b5 = b3[-1] + b4
    b3.append(b5)
b6 = [t * 1000 for t in b3]
with open('b3.csv', 'w+') as file:
    for time_ms in b6:
        file.write(str(time_ms) + '\n')
sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
b7 = list(range(1, len(b6) + 1))
b8 = sns.pointplot(x=b7, y=b6)
plt.xlabel('Cumulative Accounts Number')
plt.ylabel('Cumulative Time (ms)')
plt.savefig('b3.pdf')
plt.show()