import pandas as pd
from naive_bayes import loocv, et
def fonk1(file_path, b10, b11):
    b1 = pd.read_csv(file_path, header=None)
    b2 = b1.iloc[:, b10].values.tolist()
    b3 = b1.iloc[:, b11].values.tolist()
    return b2, b3
def fonk2(x_train, x_test, b12, b13):
    b4 = set(b12)
    b5 = et(x_train, x_test, b12, b13, b4)
    return b5
def fonk3(x, b3):
    b4 = set(b3)
    b5 = loocv(x, b3, b4)
    return b5
def fonk4():
    b6 = [
        {"name": "Tic-tac-toe Endgame", "train": "tic-tac-toe.b1", "test": None, "x_cols": range(0, 9), "y_col": 9},
        {"name": "SPECT heart Dataset", "train": "SPECT.train", "test": "SPECT.test", "x_cols": range(1, 23), "y_col": 0},
        {"name": "Soybean (small)", "train": "soybean-small.b1", "test": None, "x_cols": range(0, 35), "y_col": 35},
        {"name": "Shuttle landing control", "train": "shuttle-landing-control.b1", "test": None, "x_cols": range(0, 9), "y_col": 9},
        {"name": "Monks-1", "train": "monks-1.train", "test": "monks-1.test", "x_cols": range(2, 8), "y_col": 1},
        {"name": "Monks-2", "train": "monks-2.train", "test": "monks-2.test", "x_cols": range(2, 8), "y_col": 1},
        {"name": "Monks-3", "train": "monks-3.train", "test": "monks-3.test", "x_cols": range(2, 8), "y_col": 1}
    ]
    b7 = []
    for dataset in b6:
        b8 = dataset["train"]
        b9 = dataset["test"]
        b10 = dataset["x_cols"]
        b11 = dataset["y_col"]
        x_train, b12 = fonk1(b8, b10, b11)
        x_test, b13 = fonk1(b9, b10, b11) if b9 else (None, None)
        if b9:
            b5 = fonk2(x_train, x_test, b12, b13)
        else:
            b5 = fonk3(x_train, b12)
        b7.append({"Dataset": dataset["name"], "Accuracy(%)": b5})
    b14 = pd.DataFrame(b7)
    b14.to_csv("Data.csv", b15 = False)
if b16 = = "__main__":
    fonk4()