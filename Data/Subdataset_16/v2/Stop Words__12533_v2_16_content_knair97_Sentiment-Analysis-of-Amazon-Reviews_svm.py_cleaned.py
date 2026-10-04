import numpy as np
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfTransformer
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
b7 = TfidfTransformer()
b7.fit(b3)
b3 = b7.transform(b3)
b5 = b7.transform(b5)
b4 = b7.transform(b4)
b8 = []
b9 = []
b10 = []
b11 = [0.001, 0.01, 0.1, 1, 10, 100]
for c in b11:
    print(f'Running SVM for b12 = {c}')
    b13 = SVC(b12=c, gamma=1, kernel='rbf')
    b13.fit(b3, b2)
    b8.append(b13.score(b3, b2))
    b9.append(b13.score(b5, b6))
    b10.append(c)
plt.plot(b10, b8, b14 = 'Training Accuracy')
plt.plot(b10, b9, b14 = 'Testing Accuracy')
plt.legend()
plt.xlabel('b12 value')
plt.ylabel('Accuracy')
plt.xscale('log')
plt.title('SVM Accuracy vs. b12 Value')
plt.savefig('svm_c.png')
plt.show()
print('Writing predictions')
b15 = b13.predict(b4)
with open('svm_submissions.txt', 'w') as f:
    f.write('Id,Prediction\n')
    for idx, pred in enumerate(b15, b16 = 1):
        f.write(f'{idx},{int(pred)}\n')
print('Process completed successfully!')