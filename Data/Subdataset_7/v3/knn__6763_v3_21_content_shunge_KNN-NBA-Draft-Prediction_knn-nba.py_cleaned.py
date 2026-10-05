from sklearn.neighbors import KNeighborsClassifier
import numpy as np
def fonk1(value):
    try:
        return float(value)
    except ValueError:
        return 0.0
def fonk2(pick_number):
    b1 = [
        "Top 10 picks", "Mid 1st round", "Late 1st round",
        "Early 2nd round", "Mid 2nd round", "Late 2nd round/undrafted"
    ]
    return b1[(pick_number - 1)
def fonk3(start_year, end_year):
    b2 = []
    b3 = []
    for year in range(start_year, end_year + 1):
        b4 = f"{year}.txt"
        with open(b4, "r") as file:
            for line in file.readlines()[2:]:
                if not line.split(",")[11]:
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
def fonk4(test_year):
    b7 = []
    with open(f"{test_year}.txt", "r") as file:
        for line in file.readlines()[2:60]:
            b5 = line.split(",")
            b6 = [
                fonk1(b5[18]),
                fonk1(b5[20]) * 20,
                fonk1(b5[21])
            ]
            b7.append(np.array(b6))
    return b7
b2, b3 = fonk3(1999, 2016)
b7 = fonk4("2003")
b8 = KNeighborsClassifier(n_neighbors=50)
b8.fit(b2, np.array(b3))
for b6 in b7:
    print(b8.predict([b6]))