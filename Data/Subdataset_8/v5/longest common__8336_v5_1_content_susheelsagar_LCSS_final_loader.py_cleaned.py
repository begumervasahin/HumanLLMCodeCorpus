import numpy as np
def read_distance_matrix(filename):
    users = []
    matrix = np.zeros((8357, 8357))
    i = 0
    with open(filename, "r") as file:
        for line in file:
            elements = line.strip().split(",")
            users.append(elements[0])
            j = 0
            k = 1
            while k < len(elements):
                matrix[i][j] = float(elements[k])
                matrix[j][i] = matrix[i][j]
                j += 1
                k += 1
            i += 1
    return users, matrix
def write_distance_matrix(users, matrix, filename_with_id, filename_without_id):
    with open(filename_with_id, "w") as file_with_id, open(filename_without_id, "w") as file_without_id:
        for i, user in enumerate(users):
            file_with_id.write(str(user) + ",")
            file_without_id.write(str(user) + ",")
            for j in range(len(users)):
                file_with_id.write(str(matrix[i][j]))
                file_without_id.write(str(matrix[i][j]))
                if j != len(users) - 1:
                    file_with_id.write(",")
                    file_without_id.write(",")
            file_with_id.write("\n")
            file_without_id.write("\n")
users_full, matrix_full = read_distance_matrix("distance_matrix_full.csv")
users_additional, matrix_additional = read_distance_matrix("distance_matrix_1698.csv")
all_users = users_full + users_additional
combined_matrix = np.concatenate((matrix_full, matrix_additional), axis=0)
write_distance_matrix(all_users, combined_matrix, "distance_matrix_final.csv", "distance_matrix_final_withoutid.csv")