import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1, s):
    b1 = np.zeros(s.shape)
    b1[0] = s[0]
    for i in range(1, len(s)):
        b1[i] = a1 * s[i] + (1 - a1) * b1[i - 1]
    return b1
def fonk2(b15, b16, a1):
    b2 = 2 * b15 - b16
    b3 = (a1 / (1 - a1)) * (b15 - b16)
    return b2 + b3
def fonk3(b15, b16, s_triple, a1):
    b4 = 3 * b15 - 3 * b16 + s_triple
    b5 = (a1 / (2 * ((1 - a1) ** 2))) * (
                (6 - 5 * a1) * b15 - 2 * ((5 - 4 * a1) * b16) + (4 - 3 * a1) * s_triple)
    b6 = ((a1 ** 2) / (2 * ((1 - a1) ** 2))) * (b15 - 2 * b16 + s_triple)
    return b4 + b5 + b6
def fonk4(year, b12):
    return np.insert(year, len(year), b7 = b12, axis=0)
def fonk5(s_pre, last_values, a1, prediction_years):
    b8 = np.array([last_values[-1] + a1 * i for i in range(1, prediction_years + 1)])
    return np.insert(s_pre, len(s_pre), b7 = b8, axis=0)
def fonk6(b13):
    b9 = np.loadtxt(b13)
    year, time_id, b10 = b9.T
    b11 = np.insert(b9, 0, b7=[0, 0, b10[0]], axis=0)
    return b11.T
def fonk7():
    a1 = 0.70
    b12 = np.array([2016, 2017])
    b13 = 'data1.txt'
    initial_year, initial_time_id, b14 = fonk6(b13)
    b15 = fonk1(a1, b14)
    b16 =