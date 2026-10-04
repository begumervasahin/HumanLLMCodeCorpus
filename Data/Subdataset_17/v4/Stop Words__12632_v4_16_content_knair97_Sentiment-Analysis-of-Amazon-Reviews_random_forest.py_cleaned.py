import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
print('Reading training data')
data = np.loadtxt('training_data.txt', skiprows=1)
y_train = data[:, 0]
x_train = data[:, 1:]
print('Reading testing data')
x_test = np.loadtxt('test_data.txt', skiprows=1)
x_val = x_train[:1000]
y_val = y_train[:1000]
x_train = x_train[1000:]
y_train = y_train[1000:]
val_err = []
train_err = []
depth = []
for d in range(10, 35):
    print(f'Creating the model for maximum depth = {d}')
    clf = RandomForestClassifier(n_estimators=200, max_depth=d, n_jobs=-1)
    print('Fitting the model')
    clf.fit(x_train, y_train)
    train_accuracy = clf.score(x_train, y_train)
    val_accuracy = clf.score(x_val, y_val)
    print(f'Max depth: {d}')
    print(f'Training accuracy: {train_accuracy}')
    print(f'Validation accuracy: {val_accuracy}')
    train_err.append(train_accuracy)
    val_err.append(val_accuracy)
    depth.append(d)
plt.figure()
plt.plot(depth, train_err, label='Training Accuracy')
plt.plot(depth, val_err, label='Validation Accuracy')
plt.xlabel('Maximum Depth')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('forest_depth_vs_error.png')
val_err = []
train_err = []
leaf_nodes = []
for l in range(1, 10):
    print(f'Creating the model for minimum samples per leaf node = {l}')
    clf = RandomForestClassifier(n_estimators=200, min_samples_leaf=l, n_jobs=-1)
    print('Fitting the model')
    clf.fit(x_train, y_train)
    train_accuracy = clf.score(x_train, y_train)
    val_accuracy = clf.score(x_val, y_val)
    print(f'Minimum samples per leaf node: {l}')
    print(f'Training accuracy: {train_accuracy}')
    print(f'Validation accuracy: {val_accuracy}')
    train_err.append(train_accuracy)
    val_err.append(val_accuracy)
    leaf_nodes.append(l)
plt.figure()
plt.plot(leaf_nodes, train_err, label='Training Accuracy')
plt.plot(leaf_nodes, val_err, label='Validation Accuracy')
plt.xlabel('Minimum Samples per Leaf Node')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('forest_leaf_nodes_vs_error.png')
print('Writing predictions')
with open('forest_submissions.txt', 'w') as f:
    f.write('Id,Prediction\n')
    for it, i in enumerate(x_test, start=1):
        pred = int(clf.predict(i.reshape(1, -1))[0])
        f.write(f'{it},{pred}\n')
print('Process completed.')