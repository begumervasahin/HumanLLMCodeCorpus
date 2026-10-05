import numpy as np
with open("distance_matrix_full.csv", "r+") as file:
    lst_users = []
    distance = np.zeros((8357, 8357))
    i = 0
    for line in iter(file):
        elements = line.split(",")
        lst_users.append(elements[0])
        j = 0
        k = 1
        while k < len(elements):
            distance[i][j] = float(elements[k])
            distance[j][i] = distance[i][j]
            j += 1
            k += 1
        i += 1
with open("distance_matrix_1698.csv", "r+") as file:
    for line in iter(file):
        elements = line.split(",")
        lst_users.append(elements[0])
        j = i
        k = 1
        while k < len(elements):
            distance[i][j] = float(elements[k])
            distance[j][i] = distance[i][j]
            j += 1
            k += 1
        i += 1
with open("distance_matrix_final.csv", "r+") as file_with_id, open("distance_matrix_final_withoutid.csv", "r+") as file_without_id:
    for i in range(8357):
        file_with_id.write(str(lst_users[i]) + ",")
        file_without_id.write(str(lst_users[i]) + ",")
        for j in range(8357):
            file_with_id.write(str(distance[i][j]))
            file_without_id.write(str(distance[i][j]))
            if j != 8356:
                file_with_id.write(",")
                file_without_id.write(",")
        file_with_id.write("\n")
        file_without_id.write("\n")