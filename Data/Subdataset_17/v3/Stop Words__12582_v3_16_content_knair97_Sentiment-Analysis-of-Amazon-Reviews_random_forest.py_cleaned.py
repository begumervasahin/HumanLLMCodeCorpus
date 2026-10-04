import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
def load_data():
    print('Reading training data')
    training_data = np.loadtxt('training_data.txt', skiprows=1)
    y_train = training_data[:, 0]
    x_train = training_data[:, 1:]
    print('Reading testing data')
    x_test = np.loadtxt('test_data.txt', skiprows=1)
    return x_train, y_train, x_test
def split_data(x_train, y_train, val_size=1000):
    x_val = x_train[:val_size]
    y_val = y_train[:val_size]
    x_train = x_train[val_size:]
    y_train = y_train[val_size:]
    return x_train, y_train, x_val, y_val
def evaluate_depth(x_train, y_train, x_val, y_val):
    train_err = []
    val_err = []
    depths = range(10, 35)
    for d in depths:
        print(f'Creating the model for maximum depth = {d}')
        clf = RandomForestClassifier(n_estimators=200, max_depth=d, n_jobs=-1)
        clf.fit(x_train, y_train)
        train_acc = clf.score(x_train, y_train)
        val_acc = clf.score(x_val, y_val)
        train_err.append(train_acc)
        val_err.append(val_acc)
        print(f'Max depth: {d}, Training Accuracy: {train_acc}, Validation Accuracy: {val_acc}')
    return depths, train_err, val_err
def evaluate_leaf_nodes(x_train, y_train, x_val, y_val):
    train_err = []
    val_err = []
    leaf_nodes = range(1, 10)
    for l in leaf_nodes:
        print(f'Creating the model for minimum samples for leaf node = {l}')
        clf = RandomForestClassifier(n_estimators=200, min_samples_leaf=l, n_jobs=-1)
        clf.fit(x_train, y_train)
        train_acc = clf.score(x_train, y_train)
        val_acc = clf.score(x_val, y_val)
        train_err.append(train_acc)
        val_err.append(val_acc)
        print(f'Min samples per leaf node: {l}, Training Accuracy: {train_acc}, Validation Accuracy: {val_acc}')
    return leaf_nodes, train_err, val_err
def plot_results(x, train_err, val_err, xlabel, ylabel, filename):
    plt.figure()
    plt.plot(x, train_err, label='Training Accuracy')
    plt.plot(x, val_err, label='Validation Accuracy')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig(filename)
def write_predictions(clf, x_test, filename='forest_submissions.txt'):
    print('Writing predictions')
    with open(filename, 'w') as f:
        f.write('Id,Prediction\n')
        for it, sample in enumerate(x_test, start=1):
            pred = int(clf.predict(sample.reshape(1, -1))[0])
            f.write(f'{it},{pred}\n')
def main():
    x_train, y_train, x_test = load_data()
    x_train, y_train, x_val, y_val = split_data(x_train, y_train)
    depths, train_err_depth, val_err_depth = evaluate_depth(x_train, y_train, x_val, y_val)
    plot_results(depths, train_err_depth, val_err_depth, 'Maximum Depth', 'Accuracy', 'forest_depth_vs_error.png')
    leaf_nodes, train_err_leaf, val_err_leaf = evaluate_leaf_nodes(x_train, y_train, x_val, y_val)
    plot_results(leaf_nodes, train_err_leaf, val_err_leaf, 'Minimum Samples per Leaf Node', 'Accuracy', 'forest_leaf_nodes_vs_error.png')
    clf = RandomForestClassifier(n_estimators=200, min_samples_leaf=leaf_nodes[-1], n_jobs=-1)
    clf.fit(x_train, y_train)
    write_predictions(clf, x_test)
if __name__ == '__main__':
    main()