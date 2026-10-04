import pandas as pd
def fonk1(file_path):
    return pd.read_csv(file_path).values.flatten().tolist()
def fonk2(pred_data, b1 = 4):
    b2 = []
    b3 = []
    a1 = 0
    b4 = len(pred_data)
    while a1 < b4:
        if pred_data[a1] in [0.5, 1]:
            b5 = a1
            a2 = 0
            a3 = 0
            while a1 < b4 and pred_data[a1] in [0.5, 1]:
                if pred_data[a1] == 1:
                    a3 += 1
                a2 += 1
                a1 += 1
            if a2 >= b1 and a3 > 0:
                b2.append(b5)
                b3.append(a1)
        a1 += 1
    return b2, b3
def fonk3(b2, b3, output_file):
    b6 = pd.DataFrame({
        "Start Time": b2,
        "End Time": b3
    })
    b6.to_csv(output_file, b7 = False)
def fonk4():
    b8 = fonk1("y_prediction_itzy.csv")
    b2, b3 = fonk2(b8)
    fonk3(b2, b3, "timedata_itzy.csv")
if b9 = = "__main__":
    fonk4()