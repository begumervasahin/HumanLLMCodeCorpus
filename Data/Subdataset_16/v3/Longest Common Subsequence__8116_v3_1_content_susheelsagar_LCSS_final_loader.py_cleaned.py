import numpy as np
a1 = 8357
a2 = 1698
b1 = a1 + a2
b2 = np.zeros((b1, b1))
b3 = []
def fonk1(file_path, start_index):
    with open(file_path, "r") as f:
        for i, line in enumerate(f, b4 = start_index):
            b5 = line.strip().split(",")
            b3.append(b5[0])
            for j, value in enumerate(b5[1:], b4 = 0):
                b2[i][j] = float(value)
                b2[j][i] = b2[i][j]
fonk1("distance_matrix_full.csv", 0)
fonk1("distance_matrix_1698.csv", a1)
def fonk2(file_path, b6 = True):
    with open(file_path, "w") as f:
        for i in range(b1):
            if b6:
                f.write(b3[i] + ",")
            f.write(",".join(map(str, b2[i])) + "\n")
fonk2("distance_matrix_final.csv", b6 = True)
fonk2("distance_matrix_final_withoutid.csv", b6 = False)