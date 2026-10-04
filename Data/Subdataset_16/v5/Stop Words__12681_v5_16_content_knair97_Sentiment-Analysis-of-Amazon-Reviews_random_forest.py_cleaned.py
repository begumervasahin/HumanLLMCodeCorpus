import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
def fonk1(b16, b17):
    print('Reading training b1')
    b1 = np.loadtxt(b16, skiprows=1)
    b2 = b1[:, 0]
    b3 = b1[:, 1:]
    print('Reading testing b1')
    b4 = np.loadtxt(b17, skiprows=1)
    return b3, b2, b4
def fonk2(x, y, split_index):
    b5 = x[:split_index]
    b6 = y[:split_index]
    b3 = x[split_index:]
    b2 = y[split_index:]
    return b3, b2, b5, b6
def fonk3(x, b8, b9, xlabel, ylabel, filename):
    plt.figure()
    plt.plot(x, b8, b7 = 'Training Accuracy')
    plt.plot(x, b9, b7 = 'Validation Accuracy')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig(filename)
def fonk4(b3, b2, b5, b6, param_range, b10):
    b8 = []
    b9 = []
    for param in param_range:
        print(f'Creating the model with {b10} = {param}')
        if b10 = = 'max_depth':
            b11 = RandomForestClassifier(n_estimators=200, max_depth=param, n_jobs=-1)
        elif b10 = = 'min_samples_leaf':
            b11 = RandomForestClassifier(n_estimators=200, min_samples_leaf=param, n_jobs=-1)
        else:
            raise ValueError('Unsupported parameter name')
        print('Fitting the model')
        b11.fit(b3, b2)
        b12 = b11.score(b3, b2)
        b13 = b11.score(b5, b6)
        print(f'{b10.capitalize()}: {param}')
        print(f'Training accuracy: {b12}')
        print(f'Validation accuracy: {b13}')
        b8.append(b12)
        b9.append(b13)
    return b8, b9
def fonk5(b11, b4, b18):
    print('Writing predictions')
    with open(b18, 'w') as f:
        f.write('Id,Prediction\n')
        for it, sample in enumerate(b4, b14 = 1):
            b15 = int(b11.predict(sample.reshape(1, -1))[0])
            f.write(f'{it},{b15}\n')
    print('Process completed.')
def fonk6():
    b16 = 'training_data.txt'
    b17 = 'test_data.txt'
    b18 = 'forest_submissions.txt'
    b3, b2, b4 = fonk1(b16, b17)
    b3, b2, b5, b6 = fonk2(b3, b2, 1000)
    b19 = range(10, 35)
    b8, b9 = fonk4(b3, b2, b5, b6, b19, 'max_depth')
    fonk3(b19, b8, b9, 'Maximum Depth', 'Accuracy', 'forest_depth_vs_error.png')
    b20 = range(1, 10)
    b8, b9 = fonk4(b3, b2, b5, b6, b20, 'min_samples_leaf')
    fonk3(b20, b8, b9, 'Minimum Samples per Leaf Node', 'Accuracy', 'forest_leaf_nodes_vs_error.png')
    b21 = {'n_estimators': 200, 'max_depth': 20, 'min_samples_leaf': 1, 'n_jobs': -1}
    b11 = RandomForestClassifier(**b21)
    b11.fit(b3, b2)
    fonk5(b11, b4, b18)
if b22 = = '__main__':
    fonk6()