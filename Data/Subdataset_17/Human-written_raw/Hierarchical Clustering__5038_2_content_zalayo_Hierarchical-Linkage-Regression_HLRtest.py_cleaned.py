import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score as r2
modelpath = './model/'
inputpath = './input/'
outputpath = './output/'
with open(inputpath + 'linkages.txt') as file:
        L = np.array([[float(digit) for digit in line.split()] for line in file])
y = np.genfromtxt(inputpath + 'y.txt')
regression_model = joblib.load(modelpath + 'regression_model.sav')
yhat_test = regression_model.predict(L)
score_test = r2(y, yhat_test)
print('R^2: test=%.3f' % score_test)
yhat_sorted = list()
cindx = np.argsort(y, axis=-1)
csorted = np.sort(y, axis=-1)
for i in cindx:
    yhat_sorted.append(yhat_test[i])
samples = range(len(cindx))
plt.plot(samples, yhat_sorted, marker = 'o')
plt.plot(samples, csorted, 'r')
plt.text(5, 20, r'R$^2$='+str('%.3f' % score_test), fontsize=20)
plt.show()
np.savetxt(outputpath + 'output_test.txt', (yhat_sorted, csorted), fmt='%.3f')