from sklearn.neighbors import KNeighborsClassifier
import numpy as np
def fonk1(num):
    try:
        return float(num)
    except ValueError:
        return 0
def fonk2(num):
    b1 = ["Top 10 picks", "Mid 1st round", "Late 1st round",
                  "Early 2nd round", "Mid 2nd round", "Late 2nd round/undrafted"]
    return b1[(num-1)
b2 = []
b3 = []
for i in range(1999, 2017):
    b4 = str(i) + ".txt"
    with open(b4, "r") as file:
        for line in file.readlines()[2:]:
            if line.split(",")[11] == "":
                continue
            b5 = line.split(",")
            b6 = [
                fonk1(b5[18]),
                fonk1(b5[20]) * 20,
                fonk1(b5[21])
            ]
            b2.append(np.array(b6))
            b3.append(fonk2(int(b5[1])))
b7 = "2003"
b8 = []
with open(b7 + ".txt", "r") as file:
    for line in file.readlines()[2:60]:
        b5 = line.split(",")
        b6 = [
            fonk1(b5[18]),
            fonk1(b5[20]) * 20,
            fonk1(b5[21])
        ]
        b8.append(np.array(b6))
b9 = KNeighborsClassifier(n_neighbors=50)
b9.fit(b2, np.array(b3))
for b6 in b8:
    print(b9.predict([b6]))