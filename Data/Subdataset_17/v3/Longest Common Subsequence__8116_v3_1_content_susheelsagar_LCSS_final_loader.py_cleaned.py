import numpy as np
num_users_full = 8357
num_users_additional = 1698
total_users = num_users_full + num_users_additional
distance = np.zeros((total_users, total_users))
lst_users = []
def read_distance_matrix(file_path, start_index):
    with open(file_path, "r") as f:
        for i, line in enumerate(f, start=start_index):
            values = line.strip().split(",")
            lst_users.append(values[0])
            for j, value in enumerate(values[1:], start=0):
                distance[i][j] = float(value)
                distance[j][i] = distance[i][j]
read_distance_matrix("distance_matrix_full.csv", 0)
read_distance_matrix("distance_matrix_1698.csv", num_users_full)
def write_distance_matrix(file_path, include_user_ids=True):
    with open(file_path, "w") as f:
        for i in range(total_users):
            if include_user_ids:
                f.write(lst_users[i] + ",")
            f.write(",".join(map(str, distance[i])) + "\n")
write_distance_matrix("distance_matrix_final.csv", include_user_ids=True)
write_distance_matrix("distance_matrix_final_withoutid.csv", include_user_ids=False)