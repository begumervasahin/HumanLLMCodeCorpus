import numpy as np
def fonk1(filename):
    b1 = []
    b2 = np.zeros((8357, 8357))
    with open(filename, "r") as file:
        for i, line in enumerate(file):
            b3 = line.strip().split(",")
            b1.append(b3[0])
            for j in range(1, len(b3)):
                b2[i][j - 1] = float(b3[j])
                b2[j - 1][i] = b2[i][j - 1]
    return b1, b2
def fonk2(b1, b2, filename_with_id, filename_without_id):
    with open(filename_with_id, "w") as file_with_id, open(filename_without_id, "w") as file_without_id:
        for i, user in enumerate(b1):
            file_with_id.write(str(user) + ",")
            file_without_id.write(str(user) + ",")
            for j in range(len(b1)):
                file_with_id.write(str(b2[i][j]))
                file_without_id.write(str(b2[i][j]))
                if j != len(b1) - 1:
                    file_with_id.write(",")
                    file_without_id.write(",")
            file_with_id.write("\n")
            file_without_id.write("\n")
users_full, b4 = fonk1("distance_matrix_full.csv")
users_additional, b5 = fonk1("distance_matrix_1698.csv")
b6 = users_full + users_additional
b7 = np.concatenate((b4, b5), axis=0)
fonk2(b6, b7, "distance_matrix_final.csv", "distance_matrix_final_withoutid.csv")