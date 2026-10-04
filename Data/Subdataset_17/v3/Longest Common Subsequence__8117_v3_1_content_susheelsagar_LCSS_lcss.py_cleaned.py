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
    score = sum(cal_sim(traj1_dict[day], traj2_dict[day]) for day in days)
    print("The score is", score)
    return score
def cal_sim(traj1, traj2):
    score = 0
    while traj1 and traj2:
        traj1_last = traj1[-1]
        traj2_last = traj2[-1]
        if traj1_last[2] == traj2_last[2] and traj1_last[0] == traj2_last[0]:
            score += 1
            traj1.pop()
            traj2.pop()
        elif traj1_last[2] > traj2_last[2]:
            traj1.pop()
        elif traj1_last[2] < traj2_last[2]:
            traj2.pop()
        else:
            if len(traj1) > 1 and traj1[-2][2] == traj2_last[2]:
                traj1.pop()
            elif len(traj2) > 1 and traj1_last[2] == traj2[-2][2]:
                traj2.pop()
            else:
                traj1.pop()
                traj2.pop()
    return score
def fetch_user_trajectories(cursor, user_id):
    cursor.execute("SELECT siteid, weekday, timing FROM fulldata WHERE userid = %s", (user_id,))
    return [(siteid, weekday, timing) for siteid, weekday, timing in cursor]
def main():
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT DISTINCT userid FROM fulldata")
    user_ids = [row[0] for row in cursor]
    num_users = len(user_ids)
    similarity = np.ones((num_users, num_users))
    for user_num, user_id in enumerate(user_ids):
        traj1 = fetch_user_trajectories(cursor, user_id)
        for next_user_num in range(user_num + 1, num_users):
            next_user_id = user_ids[next_user_num]
            traj2 = fetch_user_trajectories(cursor, next_user_id)
            print(f"Calculating similarity between user {user_num} and user {next_user_num}")
            similarity[user_num, next_user_num] = similarity_lcss(traj1, traj2)
    cnx.close()
if __name__ == "__main__":
    main()