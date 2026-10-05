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
b8 = pd.read_csv("SPECT.test", header=None)
b9 = b7.iloc[:, 1:].values.tolist()
b10 = b8.iloc[:, 1:].values.tolist()
b11 = b7.iloc[:, 0].values.tolist()
b12 = b8.iloc[:, 0].values.tolist()
b13 = set(b11)
b14 = et(b9, b10, b11, b12, b13)
print("SPECT heart Dataset:", b14)
b1.loc[1, 'Dataset'] = 'SPECT heart Dataset'
b1.loc[1, 'Accuracy(%)'] = b14
b15 = pd.read_csv("soybean-small.data")
b16 = b15.iloc[:, :-1].values.tolist()
b17 = b15.iloc[:, -1].values.tolist()
b18 = set(b17)
b19 = loocv(b16, b17, b18, b15.shape[0])
print("Soybean (small):", b19)
b1.loc[2, 'Dataset'] = 'Soybean (small)'
b1.loc[2, 'Accuracy(%)'] = b19
b20 = pd.read_csv("shuttle-landing-control.data")
b21 = b20.iloc[:, 1:].values.tolist()
b22 = b20.iloc[:, 0].values.tolist()
b23 = set(b22)
b24 = loocv(b21, b22, b23, b20.shape[0])
print("Shuttle landing control:", b24)
b1.loc[3, 'Dataset'] = 'Shuttle landing control'
b1.loc[3, 'Accuracy(%)'] = b24
b25 = pd.read_csv("monks-1.train", header=None).iloc[:, :-1]
b26 = pd.read_csv("monks-1.test", header=None).iloc[:, :-1]
b27 = b25.iloc[:, 2:].values.tolist()
b28 = b26.iloc[:, 2:].values.tolist()
b29 = b25.iloc[:, 1].values.tolist()
b30 = b26.iloc[:, 1].values.tolist()
b31 = set(b29)
b32 = et(b27, b28, b29, b30, b31)
print("Monks-1:", b32)
b1.loc[4, 'Dataset'] = 'Monks-1'
b1.loc[4, 'Accuracy(%)'] = b32
b33 = pd.read_csv("monks-2.train", header=None).iloc[:, :-1]
b34 = pd.read_csv("monks-2.test", header=None).iloc[:, :-1]
b35 = b33.iloc[:, 2:].values.tolist()
b36 = b34.iloc[:, 2:].values.tolist()
b37 = b33.iloc[:, 1].values.tolist()
b38 = b34.iloc[:, 1].values.tolist()
b39 = set(b37)
b40 = et(b35, b36, b37, b38, b39)
print("Monks-2:", b40)
b1.loc[5, 'Dataset'] = 'Monks-2'
b1.loc[5, 'Accuracy(%)'] = b40
b41 = pd.read_csv("monks-3.train", header=None).iloc[:, :-1]
b42 = pd.read_csv("monks-3.test", header=None).iloc[:, :-1]
b43 = b41.iloc[:, 2:].values.tolist()
b44 = b42.iloc[:, 2:].values.tolist()
b45 = b41.iloc[:, 1].values.tolist()
b46 = b42.iloc[:, 1].values.tolist()
b47 = set(b45)
b48 = et(b43, b44, b45, b46, b47)
print("Monks-3:", b48)
b1.loc[6, 'Dataset'] = 'Monks-3'
b1.loc[6, 'Accuracy(%)'] = b48
b1.to_csv("Data.csv")