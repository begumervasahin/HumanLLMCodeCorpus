import numpy as np
def read_distance_matrix(filename):
    users = []
    matrix = np.zeros((8357, 8357))
    with open(filename, "r") as file:
        for i, line in enumerate(file):
            data = line.strip().split(",")
            users.append(data[0])
            for j in range(1, len(data)):
                matrix[i][j - 1] = float(data[j])
                matrix[j - 1][i] = matrix[i][j - 1]
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