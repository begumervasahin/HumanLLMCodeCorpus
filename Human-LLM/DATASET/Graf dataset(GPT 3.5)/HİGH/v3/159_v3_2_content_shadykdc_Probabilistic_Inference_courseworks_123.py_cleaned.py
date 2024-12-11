from IDAPICourseworkLibrary import ImportData, Discretise
import numpy as np
def fonk1(b11, root_index, b12):
    b1 = np.zeros((b12[root_index]), dtype=float)
    b2 = len(b11[:, 0])
    for i in range(b2):
        b1[b11[i, root_index]] += 1
    b1 /= b2
    return b1
def fonk2(b11, parent_index, child_index, b12):
    b2 = len(b11[:, 0])
    b3 = np.zeros((b12[parent_index], b12[child_index]), dtype=float)
    for row in range(b2):
        b3[b11[row, parent_index]][b11[row, child_index]] += 1
    for i in range(b12[child_index]):
        b4 = (np.sum(b11[:, child_index] == i))
        if b4 != 0:
            b3[:, i] /= (np.sum(b11[:, child_index] == i))
    return b3
def fonk3(b11, row_index, col_index, b12):
    b5 = np.zeros((b12[row_index], b12[col_index]), dtype=float)
    b2 = len(b11[:, 0])
    for row in range(b2):
        b5[b11[row, row_index]][b11[row, col_index]] += 1
    b5 /= b2
    return b5
def fonk4(b5):
    for i in range(len(b5[0, :])):
        b4 = (np.sum(b5[:, i]))
        if b4 != 0:
            b5[:, i] *= 1 / b4
    return b5
def fonk5(the_query, naive_bayes):
    b6 = np.zeros((naive_bayes[0].shape[0]), dtype=float)
    for i in range(len(b6)):
        b6[i] = naive_bayes[0][i]
        for j in range(len(the_query)):
            b6[i] *= naive_bayes[j + 1][the_query[j], i]
    if np.sum(b6) != 0:
        b6 *= 1 / np.sum(b6)
    else:
        b6 = np.ones((naive_bayes[0].shape[0]), dtype=float) / naive_bayes[0].shape[0]
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
            if b5[i][j] != 0:
                a1 += b5[i][j] * np.log2(b5[i][j] / (b10 * b9[j]))
    return a1
b11 = ImportData("IDAPICourseworkData.csv", ",")
b11 = Discretise(b11, [5, 5, 5, 5, 5, 5, 5], ["s", "s", "s", "s", "s", "s", "c"])
b12 = [5, 5, 5, 5, 5, 5, 5]
b13 = fonk1(b11, 0, b12)
b14 = fonk1(b11, 1, b12)
b15 = fonk1(b11, 2, b12)
b16 = fonk1(b11, 3, b12)
b17 = fonk1(b11, 4, b12)
b18 = fonk1(b11, 5, b12)
b19 = fonk1(b11, 6, b12)
b20 = fonk2(b11, 0, 1, b12)
b21 = fonk2(b11, 1, 2, b12)
b22 = fonk2(b11, 2, 3, b12)
b23 = fonk2(b11, 3, 4, b12)
b24 = fonk2(b11, 4, 5, b12)
b25 = fonk2(b11, 5, 6, b12)
b26 = fonk3(b11, 0, 1, b12)
b27 = fonk3(b11, 1, 2, b12)
b28 = fonk3(b11, 2, 3, b12)
b29 = fonk3(b11, 3, 4, b12)
b30 = fonk3(b11, 4, 5, b12)
b31 = fonk3(b11, 5, 6, b12)
b32 = fonk4(b26)
b33 = fonk4(b27)
b34 = fonk4(b28)
b35 = fonk4(b29)
b36 = fonk4(b30)
b37 = fonk4(b31)
b38 = [b13, b32, b33, b34, b35, b36, b37]
b39 = [1, 3, 2, 4, 2, 1]
b40 = fonk5(b39, b38)
print("Result of b39:", b40)
b41 = fonk6(b26)
b42 = fonk6(b27)
b43 = fonk6(b28)
b44 = fonk6(b29)
b45 = fonk6(b30)
b46 = fonk6(b31)
print("Mutual Information between A and B:", b41)
print("Mutual Information between B and C:", b42)
print("Mutual Information between C and D:", b43)
print("Mutual Information between D and E:", b44)
print("Mutual Information between E and F:", b45)
print("Mutual Information between F and G:", b46)