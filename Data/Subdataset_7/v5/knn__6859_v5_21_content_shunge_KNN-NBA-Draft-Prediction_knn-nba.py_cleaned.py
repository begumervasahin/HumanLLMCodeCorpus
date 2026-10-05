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
def fonk3(a1, a2):
    b2 = []
    b3 = []
    for i in range(a1, a2 + 1):
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
    return b2, b3
def fonk4(b8, b2, b3):
    with open(b8 + ".txt", "r") as file:
        for line in file.readlines()[2:60]:
            print([line.split(",")[3]])
            b5 = line.split(",")
            b6 = [
                fonk1(b5[18]),
                fonk1(b5[20]) * 20,
                fonk1(b5[21])
            ]
            b7 = KNeighborsClassifier(n_neighbors=50)
            b7.fit(b2, np.array(b3))
            print(b7.predict([np.array(b6)]))
def fonk5():
    a1 = 1999
    a2 = 2016
    b2, b3 = fonk3(a1, a2)
    b8 = "2003"
    fonk4(b8, b2, b3)
if b9 = = '__main__':
    fonk5()