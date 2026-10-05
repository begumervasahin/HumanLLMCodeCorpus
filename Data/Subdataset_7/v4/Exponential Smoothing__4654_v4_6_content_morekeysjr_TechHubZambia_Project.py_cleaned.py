import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, b7):
    b1 = np.zeros(b7.shape)
    b1[0] = b7[0]
    for i in range(1, len(b7)):
        b1[i] = a1 * b7[i] + (1 - a1) * b1[i - 1]
    return b1
def fonk2(years, b8, b12, b13):
    plt.figure(b2 = (14, 6), dpi=80)
    plt.plot(years, b8, b3 = 'blue', label="Actual Value")
    plt.plot(years[1:], b12[2:], b3 = 'red', label="Double Predicted Value")
    plt.plot(years[1:], b13[2:], b3 = 'green', label="Triple Predicted Value")
    plt.legend(b4 = 'lower right')
    plt.title('Projects')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.xticks(years)
    plt.show()
def fonk3():
    a1 = 0.70
    b5 = np.array([2016, 2017])
    b6 = 'data1.txt'
    b7 = np.loadtxt(b6)
    years, time_ids, b8 = b7.T
    b9 = np.array([0, 0, b8[0]])
    b10 = np.insert(b7, 0, values=b9, axis=0)
    initial_years, initial_time_ids, b10 = b10.T
    b11 = fonk1(a1, b10)
    b12 = fonk1(a1, b11)
    b13 = fonk1(a1, b12)
    b14 = 2 * b11 - b12
    b15 = (a1 / (1 - a1)) * (b11 - b12)
    b16 = np.zeros(b12.shape)
    for i in range(1, len(initial_time_ids)):
        b16[i] = b14[i - 1] + b15[i - 1]
    b16[-2:] = b14[-1] + b15[-1] * np.array([1, 2])
    b17 = 3 * b11 - 3 * b12 + b13
    b18 = (a1 / (2 * ((1 - a1) ** 2))) * ((6 - 5 * a1) * b11 - 2 * ((5 - 4 * a1) * b12) + (4 - 3 * a1) * b13)
    b19 = ((a1 ** 2) / (2 * ((1 - a1) ** 2))) * (b11 - 2 * b12 + b13)
    b20 = np.zeros(b13.shape)
    for i in range(1, len(initial_time_ids)):
        b20[i] = b17[i - 1] + b18[i - 1] * 1 + b19[i - 1] * (1 ** 2)
    b20[-2:] = b17[-1] + b18[-1] * np.array([1, 2]) + b19[-1] * np.array([1 ** 2, 2 ** 2])
    b21 = np.insert(years, len(years), values=b5, axis=0)
    b22 = np.array([b21, b16, b20])
    print(b22)
    fonk2(b21, b8, b16, b20)
if b23 = = '__main__':
    fonk3()