import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
def standard_deviation(distances):
    distances_array = np.array(distances)
    std = np.std(distances_array)
    print("Mean Distance: ", np.mean(distances_array))
    print("Minimum Distance: ", np.min(distances_array))
    print("Maximum Distance: ", np.max(distances_array))
    print("Standard Deviation of Distances: ", std)
    return std
def proj_point_on_line(point, line_2pt):
    line = [1, 1, 1, 1]
    line[0], line[1], line[2], line[3] = line_2pt[0], line_2pt[1], line_2pt[2] - line_2pt[0], line_2pt[3] - line_2pt[1]
    vx, vy = line[2], line[3]
    dx, dy = point[0] - line[0], point[1] - line[1]
    tp = (dx * vx + dy * vy) / (vx * vx + vy * vy)
    point[0], point[1] = line[0] + tp * vx, line[1] + tp * vy
    return [point[0], point[1]]
def tp_distance(L1, L2):
    w1, w2, w3, w4 = 1.0, 1.0, 1.0, 1.0
    Dspeed = abs((length(L1) / L1[0][2]) - (length(L2) / L2[0][2]))
    if length(L1) > length(L2):
        L1, L2 = deepcopy(L2), deepcopy(L1)
    point1 = [L2[0][0], L2[0][1]]
    line_2pt1 = [L1[0][0], L1[0][1], L1[1][0], L1[1][1]]
    proj1 = proj_point_on_line(point1, line_2pt1)
    point2 = [L1[0][0], L1[0][1]]
    line_2pt2 = [L2[0][0], L2[0][1], L2[1][0], L2[1][1]]
    proj2 = proj_point_on_line(point2, line_2pt2)
    six, siy, eix, eiy = L1[0][0], L1[0][1], L1[1][0], L1[1][1]
    sjx, sjy, ejx, ejy = L2[0][0], L2[0][1], L2[1][0], L2[1][1]
    lper1 = np.linalg.norm([sjy - proj1[1], sjx - proj1[0]])
    lper2 = np.linalg.norm([siy - proj2[1], six - proj2[0]])
    Dper = (math.pow(lper1, 2) + math.pow(lper2, 2)) / (lper1 + lper2)
    lpar1 = min(np.linalg.norm([siy - proj1[1], six - proj1[0]]), np.linalg.norm([eiy - proj1[1], eix - proj1[0]]))
    lpar2 = min(np.linalg.norm([siy - proj2[1], six - proj2[0]]), np.linalg.norm([eiy - proj2[1], eix - proj1[0]]))
    Dpar = min(lpar1, lpar2)
    x1, y1, x2, y2 = ejx - sjx, ejy - sjy, eix - six, eiy - siy
    inner_product = x1 * x2 + y1 * y2
    costheta = inner_product / (np.linalg.norm([x1, y1]) * np.linalg.norm([x2, y2]))
    costheta = min(1, max(-1, costheta))
    angle = math.acos(costheta)
    Dang = math.sin(angle) * length(L2) if angle < (math.pi / 2) else length(L2)
    return w1 * Dper + w2 * Dpar + w3 * Dang + w4 * Dspeed
def length(segment):
    sx, sy, ex, ey = segment[0][0], segment[0][1], segment[1][0], segment[1][1]
    return np.linalg.norm([ex - sx, ey - sy])
def mdl_par(t, s, e):
    pfactor = 2
    ld = length([t[s], t[e]])
    x1, y1, x2, y2 = t[s][0], t[s][1], t[e][0], t[e][1]
    Dx, Dy = x2 - x1, y2 - y1
    D = np.linalg.norm([Dx, Dy])
    d = sum(math.fabs((Dy * t[i][0] - Dx * t[i][1] + x2 * y1 - y2 * x1) / D) for i in range(s, e))
    ldh = d / pfactor
    return ld + ldh
def mdl_nopar(t, s, e):
    return sum(length([t[i], t[i + 1]]) for i in range(s, e))
def mdl_partition(t):
    cp = [t[0]]
    si, l = 1, 1
    while si + l <= len(t):
        ci = si + l
        cost_par = mdl_par(t, si, ci)
        cost_nopar = mdl_nopar(t, si, ci)
        if cost_par > cost_nopar:
            cp.append(t[ci - 1])
            si, l = ci - 1, 1
        else:
            l += 1
    cp.append(t[-1])
    return cp
def partition(T):
    L = []
    for p in T:
        for i in range(len(T[p]) - 1):
            segment = [T[p][i], T[p][i + 1]]
            L.append([segment, p, 0])
    return L
def total_density(T, L, D):
    distances = []
    for Li in L:
        for p in T:
            if p != Li[1]:
                for i in range(len(T[p]) - 1):
                    segment = [T[p][i], T[p][i + 1]]
                    dist = tp_distance(Li[0], segment)
                    if not math.isnan(dist):
                        distances.append(dist)
    sd = standard_deviation(distances)
    tdensity = 0
    for Li in L:
        distances = []
        for p in T:
            if p != Li[1]:
                for i in range(len(T[p]) - 1):
                    segment = [T[p][i], T[p][i + 1]]
                    dist = tp_distance(Li[0], segment)
                    distances.append(dist)
                tdensity += (len([d for d in distances if d <= sd]) + 1)
    return tdensity, sd
def detect(T, L, D, P):
    outlier_count = 0
    totaldensity, sd = total_density(T, L, D)
    for Li in L:
        distances = []
        CTR_count = 0
        for p in T:
            if p != Li[1]:
                matchLen = 0
                for i in range(len(T[p]) - 1):
                    segment = [T[p][i], T[p][i + 1]]
                    dist = tp_distance(Li[0], segment)
                    distances.append(dist)
                    if dist < D:
                        matchLen += length(segment)
                if matchLen > length(Li[0]):
                    CTR_count += 1
        density = (len([d for d in distances if d <= sd]) + 1) * len(L)
        if (CTR_count * totaldensity) / density < P * len(T):
            Li[2] = 1
            outlier_count += 1
    return L, outlier_count
def mark(T, L, F):
    otraj = []
    for p in T:
        outliers = [Li[0] for Li in L if (Li[2] == 1 and Li[1] == p)]
        olen = sum(length(seg) for seg in outliers)
        tlen = sum(length([T[p][i], T[p][i + 1]]) for i in range(len(T[p]) - 1))
        if olen / tlen > F:
            otraj.append(p)
    return otraj
def traod(T, D, P, F):
    print("Partition Phase Begins ...")
    L = partition(T)
    print("Partition Done!")
    print("Total Number of t-partitions: ", len(L))
    print("Outlying t-partition Detection Phase Begins ...")
    L, outlier_count = detect(T, L, D, P)
    print("Outlying t-partition Detection Done!")
    print("Number of Outlying t-partitions: ", outlier_count, " of ", len(L))
    print("Outlying Trajectory Detection Phase Begins ...")
    otraj = mark(T, L, F)
    print("Outlying Trajectory Detection Phase Done!")
    print("Number of Outlying Trajectories: ", len(otraj), " of ", len(T))
    return otraj
def get_time(tr):
    return ((int(tr[0:2]) * 3600) + (int(tr[3:5]) * 60) + (int(tr[6:8]))) / 86400.0
def trajectory(filename, N):
    trajectory = {}
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=' ', quotechar='|')
        P, t1, m1, x1, y1, p1 = 0, -1, '', -1, -1, -1
        for row in data:
            r = ', '.join(row).split(";")
            t2, m2, x2, y2, p2 = get_time((r[0].split('T')[1])[:-4]), r[1], int(int(r[2]) / 67), int(int(r[3]) / 67), int(r[4])
            if p1 == p2 and t1 != t2:
                if trajectory[P][len(trajectory[P]) - 1][0] != x2 or trajectory[P][len(trajectory[P]) - 1][1] != y2:
                    trajectory[P].append([x2, y2, t2])
            if p1 != p2:
                P += 1
                if not P <= N:
                    break
                trajectory[P] = [[x2, y2, t2]]
            t1, m1, p1, x1, y1 = t2, m2, p2, x2, y2
    return trajectory
def plot_trajectory(traj, p):
    x, y = zip(*[(point[0], point[1]) for point in traj])
    fig = plt.figure()
    plt.plot(x, y)
    fig.suptitle('TRAJECTORY ID: ' + str(p))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    fig.savefig('Results/' + str(p) + '.png')
filename = 'data/csv/al_position2013-02-06.csv'
T = trajectory(filename, 10)
O = traod(T, 37, 0.01, 0.4)
print("Outliers: ", O)
for p in T:
    plot_trajectory(T[p], p)