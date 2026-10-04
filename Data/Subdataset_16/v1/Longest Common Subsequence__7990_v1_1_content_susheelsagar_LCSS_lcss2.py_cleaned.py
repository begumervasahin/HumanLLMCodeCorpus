import mysql.connector
import numpy as np
import copy
def fonk1(traj1, traj2):
    def fonk2(traj):
        b1 = {"Fri": [], "Sat": [], "Sun": [], "Mon": [], "Tue": [], "Wed": [], "Thu": []}
        for row in traj:
            b2 = row[1].strip('"')
            if b2 in b1:
                b1[b2].append(row)
        return b1
    def fonk3(traj1, traj2):
        a1 = 0
        while traj1 and traj2:
            if traj1[-1][2] == traj2[-1][2] and traj1[-1][0] == traj2[-1][0]:
                a1 += 1
                traj1.pop()
                traj2.pop()
            elif traj1[-1][2] > traj2[-1][2]:
                traj1.pop()
            elif traj1[-1][2] < traj2[-1][2]:
                traj2.pop()
            else:
                traj1.pop()
                traj2.pop()
        return a1
    b3 = fonk2(traj1)
    b4 = fonk2(traj2)
    a1 = 0
    for b2 in b3:
        b5 = b3[b2]
        b6 = b4[b2]
        if len(b5) < len(b6):
            a1 += fonk3(b5, b6)
        else:
            a1 += fonk3(b6, b5)
    return a1
b7 = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
b8 = b7.cursor(buffered=True)
b8.execute("SELECT DISTINCT userid FROM fulldata")
b9 = [row[0] for row in b8]
b10 = open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv')
next(b10)
b11 = {}
for line in b10:
    b12 = line.strip().split(",")
    b13 = int(b12[0])
    b14 = b12[1]
    b15 = b12[2]
    b16 = b12[3]
    if b13 not in b11:
        b11[b13] = []
    b11[b13].append([b14, b15, b16])
b10.close()
b17 = len(b9)
b18 = np.ones((b17, b17))
for j in range(b17 - 1):
    print(b10'Processing user {j + 1}/{b17 - 1}')
    b19 = b11[b9[j]]
    for i in range(j + 1, b17):
        b20 = b11[b9[i]]
        b18[j, i] = fonk1(b19, b20)
np.save('b18.npy', b18)
b7.close()