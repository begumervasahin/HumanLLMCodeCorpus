import pandas as pd
from naive_bayes import loocv, et
fin = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
data_tic_tac_toe = pd.read_csv("tic-tac-toe.data", header=None)
x_tic_tac_toe = data_tic_tac_toe.iloc[:, :-1].values.tolist()
y_tic_tac_toe = data_tic_tac_toe.iloc[:, -1].values.tolist()
at_tic_tac_toe = set(y_tic_tac_toe)
accuracy_tic_tac_toe = loocv(x_tic_tac_toe, y_tic_tac_toe, at_tic_tac_toe, data_tic_tac_toe.shape[0])
print("Tic-tac-toe Endgame:", accuracy_tic_tac_toe)
fin.loc[0, 'Dataset'] = 'Tic-tac-toe Endgame'
fin.loc[0, 'Accuracy(%)'] = accuracy_tic_tac_toe
training_spect = pd.read_csv("SPECT.train", header=None)
test_spect = pd.read_csv("SPECT.test", header=None)
x_train_spect = training_spect.iloc[:, 1:].values.tolist()
x_test_spect = test_spect.iloc[:, 1:].values.tolist()
y_train_spect = training_spect.iloc[:, 0].values.tolist()
y_test_spect = test_spect.iloc[:, 0].values.tolist()
at_spect = set(y_train_spect)
accuracy_spect = et(x_train_spect, x_test_spect, y_train_spect, y_test_spect, at_spect)
print("SPECT heart Dataset:", accuracy_spect)
fin.loc[1, 'Dataset'] = 'SPECT heart Dataset'
fin.loc[1, 'Accuracy(%)'] = accuracy_spect
data_soybean = pd.read_csv("soybean-small.data")
x_soybean = data_soybean.iloc[:, :-1].values.tolist()
y_soybean = data_soybean.iloc[:, -1].values.tolist()
at_soybean = set(y_soybean)
accuracy_soybean = loocv(x_soybean, y_soybean, at_soybean, data_soybean.shape[0])
print("Soybean (small):", accuracy_soybean)
fin.loc[2, 'Dataset'] = 'Soybean (small)'
fin.loc[2, 'Accuracy(%)'] = accuracy_soybean
data_shuttle = pd.read_csv("shuttle-landing-control.data")
x_shuttle = data_shuttle.iloc[:, 1:].values.tolist()
y_shuttle = data_shuttle.iloc[:, 0].values.tolist()
at_shuttle = set(y_shuttle)
accuracy_shuttle = loocv(x_shuttle, y_shuttle, at_shuttle, data_shuttle.shape[0])
print("Shuttle landing control:", accuracy_shuttle)
fin.loc[3, 'Dataset'] = 'Shuttle landing control'
fin.loc[3, 'Accuracy(%)'] = accuracy_shuttle
training_monks_1 = pd.read_csv("monks-1.train", header=None).iloc[:, :-1]
test_monks_1 = pd.read_csv("monks-1.test", header=None).iloc[:, :-1]
x_train_monks_1 = training_monks_1.iloc[:, 2:].values.tolist()
x_test_monks_1 = test_monks_1.iloc[:, 2:].values.tolist()
y_train_monks_1 = training_monks_1.iloc[:, 1].values.tolist()
y_test_monks_1 = test_monks_1.iloc[:, 1].values.tolist()
at_monks_1 = set(y_train_monks_1)
accuracy_monks_1 = et(x_train_monks_1, x_test_monks_1, y_train_monks_1, y_test_monks_1, at_monks_1)
print("Monks-1:", accuracy_monks_1)
fin.loc[4, 'Dataset'] = 'Monks-1'
fin.loc[4, 'Accuracy(%)'] = accuracy_monks_1
training_monks_2 = pd.read_csv("monks-2.train", header=None).iloc[:, :-1]
test_monks_2 = pd.read_csv("monks-2.test", header=None).iloc[:, :-1]
x_train_monks_2 = training_monks_2.iloc[:, 2:].values.tolist()
x_test_monks_2 = test_monks_2.iloc[:, 2:].values.tolist()
y_train_monks_2 = training_monks_2.iloc[:, 1].values.tolist()
y_test_monks_2 = test_monks_2.iloc[:, 1].values.tolist()
at_monks_2 = set(y_train_monks_2)
accuracy_monks_2 = et(x_train_monks_2, x_test_monks_2, y_train_monks_2, y_test_monks_2, at_monks_2)
print("Monks-2:", accuracy_monks_2)
fin.loc[5, 'Dataset'] = 'Monks-2'
fin.loc[5, 'Accuracy(%)'] = accuracy_monks_2
training_monks_3 = pd.read_csv("monks-3.train", header=None).iloc[:, :-1]
test_monks_3 = pd.read_csv("monks-3.test", header=None).iloc[:, :-1]
x_train_monks_3 = training_monks_3.iloc[:, 2:].values.tolist()
x_test_monks_3 = test_monks_3.iloc[:, 2:].values.tolist()
y_train_monks_3 = training_monks_3.iloc[:, 1].values.tolist()
y_test_monks_3 = test_monks_3.iloc[:, 1].values.tolist()
at_monks_3 = set(y_train_monks_3)
accuracy_monks_3 = et(x_train_monks_3, x_test_monks_3, y_train_monks_3, y_test_monks_3, at_monks_3)
print("Monks-3:", accuracy_monks_3)
fin.loc[6, 'Dataset'] = 'Monks-3'
fin.loc[6, 'Accuracy(%)'] = accuracy_monks_3
fin.to_csv("Data.csv")