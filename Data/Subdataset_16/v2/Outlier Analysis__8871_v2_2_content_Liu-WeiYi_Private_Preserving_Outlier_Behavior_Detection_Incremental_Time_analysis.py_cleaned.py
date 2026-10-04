import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = []
with open('b1', 'r') as file:
    for line in file:
        b2 = float(line.strip())
        b1.append(b2)
b3 = [b1[0]]
for idx in range(1, len(b1)):
    b3.append(b3[-1] + b1[idx])
b3 = [t * 1000 for t in b3]
with open('b3.csv', 'w') as file:
    for t in b3:
        file.write(f"{t}\n")
sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
b4 = list(range(1, len(b3) + 1))
plt.figure(b5 = (10, 6))
sns.pointplot(b6 = b4, y=b3)
plt.xlabel('Cumulative Accounts Number')
plt.ylabel('Cumulative Time (ms)')
plt.title('Cumulative Time vs. Cumulative Accounts Number')
plt.savefig('b3.pdf')
plt.show()