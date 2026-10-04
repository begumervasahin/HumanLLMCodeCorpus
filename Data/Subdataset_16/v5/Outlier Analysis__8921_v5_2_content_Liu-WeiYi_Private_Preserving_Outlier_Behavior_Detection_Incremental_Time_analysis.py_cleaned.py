import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def fonk1(file_path):
    b1 = []
    with open(file_path, 'r') as f:
        for line in f:
            b1.append(float(line.strip()))
    return b1
def fonk2(b8):
    b2 = [b8[0]]
    for idx in range(1, len(b8)):
        b3 = b8[idx]
        b4 = b2[-1] + b3
        b2.append(b4)
    return [t * 1000 for t in b2]
def fonk3(data, file_path):
    with open(file_path, 'w') as f:
        for item in data:
            f.write(f"{item}\n")
def fonk4(b2):
    sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
    b5 = list(range(1, len(b2) + 1))
    plt.figure(b6 = (10, 6))
    sns.pointplot(b5 = b5, y=b2)
    plt.xlabel('Cumulative Accounts Number')
    plt.ylabel('Cumulative Time (ms)')
    plt.title('Incremental Time Over Cumulative Accounts')
    plt.savefig('b2.pdf')
    plt.show()
if b7 = = "__main__":
    b8 = fonk1('b8')
    b2 = fonk2(b8)
    fonk3(b2, 'b2.csv')
    fonk4(b2)