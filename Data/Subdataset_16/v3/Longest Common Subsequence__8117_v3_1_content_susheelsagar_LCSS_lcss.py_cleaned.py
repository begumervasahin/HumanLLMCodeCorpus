import mysql.connector
import numpy as np
def fonk1(b13, b15):
    b1 = ['Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu']
    b2 = {day: [] for day in b1}
    b3 = {day: [] for day in b1}
    for row in b13:
        b2[row[1]].append(row)
    for row in b15:
        b3[row[1]].append(row)
    b4 = sum(fonk2(b2[day], b3[day]) for day in b1)
    print("The b4 is", b4)
    return b4
def fonk2(b13, b15):
    b4 = 0
    while b13 and b15:
        b5 = b13[-1]
        b6 = b15[-1]
        if b5[2] == b6[2] and b5[0] == b6[0]:
            b4 += 1
            b13.pop()
            b15.pop()
        elif b5[2] > b6[2]:
            b13.pop()
        elif b5[2] < b6[2]:
            b15.pop()
        else:
            if len(b13) > 1 and b13[-2][2] == b6[2]:
                b13.pop()
            elif len(b15) > 1 and b5[2] == b15[-2][2]:
                b15.pop()
            else:
                b13.pop()
                b15.pop()
    return b4
def fonk3(b9, user_id):
    b9.execute("SELECT siteid, weekday, timing FROM fulldata WHERE b7 = %s", (user_id,))
    return [(siteid, weekday, timing) for siteid, weekday, timing in b9]
def fonk4():
    b8 = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
    b9 = b8.b9(buffered=True)
    b9.execute("SELECT DISTINCT b7 FROM fulldata")
    b10 = [row[0] for row in b9]
    b11 = len(b10)
    b12 = np.ones((b11, b11))
    for user_num, user_id in enumerate(b10):
        b13 = fonk3(b9, user_id)
        for next_user_num in range(user_num + 1, b11):
            b14 = b10[next_user_num]
            b15 = fonk3(b9, b14)
            print(f"Calculating b12 between user {user_num} and user {next_user_num}")
            b12[user_num, next_user_num] = fonk1(b13, b15)
    b8.close()
if b16 = = "__main__":
    fonk4()