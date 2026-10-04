import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
b1 = []
with open('b1','r+') as f:
    for line in f.readlines():
        b2 = float(line.strip())
        b1.append(b2)
b3 = [b1[0]]
for idx in range(1,len(b1)):
    b4 = b1[idx]
    b5 = b3[-1]+b4
    b3.append(b5)
b3 = [t*1000 for t in b3]
with open('incrementa_time.csv','w+') as f:
    for t in b3:
        f.write(str(t))
        f.write('\n')
sns.set_style("darkgrid", {'font.family':'serif','font.serif':'Times New Roman'})
b6 = list(range(1, len(b3)+1))
b7 = sns.pointplot(b6=b6, y=b3)
plt.xlabel('Cumulative Accounts Number')
plt.ylabel('Cumulative Time (ms)')
plt.savefig('b3.pdf')
plt.show()