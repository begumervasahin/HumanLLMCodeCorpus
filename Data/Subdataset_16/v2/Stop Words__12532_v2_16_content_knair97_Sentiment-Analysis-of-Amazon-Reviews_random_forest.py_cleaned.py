import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
def fonk1():
    print('Reading training b1')
    b1 = np.loadtxt('training_data.txt', skiprows=1)
    b2 = b1[:, 0]
    b3 = b1[:, 1:]
    print('Reading testing b1')
    b4 = np.loadtxt('test_data.txt', skiprows=1)
    b5 = b3[:1000]
    b6 = b2[:1000]
    b3 = b3[1000:]
    b2 = b2[1000:]
    b7 = []
    b8 = []
    b9 = []
    for d in range(10, 35):
        print(f'Creating the model for maximum b9 = {d}')
        b10 = RandomForestClassifier(n_estimators=200, max_depth=d, n_jobs=-1)
        print('Fitting the model')
        b10.fit(b3, b2)
        b11 = b10.score(b3, b2)
        b12 = b10.score(b5, b6)
        b8.append(b11)
        b7.append(b12)
        b9.append(d)
        print(f'Max b9: {d}, Training Accuracy: {b11}, Validation Accuracy: {b12}')
    plt.figure()
    plt.plot(b9, b8, b13 = 'Training Accuracy')
    plt.plot(b9, b7, b13 = 'Validation Accuracy')
    plt.xlabel('Maximum Depth')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('forest_depth_vs_error.png')
    b7 = []
    b8 = []
    b14 = []
    for l in range(1, 10):
        print(f'Creating the model for minimum samples for leaf b15 = {l}')
        b10 = RandomForestClassifier(n_estimators=200, min_samples_leaf=l, n_jobs=-1)
        print('Fitting the model')
        b10.fit(b3, b2)
        b11 = b10.score(b3, b2)
        b12 = b10.score(b5, b6)
        b8.append(b11)
        b7.append(b12)
        b14.append(l)
        print(f'Min samples per leaf b15: {l}, Training Accuracy: {b11}, Validation Accuracy: {b12}')
    plt.figure()
    plt.plot(b14, b8, b13 = 'Training Accuracy')
    plt.plot(b14, b7, b13 = 'Validation Accuracy')
    plt.xlabel('Minimum Samples per Leaf Node')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig('forest_leaf_nodes_vs_error.png')
    print('Writing predictions')
    with open('forest_submissions.txt', 'w') as f:
        f.write('Id,Prediction\n')
        for it, sample in enumerate(b4, b16 = 1):
            b17 = int(b10.predict(sample.reshape(1, -1))[0])
            f.write(f'{it},{b17}\n')
if b18 = = '__main__':
    fonk1()