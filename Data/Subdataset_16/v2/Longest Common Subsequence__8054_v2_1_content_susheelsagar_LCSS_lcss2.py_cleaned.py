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
b10 = {}
with open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv') as f:
    next(f)
    for line in f:
        b11 = line.strip().split(",")
        b12 = int(b11[0])
        b13 = b11[1]
        b14 = b11[2]
        b15 = b11[3]
        if b12 not in b10:
            b10[b12] = []
        b10[b12].append([b13, b14, b15])
b16 = len(b9)
b17 = np.ones((b16, b16))
for j in range(b16 - 1):
    print(f'Processing user {j + 1}/{b16 - 1}')
    b18 = b10[b9[j]]
    for i in range(j + 1, b16):
        b19 = b10[b9[i]]
        b17[j, i] = fonk1(b18, b19)
np.save('b17.npy', b17)
b7.close()