import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
model_path = './model/'
input_path = './input/'
output_path = './output/'
with open(input_path + 'linkages.txt') as file:
    L = np.array([[float(digit) for digit in line.split()] for line in file])
y = np.genfromtxt(input_path + 'y.txt')
regression_model = joblib.load(model_path + 'regression_model.sav')
yhat_test = regression_model.predict(L)
score_test = r2_score(y, yhat_test)
print(f'R^2: test={score_test:.3f}')
cindx = np.argsort(y)
csorted = np.sort(y)
yhat_sorted = yhat_test[cindx]
samples = range(len(cindx))
plt.plot(samples, yhat_sorted, marker='o', label='Predicted')
plt.plot(samples, csorted, 'r', label='Actual')
plt.text(5, 20, f'R$^2$={score_test:.3f}', fontsize=20)
plt.legend()
plt.show()
output_data = np.vstack((yhat_sorted, csorted)).T
np.savetxt(output_path + 'output_test.txt', output_data, fmt='%.3f')