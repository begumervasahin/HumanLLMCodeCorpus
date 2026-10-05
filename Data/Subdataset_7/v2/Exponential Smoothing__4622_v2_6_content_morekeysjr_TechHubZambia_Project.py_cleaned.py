import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, s):
    b1 = np.zeros(s.shape)
    b1[0] = s[0]
    for i in range(1, len(s)):
        b1[i] = a1 * s[i] + (1 - a1) * b1[i - 1]
    return b1
def fonk2(b26, b6, b8, double_predicted_values, triple_predicted_values):
    years, time_ids, b2 = b8.T
    plt.figure(b3 = (14, 6), dpi=80)
    plt.plot(years, b2, b4 = 'blue', label="Actual Value")
    plt.plot(b26[1:], double_predicted_values[2:], b4 = 'red', label="Double Predicted Value")
    plt.plot(b26[1:], triple_predicted_values[2:], b4 = 'green', label="Triple Predicted Value")
    plt.legend(b5 = 'lower right')
    plt.title('Projects')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.xticks(b26)
    plt.show()
def fonk3():
    a1 = 0.70
    b6 = np.array([2016, 2017])
    b7 = 'data1.txt'
    b8 = np.loadtxt(b7)
    years, time_ids, b2 = b8.T
    b9 = np.array([0, 0, b2[0]])
    b10 = np.insert(b8, 0, values=b9, axis=0)
    initial_years, initial_time_ids, b11 = b10.T
    b12 = fonk1(a1, b11)
    b13 = fonk1(a1, b12)
    b14 = fonk1(a1, b13)
    b15 = 2 * b12 - b13
    b16 = (a1 / (1 - a1)) * (b12 - b13)
    b17 = np.zeros(b13.shape)
    for i in range(1, len(initial_time_ids)):
        b17[i] = b15[i - 1] + b16[i - 1]
    b18 = b15[-1] + b16[-1] * 1
    b19 = b15[-1] + b16[-1] * 2
    b17 = np.insert(b17, len(b17), values=np.array([b18, b19]), axis=0)
    b20 = 3 * b12 - 3 * b13 + b14
    b21 = (a1 / (2 * ((1 - a1) ** 2))) * ((6 - 5 * a1) * b12 - 2 * ((5 - 4 * a1) * b13) + (4 - 3 * a1) * b14)
    b22 = ((a1 ** 2) / (2 * ((1 - a1) ** 2))) * (b12 - 2 * b13 + b14)
    b23 = np.zeros(b14.shape)
    for i in range(1, len(initial_time_ids)):
        b23[i] = b20[i - 1] + b21[i - 1] * 1 + b22[i - 1] * (1 ** 2)
    b24 = b20[-1] + b21[-1] * 1 + b22[-1] * (1 ** 2)
    b25 = b20[-1] + b21[-1] * 2 + b22[-1] * (2 ** 2)
    b23 = np.insert(b23, len(b23), values=np.array([b24, b25]), axis=0)
    b26 = np.insert(years, len(years), values=b6, axis=0)
    b27 = np.array([b26, b17, b23])
    print(b27)
    fonk2(b26, b6, b8, b17, b23)
if b28 = = '__main__':
    fonk3()