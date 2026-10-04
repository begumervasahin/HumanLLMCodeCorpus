import pandas as pd
from naive_bayes import loocv, et
b1 = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
def fonk1(file_path, dataset_name, b2 = None, b14=-1):
    b3 = pd.read_csv(file_path, b2=b2)
    b4 = b3.iloc[:, :b14].values.tolist()
    b5 = b3.iloc[:, b14].values.tolist()
    b6 = set(b5)
    b7 = loocv(b4, b5, b6, b3.shape[0])
    print(f"{dataset_name}: {b7}")
    return b7
def fonk2(train_path, test_path, dataset_name, b2 = None, x_start_col=2, y_col=1):
    b8 = pd.read_csv(train_path, b2=b2)
    b9 = pd.read_csv(test_path, b2=b2)
    b10 = b8.iloc[:, x_start_col:].values.tolist()
    b11 = b9.iloc[:, x_start_col:].values.tolist()
    b12 = b8.iloc[:, y_col].values.tolist()
    b13 = b9.iloc[:, y_col].values.tolist()
    b6 = set(b12)
    b7 = et(b10, b11, b12, b13, b6)
    print(f"{dataset_name}: {b7}")
    return b7
b1.loc[0] = ['Tic-tac-toe Endgame', fonk1("tic-tac-toe.b3", "Tic-tac-toe", b2 = None)]
b1.loc[1] = ['SPECT heart Dataset', fonk2("SPECT.train", "SPECT.test", "SPECT", b2 = None, x_start_col=1, y_col=0)]
b1.loc[2] = ['Soybean (small)', fonk1("soybean-small.b3", "Soybean")]
b1.loc[3] = ['Shuttle landing control', fonk1("shuttle-landing-control.b3", "Shuttle landing control", b14 = 0)]
b1.loc[4] = ['Monks-1', fonk2("monks-1.train", "monks-1.test", "Monks-1", b2 = None, x_start_col=2, y_col=1)]
b1.loc[5] = ['Monks-2', fonk2("monks-2.train", "monks-2.test", "Monks-2", b2 = None, x_start_col=2, y_col=1)]
b1.loc[6] = ['Monks-3', fonk2("monks-3.train", "monks-3.test", "Monks-3", b2 = None, x_start_col=2, y_col=1)]
b1.to_csv("Data.csv", b15 = False)