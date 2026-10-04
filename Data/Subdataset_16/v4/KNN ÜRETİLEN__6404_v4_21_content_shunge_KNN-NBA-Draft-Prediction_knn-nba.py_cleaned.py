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
    return b1[(num - 1)
b2 = []
b3 = []
for year in range(1999, 2017):
    b4 = f"{year}.txt"
    with open(b4, "r") as file:
        for line in file.readlines()[2:]:
            b5 = line.split(",")
            if b5[11] == "":
                continue
            b6 = []
            b6.append(fonk1(b5[18]))
            b6.append(fonk1(b5[20]) * 20)
            b6.append(fonk1(b5[21]))
            b2.append(np.array(b6))
            b3.append(fonk2(int(b5[1])))
a1 = 2003
b4 = f"{a1}.txt"
with open(b4, "r") as file:
    for line in file.readlines()[2:60]:
        print(line.split(",")[3])
        b5 = line.split(",")
        b6 = []
        b6.append(fonk1(b5[18]))
        b6.append(fonk1(b5[20]) * 20)
        b6.append(fonk1(b5[21]))
        b7 = KNeighborsClassifier(n_neighbors=50)
        b7.fit(b2, np.array(b3))
        b8 = b7.predict([np.array(b6)])
        print(b8)