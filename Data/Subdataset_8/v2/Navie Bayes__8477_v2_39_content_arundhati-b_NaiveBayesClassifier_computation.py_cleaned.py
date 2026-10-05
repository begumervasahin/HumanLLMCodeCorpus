import pandas as pd
from naive_bayes import loocv, et
def process_dataset(dataset_name, train_file, test_file, x_columns, y_column):
    training = pd.read_csv(train_file, header=None)
    test = pd.read_csv(test_file, header=None)
    x_train = training.iloc[:, x_columns].values.tolist()
    x_test = test.iloc[:, x_columns].values.tolist()
    y_train = training.iloc[:, y_column].values.tolist()
    y_test = test.iloc[:, y_column].values.tolist()
    accuracy = et(x_train, x_test, y_train, y_test, set(y_train))
    print(f"{dataset_name}:", accuracy)
    return accuracy
dataset_accuracies = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
dataset_accuracies.loc[0] = ['Tic-tac-toe Endgame', loocv(*pd.read_csv("tic-tac-toe.data", header=None).values.tolist(), set(pd.read_csv("tic-tac-toe.data", header=None).iloc[:, -1]))]
dataset_accuracies.loc[1] = ['SPECT heart Dataset', et(*pd.read_csv("SPECT.train", header=None).values.tolist(), *pd.read_csv("SPECT.test", header=None).values.tolist(), set(pd.read_csv("SPECT.train", header=None).iloc[:, 0]))]
dataset_accuracies.loc[2] = ['Soybean (small)', loocv(*pd.read_csv("soybean-small.data").values.tolist(), set(pd.read_csv("soybean-small.data").iloc[:, -1]))]
dataset_accuracies.loc[3] = ['Shuttle landing control', loocv(*pd.read_csv("shuttle-landing-control.data").values.tolist(), set(pd.read_csv("shuttle-landing-control.data").iloc[:, 0]))]
dataset_accuracies.loc[4] = ['Monks-1', process_dataset('Monks-1', "monks-1.train", "monks-1.test", range(2, 8), 1)]
dataset_accuracies.loc[5] = ['Monks-2', process_dataset('Monks-2', "monks-2.train", "monks-2.test", range(2, 8), 1)]
dataset_accuracies.loc[6] = ['Monks-3', process_dataset('Monks-3', "monks-3.train", "monks-3.test", range(2, 8), 1)]
dataset_accuracies.to_csv("Data.csv", index=False)