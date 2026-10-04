import mysql.connector
import numpy as np
import copy
def fonk1(traj):
    b1 = {"Fri": [], "Sat": [], "Sun": [], "Mon": [], "Tue": [], "Wed": [], "Thu": []}
    for row in traj:
        b2 = row[1].strip('"')
        if b2 in b1:
            b1[b2].append(row)
    return b1
def fonk2(traj1, traj2):
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
def fonk3(traj1, traj2):
    b3 = fonk1(traj1)
    b4 = fonk1(traj2)
    a1 = 0
    for b2 in b3:
        b5 = b3[b2]
        b6 = b4[b2]
        if len(b5) < len(b6):
            a1 += fonk2(b5, b6)
        else:
            a1 += fonk2(b6, b5)
    return a1
def fonk4(b18):
    b18.execute("SELECT DISTINCT userid FROM fulldata")
    return [row[0] for row in b18]
def fonk5(b20):
    b7 = {}
    with open(b20) as f:
        next(f)
        for line in f:
            b8 = line.strip().split(",")
            b9 = int(b8[0])
            b10 = b8[1]
            b11 = b8[2]
            b12 = b8[3]
            if b9 not in b7:
                b7[b9] = []
            b7[b9].append([b10, b11, b12])
    return b7
def fonk6(b19, b7):
    b13 = len(b19)
    b14 = np.ones((b13, b13))
    for j in range(b13 - 1):
        print(f'Processing user {j + 1}/{b13 - 1}')
        b15 = b7[b19[j]]
        for i in range(j + 1, b13):
            b16 = b7[b19[i]]
            b14[j, i] = fonk3(b15, b16)
    return b14
def fonk7():
    b17 = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='thesis')
    b18 = b17.b18(buffered=True)
    b19 = fonk4(b18)
    b20 = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
    b7 = fonk5(b20)
    b14 = fonk6(b19, b7)
    np.save('b14.npy', b14)
    b17.close()
if b21 = = "__main__":
    fonk7()