import numpy as np
with open("distance_matrix_full.csv", "r") as f:
    lst_users = []
    distance = np.zeros((8357, 8357))
    for i, line in enumerate(f):
        data = line.strip().split(",")
        lst_users.append(data[0])
        for j in range(1, len(data)):
            distance[i][j-1] = float(data[j])
            distance[j-1][i] = distance[i][j-1]
with open("distance_matrix_1698.csv", "r") as f:
    for i, line in enumerate(f):
        data = line.strip().split(",")
        lst_users.append(data[0])
        for j in range(1, len(data)):
            distance[i+8357][j-1] = float(data[j])
            distance[j-1][i+8357] = distance[i+8357][j-1]
with open("distance_matrix_final.csv", "w") as f2, open("distance_matrix_final_withoutid.csv", "w") as f3:
    for i in range(8357):
        f2.write(str(lst_users[i]) + ",")
        f3.write(str(lst_users[i]) + ",")
        for j in range(8357):
            f2.write(str(distance[i][j]))
            f3.write(str(distance[i][j]))
            if j != 8356:
                f2.write(",")
                f3.write(",")
        f2.write("\n")
        f3.write("\n")