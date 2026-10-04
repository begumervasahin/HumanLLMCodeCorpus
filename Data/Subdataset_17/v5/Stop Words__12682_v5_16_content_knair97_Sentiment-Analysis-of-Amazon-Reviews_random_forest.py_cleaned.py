import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
def load_data(train_path, test_path):
    print('Reading training data')
    data = np.loadtxt(train_path, skiprows=1)
    y_train = data[:, 0]
    x_train = data[:, 1:]
    print('Reading testing data')
    x_test = np.loadtxt(test_path, skiprows=1)
    return x_train, y_train, x_test
def split_data(x, y, split_index):
    x_val = x[:split_index]
    y_val = y[:split_index]
    x_train = x[split_index:]
    y_train = y[split_index:]
    return x_train, y_train, x_val, y_val
def plot_accuracy(x, train_err, val_err, xlabel, ylabel, filename):
    plt.figure()
    plt.plot(x, train_err, label='Training Accuracy')
    plt.plot(x, val_err, label='Validation Accuracy')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig(filename)
def train_random_forest(x_train, y_train, x_val, y_val, param_range, param_name):
    train_err = []
    val_err = []
    for param in param_range:
        print(f'Creating the model with {param_name} = {param}')
        if param_name == 'max_depth':
            clf = RandomForestClassifier(n_estimators=200, max_depth=param, n_jobs=-1)
        elif param_name == 'min_samples_leaf':
            clf = RandomForestClassifier(n_estimators=200, min_samples_leaf=param, n_jobs=-1)
        else:
            raise ValueError('Unsupported parameter name')
        print('Fitting the model')
        clf.fit(x_train, y_train)
        train_accuracy = clf.score(x_train, y_train)
        val_accuracy = clf.score(x_val, y_val)
        print(f'{param_name.capitalize()}: {param}')
        print(f'Training accuracy: {train_accuracy}')
        print(f'Validation accuracy: {val_accuracy}')
        train_err.append(train_accuracy)
        val_err.append(val_accuracy)
    return train_err, val_err
def write_predictions(clf, x_test, output_path):
    print('Writing predictions')
    with open(output_path, 'w') as f:
        f.write('Id,Prediction\n')
        for it, sample in enumerate(x_test, start=1):
            pred = int(clf.predict(sample.reshape(1, -1))[0])
            f.write(f'{it},{pred}\n')
    print('Process completed.')
def main():
    train_path = 'training_data.txt'
    test_path = 'test_data.txt'
    output_path = 'forest_submissions.txt'
    x_train, y_train, x_test = load_data(train_path, test_path)
    x_train, y_train, x_val, y_val = split_data(x_train, y_train, 1000)
    depth_range = range(10, 35)
    train_err, val_err = train_random_forest(x_train, y_train, x_val, y_val, depth_range, 'max_depth')
    plot_accuracy(depth_range, train_err, val_err, 'Maximum Depth', 'Accuracy', 'forest_depth_vs_error.png')
    leaf_range = range(1, 10)
    train_err, val_err = train_random_forest(x_train, y_train, x_val, y_val, leaf_range, 'min_samples_leaf')
    plot_accuracy(leaf_range, train_err, val_err, 'Minimum Samples per Leaf Node', 'Accuracy', 'forest_leaf_nodes_vs_error.png')
    best_params = {'n_estimators': 200, 'max_depth': 20, 'min_samples_leaf': 1, 'n_jobs': -1}
    clf = RandomForestClassifier(**best_params)
    clf.fit(x_train, y_train)
    write_predictions(clf, x_test, output_path)
if __name__ == '__main__':
    main()