import mysql.connector
import numpy as np
def similarity_lcss(traj1, traj2):
    days = ['Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu']
    traj1_dict = {day: [] for day in days}
    traj2_dict = {day: [] for day in days}
    for row in traj1:
        traj1_dict[row[1]].append(row)
    for row in traj2:
        traj2_dict[row[1]].append(row)
    score = 0
    for day in days:
        score += cal_sim(traj1_dict[day], traj2_dict[day])
    print("The score is", score)
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
            if len(traj1) > 1 and traj1[-2][2] == traj2[-1][2]:
                traj1.pop()
            elif len(traj2) > 1 and traj1[-1][2] == traj2[-2][2]:
                traj2.pop()
            else:
                traj1.pop()
                traj2.pop()
    return score
def main():
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
    c = cnx.cursor(buffered=True)
    num_users = 8357
    similarity = np.ones((num_users, num_users))
    user_ids = []
    c.execute("SELECT DISTINCT userid FROM fulldata")
    for row in c:
        user_ids.append(row[0])
    for user_num, user_id in enumerate(user_ids):
        traj1 = []
        c.execute("SELECT siteid, weekday, timing FROM fulldata WHERE userid = %s", (user_id,))
        traj1 = [(siteid, weekday, timing) for siteid, weekday, timing in c]
        for next_user_num in range(user_num + 1, len(user_ids)):
            next_user_id = user_ids[next_user_num]
            traj2 = []
            c.execute("SELECT siteid, weekday, timing FROM fulldata WHERE userid = %s", (next_user_id,))
            traj2 = [(siteid, weekday, timing) for siteid, weekday, timing in c]
            print(f"Calculating similarity between user {user_num} and user {next_user_num}")
            similarity[user_num, next_user_num] = similarity_lcss(traj1, traj2)
    cnx.close()
if __name__ == "__main__":
    main()