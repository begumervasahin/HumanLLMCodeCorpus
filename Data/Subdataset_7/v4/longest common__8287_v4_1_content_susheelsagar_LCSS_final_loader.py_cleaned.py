import numpy as np
with open("distance_matrix_full.csv", "r+") as file:
    b1 = []
    b2 = np.zeros((8357, 8357))
    a1 = 0
    for line in iter(file):
        b3 = line.split(",")
        b1.append(b3[0])
        a2 = 0
        a3 = 1
        while a3 < len(b3):
            b2[a1][a2] = float(b3[a3])
            b2[a2][a1] = b2[a1][a2]
            a2 += 1
            a3 += 1
        a1 += 1
with open("distance_matrix_1698.csv", "r+") as file:
    for line in iter(file):
        b3 = line.split(",")
        b1.append(b3[0])
        a2 = a1
        a3 = 1
        while a3 < len(b3):
            b2[a1][a2] = float(b3[a3])
            b2[a2][a1] = b2[a1][a2]
            a2 += 1
            a3 += 1
        a1 += 1
with open("distance_matrix_final.csv", "r+") as file_with_id, open("distance_matrix_final_withoutid.csv", "r+") as file_without_id:
    for a1 in range(8357):
        file_with_id.write(str(b1[a1]) + ",")
        file_without_id.write(str(b1[a1]) + ",")
        for a2 in range(8357):
            file_with_id.write(str(b2[a1][a2]))
            file_without_id.write(str(b2[a1][a2]))
            if a2 != 8356:
                file_with_id.write(",")
                file_without_id.write(",")
        file_with_id.write("\n")
        file_without_id.write("\n")