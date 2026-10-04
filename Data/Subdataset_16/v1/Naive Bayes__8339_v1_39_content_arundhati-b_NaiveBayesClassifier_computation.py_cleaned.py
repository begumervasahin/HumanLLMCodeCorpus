import pandas as pd
from naive_bayes import loocv, et
b1 = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
b2 = [
    ("tic-tac-toe.b11", 'Tic-tac-toe Endgame', loocv, False, None),
    ("SPECT.train", 'SPECT heart Dataset', et, True, "SPECT.b4"),
    ("soybean-small.b11", 'Soybean (small)', loocv, False, None),
    ("shuttle-landing-control.b11", 'Shuttle landing control', loocv, False, None),
    ("monks-1.train", 'Monks-1', et, True, "monks-1.b4"),
    ("monks-2.train", 'Monks-2', et, True, "monks-2.b4"),
    ("monks-3.train", 'Monks-3', et, True, "monks-3.b4")
]
for i, (train_file, b12, method, has_test, test_file) in enumerate(b2):
    if has_test:
        b3 = pd.read_csv(train_file, header=None)
        b4 = pd.read_csv(test_file, header=None)
        b5 = b3.iloc[:, 2:].values.tolist()
        b6 = b3.iloc[:, 1].values.tolist()
        b7 = b4.iloc[:, 2:].values.tolist()
        b8 = b4.iloc[:, 1].values.tolist()
        b9 = set(b6)
        b10 = method(b5, b7, b6, b8, b9)
    else:
        b11 = pd.read_csv(train_file, header=None)
        if b12 = = 'Shuttle landing control':
            b13 = b11.iloc[:, 1:].values.tolist()
            b14 = b11.iloc[:, 0].values.tolist()
        else:
            b13 = b11.iloc[:, :-1].values.tolist()
            b14 = b11.iloc[:, -1].values.tolist()
        b9 = set(b14)
        b10 = method(b13, b14, b9, b11.shape[0])
    print(b12, b10)
    b1.loc[i, 'Dataset'] = b12
    b1.loc[i, 'Accuracy(%)'] = b10
b1.to_csv("Data.csv", b15 = False)