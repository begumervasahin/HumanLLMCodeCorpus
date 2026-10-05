import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score as r2
model_path = './model/'
input_path = './input/'
output_path = './output/'
with open(input_path + 'linkages.txt') as file:
    L = np.array([[float(digit) for digit in line.split()] for line in file])
y = np.genfromtxt(input_path + 'y.txt')
regression_model = joblib.load(model_path + 'regression_model.sav')
yhat_test = regression_model.predict(L)
score_test = r2(y, yhat_test)
print('R^2: test=%.3f' % score_test)
yhat_sorted = [yhat_test[i] for i in np.argsort(y)]
csorted = np.sort(y)
samples = range(len(y))
plt.plot(samples, yhat_sorted, marker='o', label='Predicted')
plt.plot(samples, csorted, 'r', label='Actual')
plt.text(5, 20, r'R$^2$='+str('%.3f' % score_test), fontsize=20)
plt.xlabel('Samples')
plt.ylabel('Values')
plt.legend()
plt.show()
np.savetxt(output_path + 'output_test.txt', (yhat_sorted, csorted), fmt='%.3f')