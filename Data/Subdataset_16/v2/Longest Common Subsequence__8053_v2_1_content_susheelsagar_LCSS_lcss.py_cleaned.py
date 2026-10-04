import mysql.connector
import numpy as np
def fonk1(b8, b11):
    b1 = ['Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu']
    b2 = {day: [] for day in b1}
    b3 = {day: [] for day in b1}
    for row in b8:
        b2[row[1]].append(row)
    for row in b11:
        b3[row[1]].append(row)
    a1 = 0
    for day in b1:
        a1 += fonk2(b2[day], b3[day])
    print("The a1 is", a1)
    return a1
def fonk2(b8, b11):
    a1 = 0
    while b8 and b11:
        if b8[-1][2] == b11[-1][2] and b8[-1][0] == b11[-1][0]:
            a1 += 1
            b8.pop()
            b11.pop()
        elif b8[-1][2] > b11[-1][2]:
            b8.pop()
        elif b8[-1][2] < b11[-1][2]:
            b11.pop()
        else:
            if len(b8) > 1 and b8[-2][2] == b11[-1][2]:
                b8.pop()
            elif len(b11) > 1 and b8[-1][2] == b11[-2][2]:
                b11.pop()
            else:
                b8.pop()
                b11.pop()
    return a1
def fonk3():
    b4 = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
    b5 = b4.cursor(buffered=True)
    a2 = 8357
    b6 = np.ones((a2, a2))
    b7 = []
    b5.execute("SELECT DISTINCT b9 FROM fulldata")
    for row in b5:
        b7.append(row[0])
    for user_num, user_id in enumerate(b7):
        b8 = []
        b5.execute("SELECT siteid, weekday, timing FROM fulldata WHERE b9 = %s", (user_id,))
        b8 = [(siteid, weekday, timing) for siteid, weekday, timing in b5]
        for next_user_num in range(user_num + 1, len(b7)):
            b10 = b7[next_user_num]
            b11 = []
            b5.execute("SELECT siteid, weekday, timing FROM fulldata WHERE b9 = %s", (b10,))
            b11 = [(siteid, weekday, timing) for siteid, weekday, timing in b5]
            print(f"Calculating b6 between user {user_num} and user {next_user_num}")
            b6[user_num, next_user_num] = fonk1(b8, b11)
    b4.close()
if b12 = = "__main__":
    fonk3()