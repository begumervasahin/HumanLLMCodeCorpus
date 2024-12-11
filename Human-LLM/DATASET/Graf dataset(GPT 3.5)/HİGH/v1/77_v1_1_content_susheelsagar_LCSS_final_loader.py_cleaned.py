import numpy as np
with open("distance_matrix_full.csv", "r") as f:
    b1 = []
    b2 = np.zeros((8357, 8357))
    for i, line in enumerate(f):
        b3 = line.strip().split(",")
        b1.append(b3[0])
        for j in range(1, len(b3)):
            b2[i][j-1] = float(b3[j])
            b2[j-1][i] = b2[i][j-1]
with open("distance_matrix_1698.csv", "r") as f:
    for i, line in enumerate(f):
        b3 = line.strip().split(",")
        b1.append(b3[0])
        for j in range(1, len(b3)):
            b2[i+8357][j-1] = float(b3[j])
            b2[j-1][i+8357] = b2[i+8357][j-1]
with open("distance_matrix_final.csv", "w") as f2, open("distance_matrix_final_withoutid.csv", "w") as f3:
    for i in range(8357):
        f2.write(str(b1[i]) + ",")
        f3.write(str(b1[i]) + ",")
        for j in range(8357):
            f2.write(str(b2[i][j]))
            f3.write(str(b2[i][j]))
            if j != 8356:
                f2.write(",")
                f3.write(",")
        f2.write("\n")
        f3.write("\n")