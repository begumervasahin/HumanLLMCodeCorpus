import numpy as np
with open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv') as f:
    k = 0
    traj1 = []
    traj2 = []
    userid = 0
    lst_users = []
    for line in f:
        if k == 0:
            k += 1
        else:
            m = line.split(",")
            if userid == int(m[0]):
                tuple_data = [m[1], str(m[2]), m[3]]
                traj2.append(tuple_data)
            else:
                userid = int(m[0])
                if traj2:
                    traj1.append(traj2)
                traj2 = []
                lst_users.append(m[0])
                tuple_data = [m[1], str(m[2]), m[3]]
                traj2.append(tuple_data)
    traj1.append(traj2)
print("Loading done")
distance = np.zeros((8357, 8357))
with open('distance_matrix_final.csv') as f1:
    i = 0
    for line in f1:
        data = line.split(",")
        if lst_users[i] != data[0]:
            print('Error:', i)
        j = 0
        k = 1
        while k < len(data):
            if float(data[k]) == 0:
                if i != k - 1:
                    print("Error at", i, k - 1)
            distance[i][j] = float(data[k])
            j += 1
            k += 1
        i += 1
for i in range(8357):
    for j in range(8357):
        if distance[i][j] != distance[j][i]:
            print("Error at", i, j)