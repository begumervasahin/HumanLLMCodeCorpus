import mysql.connector
import numpy as np
import copy
def similarity_lcss(traj1, traj2):
    days = ['"Fri"', '"Sat"', '"Sun"', '"Mon"', '"Tue"', '"Wed"', '"Thu"']
    traj1_days = {day: [] for day in days}
    traj2_days = {day: [] for day in days}
    for row in traj1:
        if row[1] in traj1_days:
            traj1_days[row[1]].append(row)
    for row in traj2:
        if row[1] in traj2_days:
            traj2_days[row[1]].append(row)
    score = 0
    for day in days:
        if len(traj1_days[day]) < len(traj2_days[day]):
            score += cal_sim(traj1_days[day], traj2_days[day])
        else:
            score += cal_sim(traj2_days[day], traj1_days[day])
    return score
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
            if traj1[-2][2] == traj2[-1][2]:
                traj1.pop()
            elif traj1[-1][2] == traj2[-2][2]:
                traj2.pop()
            else:
                traj1.pop()
                traj2.pop()
    return score
def main():
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
    c = cnx.cursor(buffered=True)
    c.execute("SELECT DISTINCT userid FROM fulldata")
    lst = [a for a in c]
    with open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv') as f:
        traj1 = []
        traj2 = []
        userid = 0
        for line in f:
            if line.startswith("userid"):
                continue
            m = line.strip().split(",")
            if userid == int(m[0]):
                traj2.append([m[1], m[2], m[3]])
            else:
                if traj2:
                    traj1.append(traj2)
                traj2 = [[m[1], m[2], m[3]]]
                userid = int(m[0])
        if traj2:
            traj1.append(traj2)
    print(len(traj1))
    similarity = np.ones((8357, 8357))
    for j in range(8356):
        print(j)
        user1 = copy.deepcopy(traj1[j])
        for i in range(j + 1, 8357):
            user2 =
  user2 = copy.deepcopy(traj1[i])
            similarity[j][i] = similarity_lcss(user1, user2)
    cnx.close()
if __name__ == "__main__":
    main()