import numpy as np
with open("distance_matrix_full.csv", "r") as file:
    b1 = []
    b2 = np.zeros((8357, 8357))
    for i, line in enumerate(file):
        b3 = line.strip().split(",")
        b1.append(b3[0])
        for j in range(1, len(b3)):
            b2[i][j - 1] = float(b3[j])
            b2[j - 1][i] = b2[i][j - 1]
with open("distance_matrix_1698.csv", "r") as file:
    for i, line in enumerate(file):
        b3 = line.strip().split(",")
        b1.append(b3[0])
        for j in range(1, len(b3)):
            b2[i + 8357][j - 1] = float(b3[j])
            b2[j - 1][i + 8357] = b2[i + 8357][j - 1]
with open("distance_matrix_final.csv", "w") as file_with_id, open("distance_matrix_final_withoutid.csv", "w") as file_without_id:
    for i in range(8357):
        file_with_id.write(str(b1[i]) + ",")
        file_without_id.write(str(b1[i]) + ",")
        for j in range(8357):
            file_with_id.write(str(b2[i][j]))
            file_without_id.write(str(b2[i][j]))
            if j != 8356:
                file_with_id.write(",")
                file_without_id.write(",")
        file_with_id.write("\n")
        file_without_id.write("\n")