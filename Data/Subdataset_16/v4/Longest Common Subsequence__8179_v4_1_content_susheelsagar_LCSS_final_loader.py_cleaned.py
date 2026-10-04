import numpy as np
with open("distance_matrix_full.csv", "r") as f:
    b1 = []
    a1 = 8357
    b2 = np.zeros((a1, a1))
    for i, line in enumerate(f):
        b3 = line.strip().split(",")
        b1.append(b3[0])
        for j, value in enumerate(b3[1:], b4 = 0):
            b2[i][j] = float(value)
            b2[j][i] = float(value)
with open("distance_matrix_1698.csv", "r") as f1:
    for i, line in enumerate(f1, b4 = a1):
        b3 = line.strip().split(",")
        b1.append(b3[0])
        for j, value in enumerate(b3[1:], b4 = 0):
            b2[i][j] = float(value)
            b2[j][i] = float(value)
with open("distance_matrix_final.csv", "w") as f2, open("distance_matrix_final_withoutid.csv", "w") as f3:
    for i in range(a1):
        f2.write(f"{b1[i]},{','.join(map(str, b2[i]))}\n")
        f3.write(f"{','.join(map(str, b2[i]))}\n")