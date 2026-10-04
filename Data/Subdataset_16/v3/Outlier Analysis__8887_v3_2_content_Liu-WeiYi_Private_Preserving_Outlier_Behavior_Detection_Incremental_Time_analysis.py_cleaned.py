import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def fonk1(filename):
    b1 = []
    with open(filename, 'r') as file:
        for line in file:
            b1.append(float(line.strip()))
    return b1
def fonk2(b1):
    b2 = [b1[0]]
    for idx in range(1, len(b1)):
        b2.append(b2[-1] + b1[idx])
    return [t * 1000 for t in b2]
def fonk3(filename, data):
    with open(filename, 'w') as file:
        for value in data:
            file.write(f"{value}\n")
def fonk4(b8, y_values, output_filename):
    sns.set_style("darkgrid", {'font.family': 'serif', 'font.serif': 'Times New Roman'})
    plt.figure(b3 = (10, 6))
    sns.pointplot(b4 = b8, y=y_values)
    plt.xlabel('Cumulative Accounts Number')
    plt.ylabel('Cumulative Time (ms)')
    plt.title('Cumulative Time vs. Cumulative Accounts Number')
    plt.savefig(output_filename)
    plt.show()
if b5 = = "__main__":
    b6 = fonk1('b6')
    b7 = fonk2(b6)
    fonk3('b7.csv', b7)
    b8 = list(range(1, len(b7) + 1))
    fonk4(b8, b7, 'b7.pdf')