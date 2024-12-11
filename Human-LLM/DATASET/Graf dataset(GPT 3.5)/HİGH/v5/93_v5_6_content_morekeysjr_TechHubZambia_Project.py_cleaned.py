import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, data):
    b1 = np.zeros(data.shape)
    b1[0] = data[0]
    for i in range(1, len(data)):
        b1[i] = a1 * data[i] + (1 - a1) * b1[i - 1]
    return b1
def fonk2(years, b7, b15, b19):
    plt.figure(b2 = (14, 6), dpi=80)
    plt.plot(years, b7, b3 = 'blue', label="Actual Value")
    plt.plot(years[1:], b15[2:], b3 = 'red', label="Double Predicted Value")
    plt.plot(years[1:], b19[2:], b3 = 'green', label="Triple Predicted Value")
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
    years, time_ids, b7 = np.loadtxt(b6, unpack=True)
    b8 = np.insert(np.vstack((years, time_ids, b7)).T, 0, [0, 0, b7[0]], axis=0)
    initial_years, initial_time_ids, b9 = b8.T
    b10 = fonk1(a1, b9)
    b11 = fonk1(a1, b10)
    b12 = fonk1(a1, b11)
    b13 = 2 * b10 - b11
    b14 = (a1 / (1 - a1)) * (b10 - b11)
    b15 = np.zeros(b11.shape)
    b15[1:] = b13[:-1] + b14[:-1]
    b15[-2:] = b13[-1] + b14[-1] * np.array([1, 2])
    b16 = 3 * b10 - 3 * b11 + b12
    b17 = (a1 / (2 * ((1 - a1) ** 2))) * ((6 - 5 * a1) * b10 - 2 * ((5 - 4 * a1) * b11) + (4 - 3 * a1) * b12)
    b18 = ((a1 ** 2) / (2 * ((1 - a1) ** 2))) * (b10 - 2 * b11 + b12)
    b19 = np.zeros(b12.shape)
    b19[1:] = b16[:-1] + b17[:-1] * 1 + b18[:-1] * (1 ** 2)
    b19[-2:] = b16[-1] + b17[-1] * np.array([1, 2]) + b18[-1] * np.array([1 ** 2, 2 ** 2])
    b20 = np.insert(years, len(years), values=b5, axis=0)
    b21 = np.array([b20, b15, b19])
    print(b21)
    fonk2(b20, b7, b15, b19)
if b22 = = '__main__':
    fonk3()