from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
import numpy as np
def fonk1(num):
    try:
        return float(num)
    except ValueError:
        return 0
def fonk2(num):
    b1 = ["Top 10 picks", "Mid 1st round", "Late 1st round",
                   "Early 2nd round", "Mid 2nd round", "Late 2nd round/undrafted"]
    return b1[(num-1)/10]
b2 = []
b3 = []
for i in range(1999, 2017):
    b4 = str(i) + ".txt"
    b5 = open(b4, "r")
    for line in b5.readlines()[2:]:
        if line.split(",")[11] == "":
            continue
        b6 = line.split(",")
        b7 = []
        b7 += [fonk1(b6[18])]
        b7 += [fonk1(b6[20]) * 20]
        b7 += [fonk1(b6[21])]
        b2.append(np.array(b7))
        b3.append(fonk2(int(b6[1])))
b8 = str(2003)
b5 = open(b8+".txt","r")
for line in b5.readlines()[2:60]:
        print [line.split(",")[3]]
        b6 = line.split(",")
        b7 = []
        b7 += [fonk1(b6[18])]
        b7 += [fonk1(b6[20]) * 20]
        b7 += [fonk1(b6[21])]
        b9 = KNeighborsClassifier(n_neighbors=50)
        b9.fit(b2, np.array(b3))
        print b9.predict([np.array(b7)])