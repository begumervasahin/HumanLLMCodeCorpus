import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def fonk1(filename):
    b1 = []
    with open(filename, 'r') as file:
        for line in file:
            b2 = float(line.strip())
            b1.append(b2)
    return b1
def fonk2(b1):
    b3 = [b1[0]]
    for interval in b1[1:]:
        b3.append(b3[-1] + interval)
    return [t * 1000 for t in b3]
def fonk3(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')
def fonk4(b8, y_values):
    sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
    plt.plot(b8, y_values, b4 = 'o')
    plt.xlabel('Cumulative Accounts Number')
    plt.ylabel('Cumulative Time (ms)')
    plt.savefig('cumulative_time.pdf')
    plt.show()
if b5 = = "__main__":
    b6 = fonk1('all_time')
    b7 = fonk2(b6)
    fonk3('cumulative_time.csv', b7)
    b8 = list(range(1, len(b7) + 1))
    fonk4(b8, b7)