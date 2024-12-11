import numpy as np
import math
import matplotlib.pyplot as plt
import csv
def fonk1(b30):
    b1 = np.b1(np.array(b30))
    print("Mean Distance: ", np.mean(np.array(b30)))
    print("Minimum Distance: ", np.min(np.array(b30)))
    print("Maximum Distance: ", np.max(np.array(b30)))
    print("Standard Deviation of Distances: ", b1)
    return b1
def fonk2(point, line_2pt):
    b21, b22, b23, b2 = line_2pt[0], line_2pt[1], line_2pt[2], line_2pt[3]
    b3 = b23 - b21
    b4 = b2 - b22
    b5 = point[0] - b21
    b6 = point[1] - b22
    b7 = (b5 * b3 + b6 * b4) / (b3 * b3 + b4 * b4)
    b8 = [b21 + b7 * b3, b22 + b7 * b4]
    return b8
def fonk3(L1, b10):
    a1 = 1.0
    a2 = 1.0
    a3 = 1.0
    a4 = 1.0
    b9 = abs((fonk4(L1) / L1[0][2]) - (fonk4(b10) / b10[0][2]))
    if fonk4(L1) > fonk4(b10):
        L1, b10 = b10, L1
    b11 = [b10[0][0], b10[0][1]]
    b12 = fonk2(b11, [L1[0][0], L1[0][1], L1[1][0], L1[1][1]])
    b13 = [L1[0][0], L1[0][1]]
    b14 = fonk2(b13, [b10[0][0], b10[0][1], b10[1][0], b10[1][1]])
    b15 = np.linalg.norm([b10[0][1] - b12[1], b10[0][0] - b12[0]])
    b16 = np.linalg.norm([L1[0][1] - b14[1], L1[0][0] - b14[0]])
    b17 = (b15**2 + b16**2) / (b15 + b16)
    b18 = min(np.linalg.norm([L1[0][1] - b12[1], L1[0][0] - b12[0]]),
                    np.linalg.norm([L1[1][1] - b12[1], L1[1][0] - b12[0]]))
    b19 = min(np.linalg.norm([b10[0][1] - b14[1], b10[0][0] - b14[0]]),
                    np.linalg.norm([b10[1][1] - b14[1], b10[1][0] - b14[0]]))
    b20 = min(b18, b19)
    b21 = b10[1][0] - b10[0][0]
    b22 = b10[1][1] - b10[0][1]
    b23 = L1[1][0] - L1[0][0]
    b2 = L1[1][1] - L1[0][1]
    b24 = b21 * b23 + b22 * b2
    b25 = b24 / (np.linalg.norm([b21, b22]) * np.linalg.norm([b23, b2]))
    b26 = math.acos(b25)
    if b26 < (math.pi / 2):
        b27 = math.sin(b26) * fonk4(b10)
    else:
        b27 = fonk4(b10)
    return (a1 * b17 +
            a2 * b20 +
            a3 * b27 +
            a4 * b9)
def fonk4(b29):
    b21, b22, b23, b2 = b29[0][0], b29[0][1], b29[1][0], b29[1][1]
    return np.linalg.norm([b23 - b21, b2 - b22])
def fonk5(T):
    b28 = []
    for b42 in T:
        for i in range(len(T[b42]) - 1):
            b29 = [T[b42][i], T[b42][i + 1]]
            b28.append([b29, b42, 0])
    return b28
def fonk6(T, b28, distance_threshold, percentage_threshold):
    a5 = 0
    a8, b1 = fonk8(T, b28, distance_threshold)
    for partition in b28:
        b30 = []
        a6 = 0
        for b42 in T:
            if b42 != partition[1]:
                a7 = 0
                for i in range(len(T[b42]) - 1):
                    b29 = [T[b42][i], T[b42][i + 1]]
                    b31 = fonk3(partition[0], b29)
                    b30.append(b31)
                    if b31 < distance_threshold:
                        a7 = a7 + fonk4(b29)
                if a7 > fonk4(partition[0]):
                    a6 = a6 + 1
        b32 = (len([d for d in b30 if d <= b1]) + 1) * len(b28)
        if (a6 * a8) / b32 < percentage_threshold * len(T):
            partition[2] = 1
            a5 += 1
    return b28, a5
def fonk7(T, b28, outlier_fraction):
    b33 = []
    for b42 in T:
        b34 = [partition[0] for partition in b28 if partition[2] == 1 and partition[1] == b42]
        b36, b35 = 0, 0
        for b29 in b34:
            b36 = b36 + fonk4(b29)
        for i in range(len(T[b42]) - 1):
            b29 = [T[b42][i], T[b42][i + 1]]
            b35 = b35 + fonk4(b29)
        if b36 / b35 > outlier_fraction:
            b33.append(b42)
    return b33
def fonk8(T, b28, distance_threshold):
    b30 = []
    for partition in b28:
        for b42 in T:
            if b42 != partition[1]:
                for i in range(len(T[b42]) - 1):
                    b29 = [T[b42][i], T[b42][i + 1]]
                    b31 = fonk3(partition[0], b29)
                    b30.append(b31)
    b1 = fonk1(b30)
    a8 = 0
    for partition in b28:
        b30 = []
        for b42 in T:
            if b42 != partition[1]:
                for i in range(len(T[b42]) - 1):
                    b29 = [T[b42][i], T[b42][i + 1]]
                    b31 = fonk3(partition[0], b29)
                    b30.append(b31)
                a8 = a8 + (len([d for d in b30 if d <= b1]) + 1)
    return a8, b1
def fonk9(T, distance_threshold, percentage_threshold, outlier_fraction):
    print("Partition Phase Begins ...")
    b28 = fonk5(T)
    print("Partition Done !")
    print("Total Number of Trajectory Partitions: ", len(b28))
    print("Outlying Trajectory Partition Detection Phase Begins ...")
    b28, a5 = fonk6(T, b28, distance_threshold, percentage_threshold)
    print("Outlying Trajectory Partition Detection Done !")
    print("Number of Outlying Trajectory Partitions: ", a5, " of ", len(b28))
    print("Outlying Trajectory Detection Phase Begins ...")
    b33 = fonk7(T, b28, outlier_fraction)
    print("Outlying Trajectory Detection Phase Done !")
    print("Number of Outlying Trajectories: ", len(b33), " of ", len(T))
    return b33
def fonk10(time_str):
    return ((int(time_str[0:2]) * 3600) + (int(time_str[3:5]) * 60) + (int(time_str[6:8]))) / 86400.0
def fonk11(b45, N):
    b37 = {}
    with open(b45, b38 = '') as csvfile:
        b39 = csv.b39(csvfile, delimiter=' ', quotechar='|')
        t1, m1, b21, b22, b40 = -1, '', -1, -1, -1
        a9 = 0
        for row in b39:
            b41 = ', '.join(row).split(";")
            time, m, x, y, b42 = fonk10((b41[0].split('T')[1])[:-4]), b41[1], int(int(b41[2]) / 67), int(int(b41[3]) / 67), int(b41[4])
            if b40 = = b42 and t1 != time:
                if b37[a9][len(b37[a9]) - 1][0] != x or b37[a9][len(b37[a9]) - 1][1] != y:
                    b37[a9].append([x, y, time])
            if b40 != b42:
                a9 += 1
                if a9 > N:
                    break
                b37[a9] = [[x, y, time]]
            t1, m1, b40, b21, b22 = time, m, b42, x, y
    return b37
def fonk12(trajectory_points, trajectory_id):
    x, y, b43 = [], [], []
    for point in trajectory_points:
        x.append(point[0])
        y.append(point[1])
    b44 = plt.figure()
    plt.plot(x, y)
    b44.suptitle('TRAJECTORY ID: ' + str(trajectory_id))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    b44.savefig('Results/' + str(trajectory_id) + '.png')
b45 = 'data/csv/al_position2013-02-06.csv'
b37 = fonk11(b45, 10)
b33 = fonk9(b37, 37, 0.01, 0.4)
print("Outliers: ", b33)
for trajectory_id in b37:
    fonk12(b37[trajectory_id], trajectory_id)