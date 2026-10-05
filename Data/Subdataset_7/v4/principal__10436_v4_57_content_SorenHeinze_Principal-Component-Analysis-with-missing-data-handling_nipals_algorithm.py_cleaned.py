import numpy as np
from scipy import linalg as SLA
from math import sqrt
from copy import deepcopy
import plotting as pl
def fonk1(b11, rawdata, number_of_components):
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = [0]
    b6 = []
    b7 = []
    b8 = []
    b13, b9 = fonk2(rawdata)
    for a6 in range(number_of_components):
        first_Z, b10 = fonk3(b11)
        b17, b19, b24, b10 = fonk4(b11, first_Z, b10)
        b1.append(b19)
        b2.append(b17)
        b3.append(b24)
        b4.append(b10)
        print("Eigenvalue of %s. component: %s" % ((a6 + 1), b4[a6]))
        print("==================")
        b11 = b11 - np.dot(b17.T, b19)
        b5.append(fonk9(b11, b13))
        b6.append(fonk10(b11, b9))
        b7.append(fonk11(b11))
        b8.append(fonk12(b17, b8))
    b44, b43, b12 = fonk13(b2, b1, b3, number_of_components)
    return b44, b43, b12, b5, b6, b7, b8
def fonk2(rawdata):
    b13 = np.nansum(rawdata * rawdata)
    b9 = []
    for a6 in range(rawdata.shape[1]):
        b9.append(np.nansum(rawdata[:, a6] * rawdata[:, a6]))
    return b13, b9
def fonk3(b11):
    b14 = b11 * b11
    b15 = np.nansum(b14, axis=0)
    b16 = np.argmax(b15)
    b17 = b11[:, b16]
    b10 = np.nansum(b17**2)
    return b17, b10
def fonk4(b11, b17, b10):
    a1 = 1
    a2 = 0
    while a1 > 0.000000001:
        a2 += 1
        b18 = fonk7(b11, b17, b10)
        b19 = np.array(b18)
        b20 = fonk8(b11, b19)
        b21 = np.array(b20)
        b22 = np.nansum(b21**2)
        a1 = abs(b10 - b22)
        if a2 = = 300:
            print("\n300 iterations have passed, please check the b11 for extreme outliers. "
                  "And take these out if after 300 more iterations NIPALs still doesn't converge.")
            pl.plot_scores(1, [1, 1], 'b39', range(1, (len(b17) + 1)), [b17])
        b17 = b21
        b10 = b22
        if a2 > 600:
            break
    b23 = fonk5(b11, b17, b19)
    b24 = np.array(b23)
    b19 = np.array([b19])
    b17 = np.array([b17])
    b24 = np.array([b24])
    print("So many iterations undertaken:", a2)
    return b17, b19, b24, b10
def fonk5(b11, b17, b19):
    b23 = []
    for o in range(b19.shape[0]):
        a3 = 0
        a4 = 0
        a5 = 0
        b25 = []
        b26 = deepcopy(b17)
        b25 = np.argwhere(np.isnan(b11[:, o]))
        b26 = fonk6(b26, b25)
        b27 = np.nansum(b11[:, o]) / (len(b11[:, o]) - len(b25))
        b28 = np.nansum(b26) / len(b26)
        for a6 in range(len(b26)):
            if np.isnan(b11[:, o][a6]):
                continue
            b29 = b11[:, o][a6] - b27
            b30 = b26[a6] - b28
            a3 += b29 * b30
            a4 += b29**2
            a5 += b30**2
        b31 = sqrt(a4) * sqrt(a5)
        b24 = a3 / b31
        b23.append(b24)
    return b23
def fonk6(b26, b25):
    b32 = deepcopy(b26)
    a6 = 0
    for element in b25:
        b16 = element[0] - a6
        a6 += 1
        b32 = np.delete(b32, b16)
    return b32
def fonk7(b11, b17, b10):
    b18 = []
    for m in range(b11.shape[1]):
        a3 = 0
        a7 = 0
        for a6 in range(len(b17)):
            if np.isnan(b11[:, m][a6]) or np.isnan(b17[a6]):
                continue
            a3 += b17[a6] * b11[:, m][a6]
            a7 += b17[a6] * b17[a6]
        b33 = a3 / a7
        b18.append(b33)
    return b18
def fonk8(b11, b19):
    b20 = []
    for n in range(b11.shape[0]):
        a3 = 0
        a7 = 0
        for a6 in range(len(b19)):
            if np.isnan(b11[n, :][a6]):
                continue
            a3 += b19[a6] * b11[n, :][a6]
            a7 += b19[a6] * b19[a6]
        b34 = a3 / a7
        b20.append(b34)
    return b20
def fonk9(b11, b13):
    b35 = np.nansum(b11 * b11)
    return 1 - b35 / b13
def fonk10(b11, b9):
    b36 = []
    for a6 in range(b11.shape[1]):
        b37 = np.nansum(b11[:, a6] * b11[:, a6])
        b36.append(1 - b37 / b9[a6])
    return b36
def fonk11(b11):
    b38 = []
    for a6 in range(b11.shape[0]):
        b39 = sqrt(np.dot(b11[a6].reshape(b11[0].shape[0], 1).T, b11[a6].reshape(b11[0].shape[0], 1)))
        if np.isnan(b39):
            b39 = sqrt(np.nansum(b11[a6]**2))
        b38.append(b39)
    return b38
def fonk12(b17, b8):
    b40 = []
    if len(b8) == 0:
        b41 = np.std(b17)
        for a6 in range(b17.shape[1]):
            b40.append((b17[0][a6] / b41)**2)
    else:
        b42 = len(b8) - 1
        b41 = np.std(b17)
        for a6 in range(b17.shape[1]):
            b40.append(b8[b42][a6] + (b17[0][a6] / b41)**2)
    return b40
def fonk13(b2, b1, b3, number_of_components):
    b43 = np.concatenate((b1[0], b1[1]), axis=0)
    b44 = np.concatenate((b2[0], b2[1]), axis=0)
    b12 = np.concatenate((b3[0], b3[1]), axis=0)
    for a6 in range(2, number_of_components):
        b43 = np.concatenate((b43, b1[a6]), axis=0)
        b44 = np.concatenate((b44, b2[a6]), axis=0)
        b12 = np.concatenate((b12, b3[a6]), axis=0)
    return b44, b43, b12