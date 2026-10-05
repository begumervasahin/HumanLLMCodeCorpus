import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt
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
b7 = StandardScaler()
b3 = b7.fit_transform(b3)
b5 = b7.transform(b5)
b4 = b7.transform(b4)
b8 = TfidfTransformer()
b3 = b8.fit_transform(b3)
b5 = b8.transform(b5)
b4 = b8.transform(b4)
b9 = []
b10 = []
b11 = []
for c in [0.001, 0.01, 0.1, 1, 10, 100]:
    print('Running SVM for b12 = %g' % c)
    b13 = SVC(b12=c, gamma=1, kernel='rbf')
    b13.fit(b3, b2)
    print('Evaluating scores')
    b10.append(b13.score(b3, b2))
    b9.append(b13.score(b5, b6))
    b11.append(c)
plt.plot(b11, b10, b14 = 'Training Accuracy')
plt.plot(b11, b9, b14 = 'Testing Accuracy')
plt.legend()
plt.xlabel('b12 value')
plt.ylabel('Accuracy')
plt.xscale('log')
plt.savefig('svm_c.png')
plt.show()
print('Writing predictions')
b15 = b13.predict(b4)
with open('svm_submissions.txt', 'w') as f:
    f.write('Id,Prediction\n')
    for it, b16 in enumerate(b15, 1):
        b16 = int(b16)
        f.write('%d,%d\n' % (it, b16))
print('Predictions written to svm_submissions.txt')