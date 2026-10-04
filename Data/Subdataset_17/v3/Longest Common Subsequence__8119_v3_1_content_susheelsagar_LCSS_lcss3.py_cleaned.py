import numpy as np
import copy
def similarity_lcss(traj1, traj2):
    def cal_sim(traj1, traj2):
        score = 0
        while traj2:
            len2 = len(traj1) - 1
            while len2 > -1:
                if traj2[-1][2] == traj1[len2][2] and traj2[-1][0] == traj1[len2][0]:
                    score += 1
                len2 -= 1
            traj2.pop()
        return score
    days = ["Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]
    traj1_days = {day: [] for day in days}
    traj2_days = {day: [] for day in days}
    for row in traj1:
        traj1_days[row[1].strip('"')].append(row)
    for row in traj2:
        traj2_days[row[1].strip('"')].append(row)
    score = 0
    min_traj = min(len(traj1), len(traj2))
    for day in days:
        if len(traj1_days[day]) < len(traj2_days[day]):
            score += cal_sim(traj1_days[day], traj2_days[day])
        else:
            score += cal_sim(traj2_days[day], traj1_days[day])
    distance = float(score) / min_traj
    return 1.0 - distance
def read_trajectory_file(file_path):
    with open(file_path, 'r') as f:
        next(f)
        data = f.readlines()
    return data
def process_trajectory_data(data):
    traj1 = []
    traj2 = []
    lst_users = []
    userid = None
    for line in data:
        m = line.split(",")
        current_userid = int(m[0])
        if userid == current_userid:
            traj2.append([m[1], m[2], m[3].strip()])
        else:
            userid = current_userid
            if traj2:
                traj1.append(traj2)
            traj2 = [[m[1], m[2], m[3].strip()]]
            lst_users.append(m[0])
    if traj2:
        traj1.append(traj2)
    return traj1, lst_users
def write_distance_matrix(distance_matrix, lst_users, output_file_full, output_file_withoutid):
    with open(output_file_full, 'w') as f1, open(output_file_withoutid, 'w') as f2:
        for j in range(len(distance_matrix)):
            f1.write(f"{lst_users[j]},{','.join(map(str, distance_matrix[j]))}\n")
            f2.write(f"{','.join(map(str, distance_matrix[j]))}\n")
def main():
    trajectory_file = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
    output_file_full = 'distance_matrix_full.csv'
    output_file_withoutid = 'distance_matrix_full_withoutid.csv'
    data = read_trajectory_file(trajectory_file)
    traj1, lst_users = process_trajectory_data(data)
    num_users = len(traj1)
    distance_matrix = np.zeros((num_users, num_users))
    for j in range(num_users - 1):
        print(f"Processing user {j}")
        user1 = copy.deepcopy(traj1[j])
        for i in range(j + 1, num_users):
            user2 = copy.deepcopy(traj1[i])
            distance_matrix[j][i] = similarity_lcss(user1, user2)
            distance_matrix[i][j] = distance_matrix[j][i]
    write_distance_matrix(distance_matrix, lst_users, output_file_full, output_file_withoutid)
if __name__ == "__main__":
    main()