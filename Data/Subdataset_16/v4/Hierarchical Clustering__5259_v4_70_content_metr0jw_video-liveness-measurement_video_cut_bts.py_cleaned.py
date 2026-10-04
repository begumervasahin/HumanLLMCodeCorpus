import pandas as pd
b1 = pd.read_csv("y_prediction_bts.csv").values.flatten()
b2 = list(b1)
b3 = []
b4 = []
a1 = 0
b5 = len(b2)
while a1 < b5 - 1:
    a2 = 0
    a3 = 0
    if b2[a1] in [0.5, 1]:
        b6 = a1
        while a1 < b5 and b2[a1] in [0.5, 1]:
            a2 += 1
            if b2[a1] == 1:
                a3 += 1
            a1 += 1
            print("TEST")
        b7 = a1
        if a2 > 3 and a3 > 0:
            print("SUCCESS")
            b3.append(b6)
            b4.append(b7)
    a1 += 1
b8 = pd.DataFrame(b3, columns=["Start Time"])
b9 = pd.DataFrame(b4, columns=["End Time"])
b10 = pd.concat([b8, b9], axis=1)
b10.to_csv("timedata_bts.csv", b11 = False)