import numpy as np
with open("distance_matrix_full.csv", "r") as f:
    lst_users = []
    num_users = 8357
    distance = np.zeros((num_users, num_users))
    for i, line in enumerate(f):
        elements = line.strip().split(",")
        lst_users.append(elements[0])
        for j, value in enumerate(elements[1:], start=0):
            distance[i][j] = float(value)
            distance[j][i] = float(value)
with open("distance_matrix_1698.csv", "r") as f1:
    for i, line in enumerate(f1, start=num_users):
        elements = line.strip().split(",")
        lst_users.append(elements[0])
        for j, value in enumerate(elements[1:], start=0):
            distance[i][j] = float(value)
            distance[j][i] = float(value)
with open("distance_matrix_final.csv", "w") as f2, open("distance_matrix_final_withoutid.csv", "w") as f3:
    for i in range(num_users):
        f2.write(f"{lst_users[i]},{','.join(map(str, distance[i]))}\n")
        f3.write(f"{','.join(map(str, distance[i]))}\n")