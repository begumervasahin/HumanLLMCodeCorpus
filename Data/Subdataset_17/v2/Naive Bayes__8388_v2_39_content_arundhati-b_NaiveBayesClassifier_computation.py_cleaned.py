import pandas as pd
from naive_bayes import loocv, et
results_df = pd.DataFrame(columns=['Dataset', 'Accuracy(%)'])
datasets = [
    ("tic-tac-toe.data", 'Tic-tac-toe Endgame', loocv, False, None),
    ("SPECT.train", 'SPECT Heart Dataset', et, True, "SPECT.test"),
    ("soybean-small.data", 'Soybean (small)', loocv, False, None),
    ("shuttle-landing-control.data", 'Shuttle Landing Control', loocv, False, None),
    ("monks-1.train", 'Monks-1', et, True, "monks-1.test"),
    ("monks-2.train", 'Monks-2', et, True, "monks-2.test"),
    ("monks-3.train", 'Monks-3', et, True, "monks-3.test")
]
for index, (train_file, dataset_name, method, has_test, test_file) in enumerate(datasets):
    if has_test:
        train_data = pd.read_csv(train_file, header=None)
        test_data = pd.read_csv(test_file, header=None)
        x_train = train_data.iloc[:, 2:].values.tolist()
        y_train = train_data.iloc[:, 1].values.tolist()
        x_test = test_data.iloc[:, 2:].values.tolist()
        y_test = test_data.iloc[:, 1].values.tolist()
        unique_labels = set(y_train)
        accuracy = method(x_train, x_test, y_train, y_test, unique_labels)
    else:
        data = pd.read_csv(train_file, header=None)
        if dataset_name == 'Shuttle Landing Control':
            x = data.iloc[:, 1:].values.tolist()
            y = data.iloc[:, 0].values.tolist()
        else:
            x = data.iloc[:, :-1].values.tolist()
            y = data.iloc[:, -1].values.tolist()
        unique_labels = set(y)
        accuracy = method(x, y, unique_labels, data.shape[0])
    results_df.loc[index, 'Dataset'] = dataset_name
    results_df.loc[index, 'Accuracy(%)'] = accuracy
    print(f"{dataset_name}: {accuracy:.2f}%")
results_df.to_csv("Data.csv", index=False)