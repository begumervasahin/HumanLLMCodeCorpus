import pandas as pd
from naive_bayes import loocv, et
results = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
def process_loocv(file_path, dataset_name, header=None, target_col=-1):
    data = pd.read_csv(file_path, header=header)
    x = data.iloc[:, :target_col].values.tolist()
    y = data.iloc[:, target_col].values.tolist()
    unique_labels = set(y)
    accuracy = loocv(x, y, unique_labels, data.shape[0])
    print(f"{dataset_name}: {accuracy}")
    return accuracy
def process_et(train_path, test_path, dataset_name, header=None, x_start_col=2, y_col=1):
    train_data = pd.read_csv(train_path, header=header)
    test_data = pd.read_csv(test_path, header=header)
    x_train = train_data.iloc[:, x_start_col:].values.tolist()
    x_test = test_data.iloc[:, x_start_col:].values.tolist()
    y_train = train_data.iloc[:, y_col].values.tolist()
    y_test = test_data.iloc[:, y_col].values.tolist()
    unique_labels = set(y_train)
    accuracy = et(x_train, x_test, y_train, y_test, unique_labels)
    print(f"{dataset_name}: {accuracy}")
    return accuracy
results.loc[0] = ['Tic-tac-toe Endgame', process_loocv("tic-tac-toe.data", "Tic-tac-toe", header=None)]
results.loc[1] = ['SPECT heart Dataset', process_et("SPECT.train", "SPECT.test", "SPECT", header=None, x_start_col=1, y_col=0)]
results.loc[2] = ['Soybean (small)', process_loocv("soybean-small.data", "Soybean")]
results.loc[3] = ['Shuttle landing control', process_loocv("shuttle-landing-control.data", "Shuttle landing control", target_col=0)]
results.loc[4] = ['Monks-1', process_et("monks-1.train", "monks-1.test", "Monks-1", header=None, x_start_col=2, y_col=1)]
results.loc[5] = ['Monks-2', process_et("monks-2.train", "monks-2.test", "Monks-2", header=None, x_start_col=2, y_col=1)]
results.loc[6] = ['Monks-3', process_et("monks-3.train", "monks-3.test", "Monks-3", header=None, x_start_col=2, y_col=1)]
results.to_csv("Data.csv", index=False)