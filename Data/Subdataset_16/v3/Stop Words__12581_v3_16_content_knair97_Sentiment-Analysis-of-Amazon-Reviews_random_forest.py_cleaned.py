import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
def fonk1():
    print('Reading training data')
    b1 = np.loadtxt('b1.txt', skiprows=1)
    b2 = b1[:, 0]
    b3 = b1[:, 1:]
    print('Reading testing data')
    b4 = np.loadtxt('test_data.txt', skiprows=1)
    return b3, b2, b4
def fonk2(b3, b2, b5 = 1000):
    b6 = b3[:b5]
    b7 = b2[:b5]
    b3 = b3[b5:]
    b2 = b2[b5:]
    return b3, b2, b6, b7
def fonk3(b3, b2, b6, b7):
    b8 = []
    b9 = []
    b10 = range(10, 35)
    for d in b10:
        print(f'Creating the model for maximum b11 = {d}')
        b12 = RandomForestClassifier(n_estimators=200, max_depth=d, n_jobs=-1)
        b12.fit(b3, b2)
        b13 = b12.score(b3, b2)
        b14 = b12.score(b6, b7)
        b8.append(b13)
        b9.append(b14)
        print(f'Max b11: {d}, Training Accuracy: {b13}, Validation Accuracy: {b14}')
    return b10, b8, b9
def fonk4(b3, b2, b6, b7):
    b8 = []
    b9 = []
    b15 = range(1, 10)
    for l in b15:
        print(f'Creating the model for minimum samples for leaf b16 = {l}')
        b12 = RandomForestClassifier(n_estimators=200, min_samples_leaf=l, n_jobs=-1)
        b12.fit(b3, b2)
        b13 = b12.score(b3, b2)
        b14 = b12.score(b6, b7)
        b8.append(b13)
        b9.append(b14)
        print(f'Min samples per leaf b16: {l}, Training Accuracy: {b13}, Validation Accuracy: {b14}')
    return b15, b8, b9
def fonk5(x, b8, b9, xlabel, ylabel, b18):
    plt.figure()
    plt.plot(x, b8, b17 = 'Training Accuracy')
    plt.plot(x, b9, b17 = 'Validation Accuracy')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig(b18)
def fonk6(b12, b4, b18 = 'forest_submissions.txt'):
    print('Writing predictions')
    with open(b18, 'w') as f:
        f.write('Id,Prediction\n')
        for it, sample in enumerate(b4, b19 = 1):
            b20 = int(b12.predict(sample.reshape(1, -1))[0])
            f.write(f'{it},{b20}\n')
def fonk7():
    b3, b2, b4 = fonk1()
    b3, b2, b6, b7 = fonk2(b3, b2)
    b10, train_err_depth, b21 = fonk3(b3, b2, b6, b7)
    fonk5(b10, train_err_depth, b21, 'Maximum Depth', 'Accuracy', 'forest_depth_vs_error.png')
    b15, train_err_leaf, b22 = fonk4(b3, b2, b6, b7)
    fonk5(b15, train_err_leaf, b22, 'Minimum Samples per Leaf Node', 'Accuracy', 'forest_leaf_nodes_vs_error.png')
    b12 = RandomForestClassifier(n_estimators=200, min_samples_leaf=b15[-1], n_jobs=-1)
    b12.fit(b3, b2)
    fonk6(b12, b4)
if b23 = = '__main__':
    fonk7()