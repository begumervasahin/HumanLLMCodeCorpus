import numpy as np
def load_mobility_data(filepath):
    traj1 = []
    current_traj = []
    lst_users = []
    current_userid = None
    with open(filepath, 'r') as file:
        for line_num, line in enumerate(file):
            if line_num == 0:
                continue
            data = line.strip().split(",")
            userid = int(data[0])
            if userid == current_userid:
                current_traj.append([data[1], data[2], data[3]])
            else:
                if current_traj:
                    traj1.append(current_traj)
                current_traj = [[data[1], data[2], data[3]]]
                lst_users.append(data[0])
                current_userid = userid
        if current_traj:
            traj1.append(current_traj)
    print("Loading done")
    return traj1, lst_users
def load_distance_matrix(filepath, lst_users):
    num_users = len(lst_users)
    distance_matrix = np.zeros((num_users, num_users))
    with open(filepath, 'r') as file:
        for i, line in enumerate(file):
            data = line.strip().split(",")
            if lst_users[i] != data[0]:
                print(f'Error: Mismatch in user IDs at index {i}')
            for j, value in enumerate(data[1:]):
                distance_matrix[i][j] = float(value)
                if float(value) == 0.0 and i != j:
                    print(f"Error at {i}, {j}")
    return distance_matrix
def check_distance_matrix_symmetry(distance_matrix):
    num_users = distance_matrix.shape[0]
    for i in range(num_users):
        for j in range(num_users):
            if distance_matrix[i][j] != distance_matrix[j][i]:
                print(f"Error at {i}, {j}")
def main():
    mobility_filepath = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
    distance_matrix_filepath = 'distance_matrix_final.csv'
    traj1, lst_users = load_mobility_data(mobility_filepath)
    distance_matrix = load_distance_matrix(distance_matrix_filepath, lst_users)
    check_distance_matrix_symmetry(distance_matrix)
if __name__ == "__main__":
    main()