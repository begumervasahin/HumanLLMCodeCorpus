import numpy as np
from sklearn.neighbors import KNeighborsClassifier
def fonk1(num):
    try:
        return float(num)
    except ValueError:
        return 0
def fonk2(num):
    b1 = ["Top 10 picks", "Mid 1st round", "Late 1st round",
                  "Early 2nd round", "Mid 2nd round", "Late 2nd round/undrafted"]
    return b1[(num - 1)
def fonk3(b6):
    b2 = [
        fonk1(b6[18]),
        fonk1(b6[20]) * 20,
        fonk1(b6[21])
    ]
    return np.array(b2)
b3 = []
b4 = []
for year in range(1999, 2017):
    b5 = f"{year}.txt"
    with open(b5, "r") as file:
        for line in file.readlines()[2:]:
            b6 = line.split(",")
            if b6[11] == "":
                continue
            b3.append(fonk3(b6))
            b4.append(fonk2(int(b6[1])))
a1 = 2003
b5 = f"{a1}.txt"
with open(b5, "r") as file:
    for line in file.readlines()[2:60]:
        b6 = line.split(",")
        b7 = b6[3]
        b8 = fonk3(b6)
        b9 = KNeighborsClassifier(n_neighbors=50)
        b9.fit(b3, np.array(b4))
        b10 = b9.predict([b8])
        print(f"Player: {b7}, Prediction: {b10[0]}")