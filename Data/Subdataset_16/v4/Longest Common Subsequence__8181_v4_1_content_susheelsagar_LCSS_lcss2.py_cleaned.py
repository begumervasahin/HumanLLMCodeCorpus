import mysql.connector
import numpy as np
import copy
def fonk1(b7, b8):
    b1 = ['"Fri"', '"Sat"', '"Sun"', '"Mon"', '"Tue"', '"Wed"', '"Thu"']
    b2 = {day: [] for day in b1}
    b3 = {day: [] for day in b1}
    for row in b7:
        if row[1] in b2:
            b2[row[1]].append(row)
    for row in b8:
        if row[1] in b3:
            b3[row[1]].append(row)
    a1 = 0
    for day in b1:
        if len(b2[day]) < len(b3[day]):
            a1 += fonk2(b2[day], b3[day])
        else:
            a1 += fonk2(b3[day], b2[day])
    return a1
def fonk2(b7, b8):
    a1 = 0
    while b7 and b8:
        if b7[-1][2] == b8[-1][2] and b7[-1][0] == b8[-1][0]:
            a1 += 1
            b7.pop()
            b8.pop()
        elif b7[-1][2] > b8[-1][2]:
            b7.pop()
        elif b7[-1][2] < b8[-1][2]:
            b8.pop()
        else:
            if b7[-2][2] == b8[-1][2]:
                b7.pop()
            elif b7[-1][2] == b8[-2][2]:
                b8.pop()
            else:
                b7.pop()
                b8.pop()
    return a1
def fonk3():
    b4 = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
    b5 = b4.cursor(buffered=True)
    b5.execute("SELECT DISTINCT a2 FROM fulldata")
    b6 = [a for a in b5]
    with open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv') as f:
        b7 = []
        b8 = []
        a2 = 0
        for line in f:
            if line.startswith("a2"):
                continue
            b9 = line.strip().split(",")
            if a2 = = int(b9[0]):
                b8.append([b9[1], b9[2], b9[3]])
            else:
                if b8:
                    b7.append(b8)
                b8 = [[b9[1], b9[2], b9[3]]]
                a2 = int(b9[0])
        if b8:
            b7.append(b8)
    print(len(b7))
    b10 = np.ones((8357, 8357))
    for j in range(8356):
        print(j)
        b11 = copy.deepcopy(b7[j])
        for i in range(j + 1, 8357):
            b12 = b12 = copy.deepcopy(b7[i])
            b10[j][i] = fonk1(b11, b12)
    b4.close()
if b13 = = "__main__":
    fonk3()