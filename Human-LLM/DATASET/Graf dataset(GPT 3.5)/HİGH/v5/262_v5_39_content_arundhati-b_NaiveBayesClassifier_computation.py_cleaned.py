import pandas as pd
from naive_bayes import loocv, et
def fonk1(dataset_name, data, features_column_start, target_column, set_of_labels):
    b1 = data.iloc[:, features_column_start:].values.tolist()
    b2 = data.iloc[:, target_column].values.tolist()
    b3 = loocv(b1, b2, set_of_labels, len(data))
    print(f"{dataset_name}: {b3}")
    return b3
def fonk2(dataset_name, train_data, test_data, features_column_start, target_column, set_of_labels):
    b4 = train_data.iloc[:, features_column_start:].values.tolist()
    b5 = test_data.iloc[:, features_column_start:].values.tolist()
    b6 = train_data.iloc[:, target_column].values.tolist()
    b7 = test_data.iloc[:, target_column].values.tolist()
    b3 = et(b4, b5, b6, b7, set_of_labels)
    print(f"{dataset_name}: {b3}")
    return b3
def fonk3(results_df, b8 = "Data.csv"):
    results_df.to_csv(b8)
def fonk4():
    b9 = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
    b10 = pd.read_csv("tic-tac-toe.data", header=None)
    b11 = fonk1("Tic-tac-toe Endgame", b10, 0, -1, set(b10.iloc[:, -1]))
    b9.loc[0] = ['Tic-tac-toe Endgame', b11]
    b12 = pd.read_csv("SPECT.train", header=None)
    b13 = pd.read_csv("SPECT.test", header=None)
    b14 = fonk2("SPECT heart Dataset", b12, b13, 1, 0, set(b12.iloc[:, 0]))
    b9.loc[1] = ['SPECT heart Dataset', b14]
    b15 = pd.read_csv("soybean-small.data")
    b16 = fonk1("Soybean (small)", b15, 0, -1, set(b15.iloc[:, -1]))
    b9.loc[2] = ['Soybean (small)', b16]
    b17 = pd.read_csv("shuttle-landing-control.data")
    b18 = fonk1("Shuttle landing control", b17, 1, 0, set(b17.iloc[:, 0]))
    b9.loc[3] = ['Shuttle landing control', b18]
    b19 = pd.read_csv("monks-1.train", header=None)
    b20 = pd.read_csv("monks-1.test", header=None)
    b21 = fonk2("Monks-1", b19, b20, 1, 0, set(b19.iloc[:, 1]))
    b9.loc[4] = ['Monks-1', b21]
    b22 = pd.read_csv("monks-2.train", header=None)
    b23 = pd.read_csv("monks-2.test", header=None)
    b24 = fonk2("Monks-2", b22, b23, 1, 0, set(b22.iloc[:, 1]))
    b9.loc[5] = ['Monks-2', b24]
    b25 = pd.read_csv("monks-3.train", header=None)
    b26 = pd.read_csv("monks-3.test", header=None)
    b27 = fonk2("Monks-3", b25, b26, 1, 0, set(b25.iloc[:, 1]))
    b9.loc[6] = ['Monks-3', b27]
    fonk3(b9)
if b28 = = "__main__":
    fonk4()