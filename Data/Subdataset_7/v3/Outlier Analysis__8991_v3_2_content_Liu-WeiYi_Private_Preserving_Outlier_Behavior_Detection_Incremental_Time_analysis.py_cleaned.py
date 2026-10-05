import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def fonk1(filename):
    with open(filename, 'r+') as file:
        return [float(line.strip()) for line in file.readlines()]
def fonk2(b5):
    b1 = [b5[0]]
    for idx in range(1, len(b5)):
        b2 = b5[idx]
        b3 = b1[-1] + b2
        b1.append(b3)
    return b1
def fonk3(data, filename):
    with open(filename, 'w+') as file:
        for item in data:
            file.write(f"{item}\n")
def fonk4(b7, b6):
    sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
    plt.plot(b7, b6, b4 = 'o')
    plt.xlabel('Cumulative Accounts Number')
    plt.ylabel('Cumulative Time (ms)')
    plt.savefig('b1.pdf')
    plt.show()
b5 = fonk1('b5')
b1 = fonk2(b5)
b6 = [t * 1000 for t in b1]
fonk3(b6, 'b1.csv')
b7 = list(range(1, len(b6) + 1))
fonk4(b7, b6)