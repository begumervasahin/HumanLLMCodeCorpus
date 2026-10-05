import pandas as pd
b1 = pd.read_csv("y_prediction_itzy.csv").values
b2 = list(b1)
b3 = []
b4 = []
a1 = 0
while a1 < len(b2) - 1:
    a2 = 0
    a3 = 0
    if b2[a1] == 0.5 or b2[a1] == 1:
        b5 = a1
        while b2[a1] == 0.5 or b2[a1] == 1:
            a1 += 1
            a2 += 1
            if b2[a1] == 1:
                a3 += 1
        b6 = a1
        if a2 > 3 and a3 > 0:
            b3.append(b5)
            b4.append(b6)
    a1 += 1
b7 = pd.DataFrame(b3, columns=["Start Time"])
b8 = pd.DataFrame(b4, columns=["End Time"])
b9 = pd.concat([b7, b8], axis=1)
b9.to_csv("timedata_itzy.csv", b10 = 'w', index=False)