import numpy as np
def fonk1(data, root, num_states):
    b1 = np.zeros((num_states[root]), dtype=float)
    b2 = len(data[:, 0])
    for i in range(b2):
        b1[data[i, root]] += 1
    b1 /= b2
    return b1
def fonk2(data, var_c, var_p, num_states):
    b2 = len(data[:, 0])
    b3 = np.zeros((num_states[var_c], num_states[var_p]), dtype=float)
    for row in range(b2):
        b3[data[row, var_c]][data[row, var_p]] += 1
    for i in range(num_states[var_p]):
        b4 = np.sum(data[:, var_p] == i)
        if b4 != 0:
            b3[:, i] /= np.sum(data[:, var_p] == i)
    return b3
def fonk3(data, var_row, var_col, num_states):
    b5 = np.zeros((num_states[var_row], num_states[var_col]), dtype=float)
    b2 = len(data[:, 0])
    for row in range(b2):
        b5[data[row, var_row]][data[row, var_col]] += 1
    b5 /= b2
    return b5
def fonk4(b5):
    for i in range(len(b5[0, :])):
        b4 = np.sum(b5[:, i])
        if b4 != 0:
            b5[:, i] *= 1 / b4
    return b5
def fonk5(b12, b14):
    b6 = np.zeros((b14[0].shape[0]), dtype=float)
    for i in range(len(b6)):
        b6[i] = b14[0][i]
        for j in range(0, len(b12)):
            b6[i] *= b14[j + 1][b12[j], i]
    if np.sum(b6) != 0:
        b6 *= 1 / np.sum(b6)
    else:
        b6 = np.ones((b14[0].shape[0]), dtype=float) / b14[0].shape[0]
    return b6
def fonk6(b5):
    a1 = 0.0
    b7 = len(b5[0, :])
    b8 = len(b5[:, 0])
    b9 = np.zeros(b7, dtype=float)
    for j in range(b7):
        b9[j] = np.sum(b5[:, j])
    for i in range(b8):
        b10 = np.sum(b5[i, :])
        for j in range(b7):
            if b5[i][j] != 0 and b9[j] != 0 and b10 != 0:
                a1 += b5[i][j] * np.log(b5[i][j] / (b10 * b9[j]), 2)
    return a1
b11 = np.array([[1, 1, 1, 1], [1, 2, 1, 1], [2, 1, 2, 2], [2, 2, 2, 2], [2, 2, 1, 1]])
b12 = np.array([0, 1, 1])
b1 = fonk1(b11, 0, [3, 2, 2, 2])
print("Prior:", b1)
b3 = fonk2(b11, 1, 0, [3, 2, 2, 2])
print("CPT:", b3)
b5 = fonk3(b11, 0, 1, [3, 2, 2, 2])
print("JPT:", b5)
b13 = fonk4(b5)
print("CPT from JPT:", b13)
b14 = [b1, b13]
for i in range(len(b12)):
    print("Query result:", fonk5(b12, b14))
b15 = fonk6(b5)
print("Mutual Information:", b15)