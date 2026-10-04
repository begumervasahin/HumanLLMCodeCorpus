import numpy as np
with open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv') as f:
    traj1 = []
    traj2 = []
    lst_users = []
    userid = None
    next(f)
    for line in f:
        m = line.split(",")
        if userid == int(m[0]):
            traj2.append([m[1], str(m[2]), m[3]])
        else:
            userid = int(m[0])
            if traj2:
                traj1.append(traj2)
            traj2 = [[m[1], str(m[2]), m[3]]]
            lst_users.append(m[0])
    if traj2:
        traj1.append(traj2)
print("Loading done")
distance_matrix_path = 'distance_matrix_final.csv'
distance = np.zeros((8357, 8357))
with open(distance_matrix_path) as f1:
    for i, line in enumerate(f1):
        a = line.split(",")
        if lst_users[i] != a[0]:
            print('Error at user ID index', i)
        for j, value in enumerate(a[1:], start=0):
            distance[i][j] = float(value)
            if distance[i][j] == 0 and i != j:
                print(f"Error at distance {i}, {j}")
for i in range(8357):
    for j in range(8357):
        if distance[i][j] != distance[j][i]:
            print(f"Symmetry error at {i}, {j}")