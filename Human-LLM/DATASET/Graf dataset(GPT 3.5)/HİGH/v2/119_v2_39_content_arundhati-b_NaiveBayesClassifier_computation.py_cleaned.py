import pandas as pd
from naive_bayes import loocv, et
def fonk1(dataset_name, train_file, test_file, x_columns, y_column):
    b1 = pd.read_csv(train_file, b9=None)
    b2 = pd.read_csv(test_file, b9=None)
    b3 = b1.iloc[:, x_columns].values.tolist()
    b4 = b2.iloc[:, x_columns].values.tolist()
    b5 = b1.iloc[:, y_column].values.tolist()
    b6 = b2.iloc[:, y_column].values.tolist()
    b7 = et(b3, b4, b5, b6, set(b5))
    print(f"{dataset_name}:", b7)
    return b7
b8 = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
b8.loc[0] = ['Tic-tac-toe Endgame', loocv(*pd.read_csv("tic-tac-toe.data", b9 = None).values.tolist(), set(pd.read_csv("tic-tac-toe.data", b9=None).iloc[:, -1]))]
b8.loc[1] = ['SPECT heart Dataset', et(*pd.read_csv("SPECT.train", b9 = None).values.tolist(), *pd.read_csv("SPECT.b2", b9=None).values.tolist(), set(pd.read_csv("SPECT.train", b9=None).iloc[:, 0]))]
b8.loc[2] = ['Soybean (small)', loocv(*pd.read_csv("soybean-small.data").values.tolist(), set(pd.read_csv("soybean-small.data").iloc[:, -1]))]
b8.loc[3] = ['Shuttle landing control', loocv(*pd.read_csv("shuttle-landing-control.data").values.tolist(), set(pd.read_csv("shuttle-landing-control.data").iloc[:, 0]))]
b8.loc[4] = ['Monks-1', fonk1('Monks-1', "monks-1.train", "monks-1.b2", range(2, 8), 1)]
b8.loc[5] = ['Monks-2', fonk1('Monks-2', "monks-2.train", "monks-2.b2", range(2, 8), 1)]
b8.loc[6] = ['Monks-3', fonk1('Monks-3', "monks-3.train", "monks-3.b2", range(2, 8), 1)]
b8.to_csv("Data.csv", b10 = False)