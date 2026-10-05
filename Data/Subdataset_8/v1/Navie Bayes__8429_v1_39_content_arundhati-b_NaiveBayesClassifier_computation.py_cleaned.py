import pandas as pd
from naive_bayes import loocv, et
fin = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
tic_tac_toe_data = pd.read_csv("tic-tac-toe.data", header=None)
tic_tac_toe_x = tic_tac_toe_data.iloc[:, :-1].values.tolist()
tic_tac_toe_y = tic_tac_toe_data.iloc[:, -1].values.tolist()
at = set(tic_tac_toe_y)
tic_tac_toe_accuracy = loocv(tic_tac_toe_x, tic_tac_toe_y, at, tic_tac_toe_data.shape[0])
print("Tic-tac-toe Endgame:", tic_tac_toe_accuracy)
fin.loc[0, 'Dataset'] = 'Tic-tac-toe Endgame'
fin.loc[0, 'Accuracy(%)'] = tic_tac_toe_accuracy
training = pd.read_csv("SPECT.train", header=None)
test = pd.read_csv("SPECT.test", header=None)
x_train = training.iloc[:, 1:].values.tolist()
x_test = test.iloc[:, 1:].values.tolist()
y_train = training.iloc[:, 0].values.tolist()
y_test = test.iloc[:, 0].values.tolist()
at = set(y_train)
spect_accuracy = et(x_train, x_test, y_train, y_test, at)
print("SPECT heart Dataset:", spect_accuracy)
fin.loc[1, 'Dataset'] = 'SPECT heart Dataset'
fin.loc[1, 'Accuracy(%)'] = spect_accuracy
soybean_data = pd.read_csv("soybean-small.data")
soybean_x = soybean_data.iloc[:, :-1].values.tolist()
soybean_y = soybean_data.iloc[:, -1].values.tolist()
at = set(soybean_y)
soybean_accuracy = loocv(soybean_x, soybean_y, at, soybean_data.shape[0])
print("Soybean (small):", soybean_accuracy)
fin.loc[2, 'Dataset'] = 'Soybean (small)'
fin.loc[2, 'Accuracy(%)'] = soybean_accuracy
shuttle_data = pd.read_csv("shuttle-landing-control.data")
shuttle_x = shuttle_data.iloc[:, 1:].values.tolist()
shuttle_y = shuttle_data.iloc[:, 0].values.tolist()
at = set(shuttle_y)
shuttle_accuracy = loocv(shuttle_x, shuttle_y, at, shuttle_data.shape[0])
print("Shuttle landing control:", shuttle_accuracy)
fin.loc[3, 'Dataset'] = 'Shuttle landing control'
fin.loc[3, 'Accuracy(%)'] = shuttle_accuracy
training = pd.read_csv("monks-1.train", header=None)
test = pd.read_csv("monks-1.test", header=None)
training = training.iloc[:, :-1]
test = test.iloc[:, :-1]
x_train = training.iloc[:, 2:].values.tolist()
x_test = test.iloc[:, 2:].values.tolist()
y_train = training.iloc[:, 1].values.tolist()
y_test = test.iloc[:, 1].values.tolist()
at = set(y_train)
monks_1_accuracy = et(x_train, x_test, y_train, y_test, at)
print("Monks-1:", monks_1_accuracy)
fin.loc[4, 'Dataset'] = 'Monks-1'
fin.loc[4, 'Accuracy(%)'] = monks_1_accuracy
training = pd.read_csv("monks-2.train", header=None).iloc[:, :-1]
test = pd.read_csv("monks-2.test", header=None).iloc[:, :-1]
x_train = training.iloc[:, 2:].values.tolist()
x_test = test.iloc[:, 2:].values.tolist()
y_train = training.iloc[:, 1].values.tolist()
y_test = test.iloc[:, 1].values.tolist()
at = set(y_train)
monks_2_accuracy = et(x_train, x_test, y_train, y_test, at)
print("Monks-2:", monks_2_accuracy)
fin.loc[5, 'Dataset'] = 'Monks-2'
fin.loc[5, 'Accuracy(%)'] = monks_2_accuracy
training = pd.read_csv("monks-3.train", header=None).iloc[:, :-1]
test = pd.read_csv("monks-3.test", header=None).iloc[:, :-1]
x_train = training.iloc[:, 2:].values.tolist()
x_test = test.iloc[:, 2:].values.tolist()
y_train = training.iloc[:, 1].values.tolist()
y_test = test.iloc[:, 1].values.tolist()
at = set(y_train)
monks_3_accuracy = et(x_train, x_test, y_train, y_test, at)
print("Monks-3:", monks_3_accuracy)
fin.loc[6, 'Dataset'] = 'Monks-3'
fin.loc[6, 'Accuracy(%)'] = monks_3_accuracy
fin.to_csv("Data.csv", index=False)