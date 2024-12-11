import numpy as np
from scipy import linalg as SLA
from math import sqrt
from copy import deepcopy
import plotting as pl
def fonk1(b5, rawdata, number_of_components):
    P_s, Z_s, b1 = [], [], []
    Z_Eigenvalues, R_2, R_k_2, SPE, b2 = [], [0], [], [], []
    b7, b3 = fonk2(rawdata)
    for b29 in range(number_of_components):
        first_Z, b4 = fonk3(b5)
        b11, b14, b28, b4 = fonk4(b5, first_Z, b4)
        P_s.append(b14)
        Z_s.append(b11)
        b1.append(b28)
        Z_Eigenvalues.append(b4)
        print(f"Eigenvalue of {b29 + 1}. component: {Z_Eigenvalues[b29]}")
        print("==================")
        b5 = b5 - np.dot(b11.T, b14)
        R_2.append(fonk9(b5, b7))
        R_k_2.append(fonk10(b5, b3))
        SPE.append(fonk11(b5))
        b2.append(fonk12(b11, b2))
    b41, b40, b6 = fonk13(Z_s, P_s, b1, number_of_components)
    return b41, b40, b6, R_2, R_k_2, SPE, b2
def fonk2(rawdata):
    b7 = np.nansum(rawdata * rawdata)
    b3 = [np.nansum(rawdata[:, b29] * rawdata[:, b29]) for b29 in range(rawdata.shape[1])]
    return b7, b3
def fonk3(b5):
    b8 = b5 * b5
    b9 = np.nansum(b8, axis=0)
    b10 = np.argmax(b9)
    b11 = b5[:, b10]
    b4 = np.nansum(b11**2)
    return b11, b4
def fonk4(b5, b11, b4):
    b18, b12 = 1, 0
    while b18 > 0.000000001:
        b12 += 1
        b13 = fonk7(b5, b11, b4)
        b14 = np.array(b13)
        b15 = fonk8(b5, b14)
        b16 = np.array(b15)
        b17 = np.nansum(b16**2)
        b18 = abs(b4 - b17)
        if b12 = = 300:
            print("\n300 iterations have passed, please check the b5 for extreme outliers. "
                  "And take these out if after 300 more iterations NIPALs still doesn't converge.")
            pl.plot_scores(1, [1, 1], 'foo', range(1, (len(b11) + 1)), [b11])
        b11 = b16
        b4 = b17
        if b12 > 600:
            break
    b19 = fonk5(b5, b11, b14)
    b28, b14, b11 = np.array(b19), np.array([b14]), np.array([b11])
    print("So many iterations undertaken:", b12)
    return b11, b14, b28, b4
def fonk5(b5, b11, b14):
    b19 = []
    for o in range(b14.shape[0]):
        upper_sum, first_lower_sum, b20 = 0, 0, 0
        b21 = deepcopy(b11)
        b22 = np.argwhere(np.isnan(b5[:, o]))
        b21 = fonk6(b21, b22)
        b23 = np.nansum(b5[:, o]) / (len(b5[:, o]) - len(b22))
        b24 = np.nansum(b21) / len(b21)
        for b29 in range(len(b21)):
            if np.isnan(b5[:, o][b29]):
                continue
            b25 = b5[:, o][b29] - b23
            b26 = b21[b29] - b24
            upper_sum += b25 * b26
            first_lower_sum += b25**2
            b20 += b26**2
        b27 = sqrt(first_lower_sum) * sqrt(b20)
        b28 = upper_sum / b27
        b19.append(b28)
    return b19
def fonk6(b21, b22):
    b30, b29 = deepcopy(b21), 0
    for element in b22:
        b10 = element[0] - b29
        b29 += 1
        b30 = np.delete(b30, b10)
    return b30
def fonk7(b5, b11, b4):
    b13 = []
    for m in range(b5.shape[1]):
        upper_sum, b31 = 0, 0
        for b29 in range(len(b11)):
            if np.isnan(b5[:, m][b29]) or np.isnan(b11[b29]):
                continue
            upper_sum += b11[b29] * b5[:, m][b29]
            b31 += b11[b29] * b11[b29]
        b32 = upper_sum / b31
        b13.append(b32)
    return b13
def fonk8(b5, b14):
    b15 = []
    for n in range(b5.shape[0]):
        upper_sum, b31 = 0, 0
        for b29 in range(len(b14)):
            if np.isnan(b5[n, :][b29]):
                continue
            upper_sum += b14[b29] * b5[n, :][b29]
            b31 += b14[b29] * b14[b29]
        b33 = upper_sum / b31
        b15.append(b33)
    return b15
def fonk9(b5, b7):
    b34 = np.nansum(b5 * b5)
    return 1 - b34 / b7
def fonk10(b5, b3):
    b35 = [1 - np.nansum(b5[:, b29] * b5[:, b29]) / b3[b29] for b29 in range(b5.shape[1])]
    return b35
def fonk11(b5):
    b36 = [sqrt(np.dot(b5[b29].reshape(b5[0].shape[0], 1).T, b5[b29].reshape(b5[0].shape[0], 1)))
               if np.isnan(sqrt(np.dot(b5[b29].reshape(b5[0].shape[0], 1).T, b5[b29].reshape(b5[0].shape[0], 1))))
               else sqrt(np.nansum(b5[b29]**2)) for b29 in range(b5.shape[0])]
    return b36
def fonk12(b11, b2):
    b37 = []
    if not b2:
        b38 = np.std(b11)
        b37 = [(b11[0][b29] / b38)**2 for b29 in range(b11.shape[1])]
    else:
        b39 = len(b2) - 1
        b38 = np.std(b11)
        b37 = [b2[b39][b29] + (b11[0][b29] / b38)**2 for b29 in range(b11.shape[1])]
    return b37
def fonk13(Z_s, P_s, b1, number_of_components):
    b40 = np.concatenate((P_s[0], P_s[1]), axis=0)
    b41 = np.concatenate((Z_s[0], Z_s[1]), axis=0)
    b6 = np.concatenate((b1[0], b1[1]), axis=0)
    for b29 in range(2, number_of_components):
        b40 = np.concatenate((b40, P_s[b29]), axis=0)
        b41 = np.concatenate((b41, Z_s[b29]), axis=0)
        b6 = np.concatenate((b6, b1[b29]), axis=0)
    return b41, b40, b6