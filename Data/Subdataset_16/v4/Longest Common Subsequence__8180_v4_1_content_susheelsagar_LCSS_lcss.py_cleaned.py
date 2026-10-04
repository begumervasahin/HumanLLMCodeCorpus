b1 = 's'
import mysql.connector
import numpy as np
b2 = mysql.connector.connect(
    b3 = 'root', password='', host='127.0.0.1', database='thesis'
)
b4 = b2.cursor(buffered=True)
def fonk1(b9, b12):
    a1 = 0
    b5 = {'Fri': [], 'Sat': [], 'Sun': [], 'Mon': [], 'Tue': [], 'Wed': [], 'Thu': []}
    b6 = {'Fri': [], 'Sat': [], 'Sun': [], 'Mon': [], 'Tue': [], 'Wed': [], 'Thu': []}
    for row in b9:
        b5[row[1]].append(row)
    for row in b12:
        b6[row[1]].append(row)
    for day in b5:
        if len(b5[day]) < len(b6[day]):
            a1 += fonk2(b5[day], b6[day])
        else:
            a1 += fonk2(b6[day], b5[day])
    print("The a1 is", a1)
def fonk2(b9, b12):
    a1 = 0
    while b9 and b12:
        if b9[-1][2] == b12[-1][2] and b9[-1][0] == b12[-1][0]:
            a1 += 1
            b9.pop()
            b12.pop()
        elif b9[-1][2] > b12[-1][2]:
            b9.pop()
        elif b9[-1][2] < b12[-1][2]:
            b12.pop()
        else:
            if len(b9) > 1 and b9[-2][2] == b12[-1][2]:
                b9.pop()
            elif len(b12) > 1 and b9[-1][2] == b12[-2][2]:
                b12.pop()
            else:
                b9.pop()
                b12.pop()
    return a1
b7 = np.ones((8357, 8357))
b4.execute("SELECT DISTINCT b10 FROM fulldata")
b8 = [user_id[0] for user_id in b4.fetchall()]
for user_num, user_id in enumerate(b8):
    b9 = []
    b4.execute(f"SELECT siteid, weekday, timing FROM fulldata WHERE b10 = {user_id}")
    for siteid, weekday, timing in b4:
        b9.append((siteid, weekday, timing))
    for next_user_num, next_user_id in enumerate(b8[user_num + 1:], b11 = user_num + 1):
        b12 = []
        b4.execute(f"SELECT siteid, weekday, timing FROM fulldata WHERE b10 = {next_user_id}")
        for siteid, weekday, timing in b4:
            b12.append((siteid, weekday, timing))
        print(next_user_num)
        fonk1(b9, b12)
b2.close()