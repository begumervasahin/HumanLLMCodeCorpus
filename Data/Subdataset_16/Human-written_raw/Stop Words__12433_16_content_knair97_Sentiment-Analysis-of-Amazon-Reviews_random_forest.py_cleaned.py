import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
print('Reading training b1')
b1 = np.loadtxt('training_data.txt', skiprows = 1)
b2 = b1[:, 0]
b3 = b1[:, 1:]
print('Reading testing b1')
b4 = np.loadtxt('test_data.txt', skiprows = 1)
b5 = b3[:1000]
b6 = b2[:1000]
b3 = b3[1000:]
b2 = b2[1000:]
b7 = []
b8 = []
b9 = []
for d in range(10, 35):
    print('Creating the model for maximum b9 = %i' % d)
    b10 = RandomForestClassifier(n_estimators = 200, max_depth=d, n_jobs=-1)
    print('Fitting the model')
    b10.fit(b3, b2)
    print('Max b9: ' + str(d))
    print('Training error: ')
    b8.append(b10.score(b3, b2))
    print('Validation error: ')
    b7.append(b10.score(b5, b6))
    b9.append(d)
plt.figure()
plt.plot(b9, b8, b11 = 'Training Accuracy')
plt.plot(b9, b7, b11 = 'Testing Accuracy')
plt.xlabel('Maximum Depth')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('forest_depth_vs_error.png')
b7 = []
b8 = []
b12 = []
for l in range(1, 10):
    print('Creating the model for minimum samples for leaf b13 = %i' % l)
    b10 = RandomForestClassifier(n_estimators = 200,
        b14 = l, n_jobs=-1)
    print('Fitting the model')
    b10.fit(b3, b2)
    print('Training error: ')
    b8.append(b10.score(b3, b2))
    print('Validation error: ')
    b7.append(b10.score(b5, b6))
    b12.append(l)
plt.figure()
plt.plot(b12, b8, b11 = 'Training Error')
plt.plot(b12, b7, b11 = 'Testing Error')
plt.xlabel('Minimum samples per Leaf Node')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('forest_leaf_nodes_vs_error.png')
print('Writing predictions')
with open('forest_submissions.txt', 'w') as f:
    f.write('Id,Prediction\n')
    a1 = 1
    for i in (b4):
        b15 = int(b10.predict(i.reshape(1, -1))[0])
        f.write('%d,%d\n' % (a1, b15))
        a1 += 1
f.close()