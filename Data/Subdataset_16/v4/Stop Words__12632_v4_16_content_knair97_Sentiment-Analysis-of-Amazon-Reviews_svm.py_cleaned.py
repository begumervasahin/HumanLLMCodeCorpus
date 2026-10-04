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
b4 = np.loadtxt('b4.txt', skiprows=1)
b5 = b3[:1000]
b6 = b2[:1000]
b3 = b3[1000:]
b2 = b2[1000:]
b7 = TfidfTransformer()
b7.fit(b3)
b3 = b7.transform(b3)
b5 = b7.transform(b5)
b4 = b7.transform(b4)
b8 = []
b9 = []
b10 = [0.001, 0.01, 0.1, 1, 10, 100]
for c in b10:
    print(f'Running SVM for b11 = {c}')
    b12 = SVC(b11=c, gamma=1, kernel='rbf')
    b12.fit(b3, b2)
    b8.append(b12.score(b3, b2))
    b9.append(b12.score(b5, b6))
plt.plot(b10, b8, b13 = 'Training Accuracy')
plt.plot(b10, b9, b13 = 'Testing Accuracy')
plt.legend()
plt.xlabel('b11 value')
plt.ylabel('Accuracy')
plt.xscale('log')
plt.savefig('svm_c.png')
print('Writing b14')
b14 = b12.predict(b4)
with open('svm_submissions.txt', 'w') as f:
    f.write('Id,Prediction\n')
    for idx, pred in enumerate(b14, b15 = 1):
        f.write(f'{idx},{int(pred)}\n')
print('Done')