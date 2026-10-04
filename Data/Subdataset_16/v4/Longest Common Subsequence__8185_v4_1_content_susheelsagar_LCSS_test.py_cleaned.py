import numpy as np
with open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv') as f:
    b1 = []
    b2 = []
    b3 = []
    b4 = None
    next(f)
    for line in f:
        b5 = line.split(",")
        if b4 = = int(b5[0]):
            b2.append([b5[1], str(b5[2]), b5[3]])
        else:
            b4 = int(b5[0])
            if b2:
                b1.append(b2)
            b2 = [[b5[1], str(b5[2]), b5[3]]]
            b3.append(b5[0])
    if b2:
        b1.append(b2)
print("Loading done")
b6 = 'distance_matrix_final.csv'
b7 = np.zeros((8357, 8357))
with open(b6) as f1:
    for i, line in enumerate(f1):
        b8 = line.split(",")
        if b3[i] != b8[0]:
            print('Error at user ID index', i)
        for j, value in enumerate(b8[1:], b9 = 0):
            b7[i][j] = float(value)
            if b7[i][j] == 0 and i != j:
                print(f"Error at b7 {i}, {j}")
for i in range(8357):
    for j in range(8357):
        if b7[i][j] != b7[j][i]:
            print(f"Symmetry error at {i}, {j}")