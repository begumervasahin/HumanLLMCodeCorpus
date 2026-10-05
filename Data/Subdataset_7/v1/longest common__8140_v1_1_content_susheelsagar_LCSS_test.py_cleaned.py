import numpy as np
with open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv') as f:
    a1 = 0
    b1 = []
    b2 = []
    a2 = 0
    b3 = []
    for line in f:
        if a1 = = 0:
            a1 += 1
        else:
            b4 = line.split(",")
            if a2 = = int(b4[0]):
                b5 = [b4[1], str(b4[2]), b4[3]]
                b2.append(b5)
            else:
                a2 = int(b4[0])
                if b2:
                    b1.append(b2)
                b2 = []
                b3.append(b4[0])
                b5 = [b4[1], str(b4[2]), b4[3]]
                b2.append(b5)
    b1.append(b2)
print("Loading done")
b6 = np.zeros((8357, 8357))
with open('distance_matrix_final.csv') as f1:
    a3 = 0
    for line in f1:
        b7 = line.split(",")
        if b3[a3] != b7[0]:
            print('Error:', a3)
        a4 = 0
        a1 = 1
        while a1 < len(b7):
            if float(b7[a1]) == 0:
                if a3 != a1 - 1:
                    print("Error at", a3, a1 - 1)
            b6[a3][a4] = float(b7[a1])
            a4 += 1
            a1 += 1
        a3 += 1
for a3 in range(8357):
    for a4 in range(8357):
        if b6[a3][a4] != b6[a4][a3]:
            print("Error at", a3, a4)