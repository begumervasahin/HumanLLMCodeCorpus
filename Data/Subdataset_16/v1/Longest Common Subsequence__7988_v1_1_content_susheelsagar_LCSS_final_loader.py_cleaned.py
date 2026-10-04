import numpy as np
a1 = 8357
a2 = 1698
b1 = a1 + a2
b2 = np.zeros((b1, b1))
b3 = []
with open("distance_matrix_full.csv", "r") as f:
    for i, line in enumerate(f):
        b4 = line.strip().split(",")
        b3.append(b4[0])
        for j, value in enumerate(b4[1:], b5 = 0):
            b2[i][j] = float(value)
            b2[j][i] = b2[i][j]
with open("distance_matrix_1698.csv", "r") as f1:
    for line in f1:
        b4 = line.strip().split(",")
        b3.append(b4[0])
        for j, value in enumerate(b4[1:], b5 = len(b3) - 1 - a2):
            b2[len(b3) - 1][j] = float(value)
            b2[j][len(b3) - 1] = b2[len(b3) - 1][j]
with open("distance_matrix_final.csv", "w") as f2:
    for i in range(b1):
        f2.write(b3[i])
        f2.write("," + ",".join(map(str, b2[i])) + "\n")
with open("distance_matrix_final_withoutid.csv", "w") as f3:
    for i in range(b1):
        f3.write(",".join(map(str, b2[i])) + "\n")