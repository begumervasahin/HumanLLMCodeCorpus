import mysql.connector
import numpy as np
import copy
def similarity_lcss(traj1, traj2):
    def split_by_days(traj):
        days = {"Fri": [], "Sat": [], "Sun": [], "Mon": [], "Tue": [], "Wed": [], "Thu": []}
        for row in traj:
            day = row[1].strip('"')
            if day in days:
                days[day].append(row)
        return days
    def cal_sim(traj1, traj2):
        score = 0
        while traj1 and traj2:
            if traj1[-1][2] == traj2[-1][2] and traj1[-1][0] == traj2[-1][0]:
                score += 1
                traj1.pop()
                traj2.pop()
            elif traj1[-1][2] > traj2[-1][2]:
                traj1.pop()
            elif traj1[-1][2] < traj2[-1][2]:
                traj2.pop()
            else:
                traj1.pop()
                traj2.pop()
        return score
    traj1_days = split_by_days(traj1)
    traj2_days = split_by_days(traj2)
    score = 0
    for day in traj1_days:
        traj1_day = traj1_days[day]
        traj2_day = traj2_days[day]
        if len(traj1_day) < len(traj2_day):
            score += cal_sim(traj1_day, traj2_day)
        else:
            score += cal_sim(traj2_day, traj1_day)
    return score
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
c = cnx.cursor(buffered=True)
c.execute("SELECT DISTINCT userid FROM fulldata")
user_ids = [row[0] for row in c]
f = open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv')
next(f)
trajectories = {}
for line in f:
    m = line.strip().split(",")
    user_id = int(m[0])
    siteid = m[1]
    weekday = m[2]
    timing = m[3]
    if user_id not in trajectories:
        trajectories[user_id] = []
    trajectories[user_id].append([siteid, weekday, timing])
f.close()
user_count = len(user_ids)
similarity_matrix = np.ones((user_count, user_count))
for j in range(user_count - 1):
    print(f'Processing user {j + 1}/{user_count - 1}')
    user1_traj = trajectories[user_ids[j]]
    for i in range(j + 1, user_count):
        user2_traj = trajectories[user_ids[i]]
        similarity_matrix[j, i] = similarity_lcss(user1_traj, user2_traj)
np.save('similarity_matrix.npy', similarity_matrix)
cnx.close()