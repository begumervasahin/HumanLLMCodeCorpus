import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, s):
    b1 = np.zeros(s.shape)
    b1[0] = s[0]
    for i in range(1, len(s)):
        b1[i] = a1 * s[i] + (1 - a1) * b1[i - 1]
    return b1
def fonk2(b22, b6, b8, b17, b21):
    year, time_id, b2 = b8.T
    plt.figure(b3 = (14, 6), dpi=80)
    plt.plot(year, b2, b4 = 'blue', label="Actual Value")
    plt.plot(b22[1:], b17[2:], b4 = 'red', label="Double Predicted Value")
    plt.plot(b22[1:], b21[2:], b4 = 'green', label="Triple Predicted Value")
    plt.legend(b5 = 'lower right')
    plt.title('Projects')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.xticks(b22)
    plt.show()
def fonk3():
    a1 = 0.70
    b6 = np.array([2016, 2017])
    b7 = 'data1.txt'
    b8 = np.loadtxt(b7)
    year, time_id, b2 = b8.T
    b9 = np.array([0, 0, b2[0]])
    b10 = np.insert(b8, 0, values=b9, b23=0)
    initial_year, initial_time_id, b11 = b10.T
    b12 = fonk1(a1, b11)
    b13 = fonk1(a1, b12)
    b14 = fonk1(a1, b13)
    b15 = 2 * b12 - b13
    b16 = (a1 / (1 - a1)) * (b12 - b13)
    b17 = b15 + b16
    b18 = 3 * b12 - 3 * b13 + b14
    b19 = (a1 / (2 * ((1 - a1) ** 2))) * (
                (6 - 5 * a1) * b12 - 2 * ((5 - 4 * a1) * b13) + (4 - 3 * a1) * b14)
    b20 = ((a1 ** 2) / (2 * ((1 - a1) ** 2))) * (b12 - 2 * b13 + b14)
    b21 = b18 + b19 + b20
    b22 = np.insert(year, len(year), values=b6, b23=0)
    b17 = np.insert(b17, len(b17), values=np.array(
        [b15[-1] + b16[-1] * i for i in range(1, 3)]), b23 = 0)
    b21 = np.insert(b21, len(b21), values=np.array(
        [b18[-1] + b19[-1] * i + b20[-1] * (i ** 2) for i in range(1, 3)]), b23 = 0)
    fonk2(b22, b6, b8, b17, b21)
if b24 = = '__main__':
    fonk3()