import pandas as pd
b1 = pd.read_csv("y_prediction_itzy.csv").values
b2 = list(b1)
b3 = list()
b4 = list()
a1 = 0
b5 = b2.__len__() - 1
while a1 != b5:
    a2 = 0
    a3 = 0
    if b2[a1] == 0.5 or b2[a1] == 1:
        b6 = a1
        while b2[a1] == 0.5 or b2[a1] == 1:
            a1 += 1
            a2 += 1
            if b2[a1] == 1:
                a3 += 1
            print("TEST")
        b7 = a1
    if a2 > 3 and a3 > 0:
        print("SUCCESS")
        b3.append(b6)
        b4.append(b7)
    a1 += 1
b3 = pd.DataFrame(b3, columns=["Start Time"])
b4 = pd.DataFrame(b4, columns=["End Time"])
b8 = pd.concat([b3, b4], axis=1)
b8.to_csv("timedata_itzy.csv", b9 = 'w', index=False)