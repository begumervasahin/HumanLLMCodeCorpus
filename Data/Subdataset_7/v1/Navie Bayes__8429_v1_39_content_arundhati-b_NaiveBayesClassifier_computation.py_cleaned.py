import pandas as pd
from naive_bayes import loocv, et
b1 = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
b2 = pd.read_csv("tic-tac-toe.data", header=None)
b3 = b2.iloc[:, :-1].values.tolist()
b4 = b2.iloc[:, -1].values.tolist()
b5 = set(b4)
b6 = loocv(b3, b4, b5, b2.shape[0])
print("Tic-tac-toe Endgame:", b6)
b1.loc[0, 'Dataset'] = 'Tic-tac-toe Endgame'
b1.loc[0, 'Accuracy(%)'] = b6
b7 = pd.read_csv("SPECT.train", header=None)
b8 = pd.read_csv("SPECT.b8", header=None)
b9 = b7.iloc[:, 1:].values.tolist()
b10 = b8.iloc[:, 1:].values.tolist()
b11 = b7.iloc[:, 0].values.tolist()
b12 = b8.iloc[:, 0].values.tolist()
b5 = set(b11)
b13 = et(b9, b10, b11, b12, b5)
print("SPECT heart Dataset:", b13)
b1.loc[1, 'Dataset'] = 'SPECT heart Dataset'
b1.loc[1, 'Accuracy(%)'] = b13
b14 = pd.read_csv("soybean-small.data")
b15 = b14.iloc[:, :-1].values.tolist()
b16 = b14.iloc[:, -1].values.tolist()
b5 = set(b16)
b17 = loocv(b15, b16, b5, b14.shape[0])
print("Soybean (small):", b17)
b1.loc[2, 'Dataset'] = 'Soybean (small)'
b1.loc[2, 'Accuracy(%)'] = b17
b18 = pd.read_csv("shuttle-landing-control.data")
b19 = b18.iloc[:, 1:].values.tolist()
b20 = b18.iloc[:, 0].values.tolist()
b5 = set(b20)
b21 = loocv(b19, b20, b5, b18.shape[0])
print("Shuttle landing control:", b21)
b1.loc[3, 'Dataset'] = 'Shuttle landing control'
b1.loc[3, 'Accuracy(%)'] = b21
b7 = pd.read_csv("monks-1.train", header=None)
b8 = pd.read_csv("monks-1.b8", header=None)
b7 = b7.iloc[:, :-1]
b8 = b8.iloc[:, :-1]
b9 = b7.iloc[:, 2:].values.tolist()
b10 = b8.iloc[:, 2:].values.tolist()
b11 = b7.iloc[:, 1].values.tolist()
b12 = b8.iloc[:, 1].values.tolist()
b5 = set(b11)
b22 = et(b9, b10, b11, b12, b5)
print("Monks-1:", b22)
b1.loc[4, 'Dataset'] = 'Monks-1'
b1.loc[4, 'Accuracy(%)'] = b22
b7 = pd.read_csv("monks-2.train", header=None).iloc[:, :-1]
b8 = pd.read_csv("monks-2.b8", header=None).iloc[:, :-1]
b9 = b7.iloc[:, 2:].values.tolist()
b10 = b8.iloc[:, 2:].values.tolist()
b11 = b7.iloc[:, 1].values.tolist()
b12 = b8.iloc[:, 1].values.tolist()
b5 = set(b11)
b23 = et(b9, b10, b11, b12, b5)
print("Monks-2:", b23)
b1.loc[5, 'Dataset'] = 'Monks-2'
b1.loc[5, 'Accuracy(%)'] = b23
b7 = pd.read_csv("monks-3.train", header=None).iloc[:, :-1]
b8 = pd.read_csv("monks-3.b8", header=None).iloc[:, :-1]
b9 = b7.iloc[:, 2:].values.tolist()
b10 = b8.iloc[:, 2:].values.tolist()
b11 = b7.iloc[:, 1].values.tolist()
b12 = b8.iloc[:, 1].values.tolist()
b5 = set(b11)
b24 = et(b9, b10, b11, b12, b5)
print("Monks-3:", b24)
b1.loc[6, 'Dataset'] = 'Monks-3'
b1.loc[6, 'Accuracy(%)'] = b24
b1.to_csv("Data.csv", b25 = False)