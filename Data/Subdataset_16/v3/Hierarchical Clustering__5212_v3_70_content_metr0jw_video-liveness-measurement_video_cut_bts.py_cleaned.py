import pandas as pd
def fonk1(file_path):
    return pd.read_csv(file_path).values.flatten().tolist()
def fonk2(b9, b1 = 4):
    b2 = []
    b3 = []
    a1 = 0
    b4 = len(b9)
    while a1 < b4:
        a2 = 0
        a3 = 0
        if b9[a1] in [0.5, 1]:
            b5 = a1
            while a1 < b4 and b9[a1] in [0.5, 1]:
                if b9[a1] == 1:
                    a3 += 1
                a2 += 1
                a1 += 1
            b6 = a1
            if a2 >= b1 and a3 > 0:
                b2.append(b5)
                b3.append(b6)
        else:
            a1 += 1
    return b2, b3
def fonk3(b2, b3, output_file):
    b7 = pd.DataFrame({
        "Start Time": b2,
        "End Time": b3
    })
    b7.to_csv(output_file, b8 = False)
def fonk4():
    b9 = fonk1("y_prediction_bts.csv")
    b2, b3 = fonk2(b9)
    fonk3(b2, b3, "timedata_bts.csv")
if b10 = = "__main__":
    fonk4()