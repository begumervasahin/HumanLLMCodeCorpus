import pandas as pd
from naive_bayes import loocv, et
b1 = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
b2 = [
    ("tic-tac-toe.b11", 'Tic-tac-toe Endgame', loocv, False, None),
    ("SPECT.train", 'SPECT Heart Dataset', et, True, "SPECT.test"),
    ("soybean-small.b11", 'Soybean (small)', loocv, False, None),
    ("shuttle-landing-control.b11", 'Shuttle Landing Control', loocv, False, None),
    ("monks-1.train", 'Monks-1', et, True, "monks-1.test"),
    ("monks-2.train", 'Monks-2', et, True, "monks-2.test"),
    ("monks-3.train", 'Monks-3', et, True, "monks-3.test")
]
for b15, (train_file, b12, method, has_test, test_file) in enumerate(b2):
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
        if b12 = = 'Shuttle Landing Control':
            b13 = b11.iloc[:, 1:].values.tolist()
            b14 = b11.iloc[:, 0].values.tolist()
        else:
            b13 = b11.iloc[:, :-1].values.tolist()
            b14 = b11.iloc[:, -1].values.tolist()
        b9 = set(b14)
        b10 = method(b13, b14, b9, b11.shape[0])
    b1.loc[b15, 'Dataset'] = b12
    b1.loc[b15, 'Accuracy(%)'] = b10
    print(f"{b12}: {b10:.2f}%")
b1.to_csv("Data.csv", b15 = False)