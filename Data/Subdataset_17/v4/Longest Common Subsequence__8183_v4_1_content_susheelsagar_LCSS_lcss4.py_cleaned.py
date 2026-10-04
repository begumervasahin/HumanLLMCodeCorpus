import mysql.connector
import numpy as np
import copy
def similarity_lcss(traj1, traj2):
    score = 0
    min_traj = min(len(traj1), len(traj2))
    days_of_week = ['"Fri"', '"Sat"', '"Sun"', '"Mon"', '"Tue"', '"Wed"', '"Thu"']
    traj1_days = {day: [] for day in days_of_week}
    traj2_days = {day: [] for day in days_of_week}
    for row in traj1:
        if row[1] in traj1_days:
            traj1_days[row[1]].append(row)
    for row in traj2:
        if row[1] in traj2_days:
            traj2_days[row[1]].append(row)
    for day in days_of_week:
        if len(traj1_days[day]) < len(traj2_days[day]):
            score += cal_sim(traj1_days[day], traj2_days[day])
        else:
            score += cal_sim(traj2_days[day], traj1_days[day])
    distance = float(score) / min_traj
    distance = 1 - distance
    return distance
def cal_sim(traj1, traj2):
    score = 0
    while traj2:
        len2 = len(traj1) - 1
        while len2 >= 0:
            if traj2[-1][2] == traj1[len2][2] and traj2[-1][0] == traj1[len2][0]:
                score += 1
            len2 -= 1
        traj2.pop()
    return score
def main():
    distance = np.zeros((8357, 8357))
    traj1 = []
    traj2 = []
    userid = 0
    lst_users = []
    with open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv') as f:
        next(f)
        for line in f:
            m = line.strip().split(",")
            if userid == int(m[0]):
                traj2.append([m[1], str(m[2]), m[3]])
            else:
                userid = int(m[0])
                if traj2:
                    traj1.append(traj2)
                traj2 = [[m[1], str(m[2]), m[3]]]
                lst_users.append(m[0])
        traj1.append(traj2)
    with open('distance_matrix_1698.csv', 'w') as f1, open('distance_matrix_1698_withoutid.csv', 'w') as f2:
        print(lst_users[1697])
        j = 1698
        while j < 8356:
            print(f"j= {j}")
            user1 = copy.deepcopy(traj1[j])
            for i in range(j + 1, 8357):
                user2 = copy.deepcopy(traj1[i])
                distance[j][i] = similarity_lcss(user1, user2)
                distance[i][j] = distance[j][i]
            f1.write(f"{lst_users[j]},{distance[j][j]}")
            f2.write(f"{distance[j][j]}")
            for k in range(j + 1, 8357):
                f1.write(f",{distance[j][k]}")
                f2.write(f",{distance[j][k]}")
            f1.write("\n")
            f2.write("\n")
            j += 1
if __name__ == "__main__":
    main()