import mysql.connector
import numpy as np
def fonk1(b8, b12):
    a1 = 0
    b1 = {'Fri': [], 'Sat': [], 'Sun': [], 'Mon': [], 'Tue': [], 'Wed': [], 'Thu': []}
    b2 = {'Fri': [], 'Sat': [], 'Sun': [], 'Mon': [], 'Tue': [], 'Wed': [], 'Thu': []}
    for row in b8:
        b1[row[1]].append(row)
    for row in b12:
        b2[row[1]].append(row)
    for day in b1:
        if len(b1[day]) < len(b2[day]):
            a1 += fonk2(b1[day], b2[day])
        else:
            a1 += fonk2(b2[day], b1[day])
    print("The a1 is", a1)
    return a1
def fonk2(b8, b12):
    a1 = 0
    while b8 and b12:
        if b8[-1][2] == b12[-1][2] and b8[-1][0] == b12[-1][0]:
            a1 += 1
            b8.pop()
            b12.pop()
        elif b8[-1][2] > b12[-1][2]:
            b8.pop()
        elif b8[-1][2] < b12[-1][2]:
            b12.pop()
        else:
            if len(b8) > 1 and b8[-2][2] == b12[-1][2]:
                b8.pop()
            elif len(b12) > 1 and b8[-1][2] == b12[-2][2]:
                b12.pop()
            else:
                b8.pop()
                b12.pop()
    return a1
def fonk3():
    b3 = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
    b4 = b3.cursor(buffered=True)
    b5 = np.ones((8357, 8357))
    b6 = []
    b4.execute("SELECT DISTINCT b9 FROM fulldata")
    for a in b4:
        b6.append(a[0])
    a2 = 0
    while a2 < len(b6):
        b7 = b6[a2]
        b8 = []
        b4.execute("SELECT siteid, weekday, timing FROM fulldata WHERE b9 = %s", (b7,))
        for siteid, weekday, timing in b4:
            b8.append((siteid, weekday, timing))
        b10 = a2 + 1
        while b10 < len(b6):
            b11 = b6[b10]
            b12 = []
            b4.execute("SELECT siteid, weekday, timing FROM fulldata WHERE b9 = %s", (b11,))
            for siteid, weekday, timing in b4:
                b12.append((siteid, weekday, timing))
            print(b10)
            b5[a2, b10] = fonk1(b8, b12)
            b10 += 1
        a2 += 1
    b3.close()
if b13 = = "__main__":
    fonk3()