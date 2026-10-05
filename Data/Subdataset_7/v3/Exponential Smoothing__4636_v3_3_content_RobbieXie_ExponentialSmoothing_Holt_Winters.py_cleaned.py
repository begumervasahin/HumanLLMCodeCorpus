import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, series):
    b1 = np.zeros(series.shape)
    b1[0] = series[0]
    for i in range(1, len(series)):
        b1[i] = a1 * series[i] + (1 - a1) * b1[i - 1]
    return b1
def fonk2(year, actual_data, b16, b20):
    plt.figure(b2 = (14, 6), dpi=80)
    plt.plot(year, actual_data, b3 = 'blue', label="Actual Value")
    plt.plot(year[2:], b16[2:], b3 = 'red', label="Double Predicted Value")
    plt.plot(year[2:], b20[2:], b3 = 'green', label="Triple Predicted Value")
    plt.legend(b4 = 'lower right')
    plt.title('Projects')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.xticks(year)
    plt.show()
def fonk3():
    a1 = 0.70
    b5 = np.array([2016, 2017])
    b6 = 'data1.txt'
    b7 = np.loadtxt(b6)
    year, time_id, b8 = b7.T
    b9 = np.insert(b7, 0, values=[0, 0, b8[0]], b22=0)
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
    b21 = np.insert(year, len(year), values=b5, b22=0)
    b16 = np.insert(b16, len(b16), values=np.array(
        [b14[-1] + b15[-1] * i for i in range(1, 3)]), b22 = 0)
    b20 = np.insert(b20, len(b20), values=np.array(
        [b17[-1] + b18[-1] * i + b19[-1] * (i ** 2) for i in range(1, 3)]), b22 = 0)
    fonk2(b21, b10, b16, b20)
if b23 = = '__main__':
    fonk3()