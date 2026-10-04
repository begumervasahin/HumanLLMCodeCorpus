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
    b13 = np.zeros(b11.shape)
    for i in range(1, len(initial_time_id)):
        b13[i] = a1 * b10[i - 1] + (1 - a1) * b11[i - 1]
    b14 = 2 * b11 - b12
    b15 = (a1 / (1 - a1)) * (b11 - b12)
    b16 = np.zeros(b12.shape)
    for i in range(1, len(initial_time_id)):
        b16[i] = b14[i - 1] + b15[i - 1]
    b17 = b14[-1] + b15[-1] * 1
    b18 = b14[-1] + b15[-1] * 2
    b16 = np.append(b16, [b17, b18])
    b19 = fonk1(a1, b12)
    b20 = 3 * b11 - 3 * b12 + b19
    b21 = (a1 / (2 * (1 - a1)**2)) * ((6 - 5 * a1) * b11 -
              2 * ((5 - 4 * a1) * b12) + (4 - 3 * a1) * b19)
    b22 = ((a1**2) / (2 * (1 - a1)**2)) * (b11 - 2 * b12 + b19)
    b23 = np.zeros(b19.shape)
    for i in range(1, len(initial_time_id)):
        b23[i] = b20[i - 1] + b21[i - 1] + b22[i - 1] * (1**2)
    b24 = b20[-1] + b21[-1] * 1 + b22[-1] * (1**2)
    b25 = b20[-1] + b21[-1] * 2 + b22[-1] * (2**2)
    b23 = np.append(b23, [b24, b25])
    b26 = np.append(year, b5)
    b27 = np.array([b26, b16, b23])
    print(b27)
    fonk2(b26, b8, b16, b23)
if b28 = = '__main__':
    fonk3()