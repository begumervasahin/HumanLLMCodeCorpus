import pandas as pd
from naive_bayes import loocv, et
b1 = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
b2 = [
    ("tic-tac-toe.b4", 'Tic-tac-toe Endgame', loocv, False, None),
    ("SPECT.train", 'SPECT Heart Dataset', et, True, "SPECT.test"),
    ("soybean-small.b4", 'Soybean (small)', loocv, False, None),
    ("shuttle-landing-control.b4", 'Shuttle Landing Control', loocv, False, None),
    ("monks-1.train", 'Monks-1', et, True, "monks-1.test"),
    ("monks-2.train", 'Monks-2', et, True, "monks-2.test"),
    ("monks-3.train", 'Monks-3', et, True, "monks-3.test")
]
def fonk1(file, has_test, b3 = None):
    b4 = pd.read_csv(file, header=None)
    if has_test:
        b5 = pd.read_csv(b3, header=None)
        return b4, b5
    return b4, None
def fonk2(b4, b6):
    if b6 = = 'Shuttle Landing Control':
        b7 = b4.iloc[:, 1:].values.tolist()
        b8 = b4.iloc[:, 0].values.tolist()
    else:
        b7 = b4.iloc[:, :-1].values.tolist()
        b8 = b4.iloc[:, -1].values.tolist()
    return b7, b8
def fonk3(b13, train_file, b6, method, has_test, b3):
    train_data, b5 = fonk1(train_file, has_test, b3)
    if has_test:
        x_train, b9 = fonk2(train_data, b6)
        x_test, b10 = fonk2(b5, b6)
        b11 = set(b9)
        b12 = method(x_train, x_test, b9, b10, b11)
    else:
        b7, b8 = fonk2(train_data, b6)
        b11 = set(b8)
        b12 = method(b7, b8, b11, train_data.shape[0])
    b1.loc[b13, 'Dataset'] = b6
    b1.loc[b13, 'Accuracy(%)'] = b12
    print(f"{b6}: {b12:.2f}%")
for b13, dataset in enumerate(b2):
    train_file, b6, method, has_test, b3 = dataset
    fonk3(b13, train_file, b6, method, has_test, b3)
b1.to_csv("Data.csv", b13 = False)