import numpy as np
from matplotlib import pyplot as plt
def fonk1(a1, s):
    b1 = np.zeros(s.shape)
    b1[0] = s[0]
    for i in range(1, len(b1)):
        b1[i] = a1 * s[i] + (1 - a1) * b1[i - 1]
    return b1
def fonk2(years, original_data, double_smoothing, triple_smoothing):
    plt.figure(b2 = (14, 6), dpi=80)
    plt.plot(years, original_data, b3 = 'blue', label="Actual Value")
    plt.plot(years[1:], double_smoothing[2:], b3 = 'red', label="Double Predicted Value")
    plt.plot(years[1:], triple_smoothing[2:], b3 = 'green', label="Triple Predicted Value")
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
    year, time_id, b8 = b7.T
    b9 = np.insert(b7, 0, values=[0, 0, b8[0]], axis=0)
    initial_year, initial_time_id, b10 = b9.T
    b11 = fonk1(a1, b10)
    b12 = fonk1(a1, b11)
    b13 = 2 * b11 - b12
    b14 = (a1 / (1 - a1)) * (b11 - b12)
    b15 = np.zeros(b12.shape)
    for i in range(1, len(initial_time_id)):
        b15[i] = b13[i - 1] + b14[i - 1]
    b15 = np.append(b15, [
        b13[-1] + b14[-1] * 1,
        b13[-1] + b14[-1] * 2
    ])
    b16 = fonk1(a1, b12)
    b17 = 3 * b11 - 3 * b12 + b16
    b18 = (a1 / (2 * (1 - a1)**2)) * ((6 - 5 * a1) * b11 -
              2 * ((5 - 4 * a1) * b12) + (4 - 3 * a1) * b16)
    b19 = ((a1**2) / (2 * (1 - a1)**2)) * (b11 - 2 * b12 + b16)
    b20 = np.zeros(b16.shape)
    for i in range(1, len(initial_time_id)):
        b20[i] = b17[i - 1] + b18[i - 1] + b19[i - 1]
    b20 = np.append(b20, [
        b17[-1] + b18[-1] * 1 + b19[-1] * 1,
        b17[-1] + b18[-1] * 2 + b19[-1] * 4
    ])
    b21 = np.append(year, b5)
    b22 = np.array([b21, b15, b20])
    print(b22)
    fonk2(b21, b8, b15, b20)
if b23 = = '__main__':
    fonk3()