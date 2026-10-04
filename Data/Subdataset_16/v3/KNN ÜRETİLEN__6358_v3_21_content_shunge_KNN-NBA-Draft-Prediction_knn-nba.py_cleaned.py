import numpy as np
from sklearn.neighbors import KNeighborsClassifier
def fonk1(num):
    try:
        return float(num)
    except ValueError:
        return 0
def fonk2(num):
    b1 = [
        "Top 10 picks", "Mid 1st round", "Late 1st round",
        "Early 2nd round", "Mid 2nd round", "Late 2nd round/undrafted"
    ]
    return b1[(num - 1)
def fonk3(b8):
    b2 = []
    b3 = []
    with open(b8, "r") as file:
        for line in file.readlines()[2:]:
            if line.split(",")[11] == "":
                continue
            b4 = line.split(",")
            b5 = [
                fonk1(b4[18]),
                fonk1(b4[20]) * 20,
                fonk1(b4[21])
            ]
            b2.append(np.array(b5))
            b3.append(fonk2(int(b4[1])))
    return b2, b3
b6 = []
b7 = []
for year in range(1999, 2017):
    b8 = f"{year}.txt"
    yearly_stats, b9 = fonk3(b8)
    b6.extend(yearly_stats)
    b7.extend(b9)
b10 = KNeighborsClassifier(n_neighbors=50)
b10.fit(b6, np.array(b7))
def fonk4(year):
    b8 = f"{year}.txt"
    with open(b8, "r") as file:
        for line in file.readlines()[2:60]:
            b11 = line.split(",")[3]
            print(b11)
            b4 = line.split(",")
            b5 = [
                fonk1(b4[18]),
                fonk1(b4[20]) * 20,
                fonk1(b4[21])
            ]
            b12 = b10.predict([np.array(b5)])
            print(b12[0])
fonk4(2003)
b13 = [fonk1('22.5'), fonk1('8.2') * 20, fonk1('1.5')]
b12 = b10.predict([np.array(b13)])
print("Prediction for new b2:", b12[0])