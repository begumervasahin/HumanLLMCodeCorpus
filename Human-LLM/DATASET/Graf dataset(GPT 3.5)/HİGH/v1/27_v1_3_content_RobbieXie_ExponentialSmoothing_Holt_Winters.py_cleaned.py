import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, s):
    b1 = np.zeros(s.shape)
    b1[0] = s[0]
    for i in range(1, len(b1)):
        b1[i] = a1 * s[i] + (1 - a1) * b1[i - 1]
    return b1
def fonk2(b27, b6, b8, b17, b26):
    year, time_id, b2 = b8.T
    plt.figure(b3 = (14, 6), dpi=80)
    plt.plot(year, b2, b4 = 'blue', label="actual value")
    plt.plot(b27[1:], b17[2:],
             b4 = 'red', label="double predicted value")
    plt.plot(b27[1:], b26[2:],
             b4 = 'green', label="triple predicted value")
    plt.legend(b5 = 'lower right')
    plt.title('Projects')
    plt.xlabel('year')
    plt.ylabel('b2')
    plt.xticks(b27)
    plt.show()
def fonk3():
    a1 = .70
    b6 = np.array([2016, 2017])
    b7 = r'data1.txt'
    b8 = np.loadtxt(b7)
    year, time_id, b2 = b8.T
    b9 = np.array([0, 0, b2[0]])
    b10 = np.insert(b8, 0, values=b9, b21=0)
    initial_year, initial_time_id, b11 = b10.T
    b12 = fonk1(a1, b11)
    b13 = fonk1(a1, b12)
    b14 = np.zeros(b12.shape)
    for i in range(1, len(initial_time_id)):
        b14[i] = a1 * b11[i - 1] + (1 - a1) * b12[i - 1]
    b15 = 2 * b12 - b13
    b16 = (a1 / (1 - a1)) * (b12 - b13)
    b17 = np.zeros(b13.shape)
    for i in range(1, len(initial_time_id)):
        b17[i] = b15[i - 1] + b16[i - 1]
    b18 = b15[-1] + b16[-1] * 1
    b19 = b15[-1] + b16[-1] * 2
    b20 = np.array([b18, b19])
    b17 = np.insert(b17, len(b17), values=np.array(
        [b18, b19]), b21 = 0)
    b22 = fonk1(a1, b13)
    b23 = 3 * b12 - 3 * b13 + b22
    b24 = (a1 / (2 * ((1 - a1) ** 2))) * (
                (6 - 5 * a1) * b12 - 2 * ((5 - 4 * a1) * b13) + (4 - 3 * a1) * b22)
    b25 = ((a1 ** 2) / (2 * ((1 - a1) ** 2))) * (b12 - 2 * b13 + b22)
    b26 = np.zeros(b22.shape)
    for i in range(1, len(initial_time_id)):
        b26[i] = b23[i - 1] + b24[i - 1] * 1 + b25[i - 1] * (1 ** 2)
    b18 = b23[-1] + b24[-1] * 1 + b25[-1] * (1 ** 2)
    b19 = b23[-1] + b24[-1] * 2 + b25[-1] * (2 ** 2)
    b20 = np.array([b18, b19])
    b26 = np.insert(b26, len(b26), values=np.array(
        [b18, b19]), b21 = 0)
    b27 = np.insert(year, len(year), values=b6, b21=0)
    b28 = np.array([b27, b17, b26])
    print(b28)
    fonk2(b27, b6, b8, b17, b26)
if b29 = = '__main__':
    fonk3()