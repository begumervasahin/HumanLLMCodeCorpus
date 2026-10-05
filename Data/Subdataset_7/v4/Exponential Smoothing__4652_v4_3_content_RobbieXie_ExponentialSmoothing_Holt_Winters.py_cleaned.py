import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, s):
    b1 = np.zeros(s.shape)
    b1[0] = s[0]
    for i in range(1, len(s)):
        b1[i] = a1 * s[i] + (1 - a1) * b1[i - 1]
    return b1
def fonk2(b21, b6, b8, b16, b20):
    year, time_id, b2 = b8.T
    plt.figure(b3 = (14, 6), dpi=80)
    plt.plot(year, b2, b4 = 'blue', label="Actual Value")
    plt.plot(b21[1:], b16[2:], b4 = 'red', label="Double Predicted Value")
    plt.plot(b21[1:], b20[2:], b4 = 'green', label="Triple Predicted Value")
    plt.legend(b5 = 'lower right')
    plt.title('Projects')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.xticks(b21)
    plt.show()
def fonk3():
    a1 = 0.70
    b6 = np.array([2016, 2017])
    b7 = 'data1.txt'
    b8 = np.loadtxt(b7)
    year, time_id, b2 = b8.T
    b9 = np.insert(b8, 0, values=[0, 0, b2[0]], b22=0)
    initial_year, initial_time_id, b10 = b9.T
    b11 = fonk1(a1, b10)
    b12 = fonk1(a1, b11)
    b13 = fonk1(a1, b12)
    b14 = 2 * b11 - b12
    b15 = (a1 / (1 - a1)) * (b11 - b12)
    b16 = b14 + b15
    b17 = 3 * b11 - 3 * b12 + b13
    b18 = (a1 / (2 * ((1 - a1) ** 2))) * (
                (6 - 5 * a1) * b11 - 2 * ((5 - 4 * a1) * b12) + (4 - 3 * a1) * b13)
    b19 = ((a1 ** 2) / (2 * ((1 - a1) ** 2))) * (b11 - 2 * b12 + b13)
    b20 = b17 + b18 + b19
    b21 = np.insert(year, len(year), values=b6, b22=0)
    b16 = np.insert(b16, len(b16), values=np.array(
        [b14[-1] + b15[-1] * i for i in range(1, 3)]), b22 = 0)
    b20 = np.insert(b20, len(b20), values=np.array(
        [b17[-1] + b18[-1] * i + b19[-1] * (i ** 2) for i in range(1, 3)]), b22 = 0)
    fonk2(b21, b6, b8, b16, b20)
if b23 = = '__main__':
    fonk3()