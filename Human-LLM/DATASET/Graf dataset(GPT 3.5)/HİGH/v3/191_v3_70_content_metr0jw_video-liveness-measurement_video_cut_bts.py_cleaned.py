import pandas as pd
b1 = pd.read_csv("y_prediction_bts.csv").values.flatten()
b2 = []
b3 = []
a1 = 0
while a1 < len(b1) - 1:
    a2 = 0
    a3 = 0
    if b1[a1] in (0.5, 1):
        b4 = a1
        while b1[a1] in (0.5, 1):
            a1 += 1
            a2 += 1
            if b1[a1] == 1:
                a3 += 1
        b5 = a1
        if a2 > 3 and a3 > 0:
            b2.append(b4)
            b3.append(b5)
    a1 += 1
b6 = pd.DataFrame(b2, columns=["Start Time"])
b7 = pd.DataFrame(b3, columns=["End Time"])
b8 = pd.concat([b6, b7], axis=1)
b8.to_csv("timedata_bts.csv", b9 = 'w', index=False)