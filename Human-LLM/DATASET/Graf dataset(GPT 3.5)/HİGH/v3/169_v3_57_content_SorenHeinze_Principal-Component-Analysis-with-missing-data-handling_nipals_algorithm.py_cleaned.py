import numpy as np
from math import sqrt
from copy import deepcopy
def fonk1(b5, rawdata, number_of_components):
    P_s, Z_s, r_s, b1 = [], [], [], []
    R_2, R_k_2, SPE, b2 = [0], [], [], []
    b7, b3 = fonk2(rawdata)
    for i in range(number_of_components):
        first_Z, b4 = fonk3(b5)
        b11, b12, b14, b4 = fonk4(b5, first_Z, b4)
        P_s.append(b12)
        Z_s.append(b11)
        r_s.append(b14)
        b1.append(b4)
        print("Eigenvalue of {}th component: {}".format(i + 1, b1[i]))
        print("==================")
        b5 = b5 - np.dot(b11.T, b12)
        R_2.append(fonk8(b5, b7))
        R_k_2.append(fonk9(b5, b3))
        SPE.append(fonk10(b5))
        b2.append(fonk11(b11, b2))
    b37, b36, b6 = fonk12(Z_s, P_s, r_s, number_of_components)
    return b37, b36, b6, R_2, R_k_2, SPE, b2
def fonk2(rawdata):
    b7 = np.nansum(rawdata * rawdata)
    b3 = [np.nansum(rawdata[:, i] * rawdata[:, i]) for i in range(rawdata.shape[1])]
    return b7, b3
def fonk3(b5):
    b8 = b5 * b5
    b9 = np.nansum(b8, axis=0)
    b10 = np.argmax(b9)
    b11 = b5[:, b10]
    b4 = np.nansum(b11 ** 2)
    return b11, b4
def fonk4(b5, b11, b4):
    a1 = 1
    a2 = 0
    while a1 > 1e-9:
        a2 += 1
        b12 = fonk5(b5, b11, b4)
        b11 = fonk6(b5, b12)
        b13 = np.nansum(b11 ** 2)
        a1 = abs(b4 - b13)
        if a2 = = 300:
            print("\n300 iterations have passed. Please check for extreme outliers in the b5.")
        b4 = b13
        if a2 > 600:
            break
    b14 = fonk7(b5, b11, b12)
    b12 = np.array([b12])
    b11 = np.array([b11])
    b14 = np.array([b14])
    print("Iterations completed:", a2)
    return b11, b12, b14, b4
def fonk5(b5, b11, b4):
    b15 = []
    for m in range(b5.shape[1]):
        b16 = np.sum(b11 * b5[:, m]) / b4
        b15.append(b16)
    return b15
def fonk6(b5, b12):
    b17 = []
    for n in range(b5.shape[0]):
        b18 = np.sum(b12 * b5[n, :]) / np.sum(b12 * b12)
        b17.append(b18)
    return b17
def fonk7(b5, b11, b12):
    b19 = []
    for o in range(b12.shape[0]):
        b20 = deepcopy(b11)
        b21 = np.argwhere(np.isnan(b5[:, o]))
        b20 = np.delete(b20, b21)
        b22 = np.nanmean(b5[:, o])
        b23 = np.nanmean(b20)
        b24 = np.sum((b5[:, o] - b22) * (b20 - b23))
        b25 = np.sum((b5[:, o] - b22) ** 2)
        b26 = np.sum((b20 - b23) ** 2)
        b27 = sqrt(b25) * sqrt(b26)
        b14 = b24 / b27
        b19.append(b14)
    return b19
def fonk8(b5, b7):
    b28 = np.nansum(b5 * b5)
    return 1 - b28 / b7
def fonk9(b5, b3):
    b29 = []
    for i in range(b5.shape[1]):
        b30 = np.nansum(b5[:, i] * b5[:, i])
        b29.append(1 - b30 / b3[i])
    return b29
def fonk10(b5):
    b31 = []
    for i in range(b5.shape[0]):
        b32 = sqrt(np.dot(b5[i].reshape(b5[0].shape[0], 1).T, b5[i].reshape(b5[0].shape[0], 1)))
        if np.isnan(b32):
            b32 = sqrt(np.nansum(b5[i] ** 2))
        b31.append(b32)
    return b31
def fonk11(b11, b2):
    b33 = []
    if len(b2) == 0:
        b34 = np.std(b11)
        for i in range(b11.shape[1]):
            b33.append((b11[0][i] / b34) ** 2)
    else:
        b35 = len(b2) - 1
        b34 = np.std(b11)
        for i in range(b11.shape[1]):
            b33.append(b2[b35][i] + (b11[0][i] / b34) ** 2)
    return b33
def fonk12(Z_s, P_s, r_s, number_of_components):
    b36 = np.concatenate(P_s, axis=0)
    b37 = np.concatenate(Z_s, axis=0)
    b6 = np.concatenate(r_s, axis=0)
    return b37, b36, b6
