import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score as r2
MODEL_PATH = './model/'
INPUT_PATH = './input/'
OUTPUT_PATH = './output/'
with open(INPUT_PATH + 'linkages.txt') as file:
    linkages = np.array([[float(digit) for digit in line.split()] for line in file])
target_values = np.genfromtxt(INPUT_PATH + 'y.txt')
regression_model = joblib.load(MODEL_PATH + 'regression_model.sav')
predicted_values = regression_model.predict(linkages)
r2_score = r2(target_values, predicted_values)
print(f'R^2: test = {r2_score:.3f}')
sorted_predicted_values = [predicted_values[i] for i in np.argsort(target_values)]
sorted_target_values = np.sort(target_values)
samples = range(len(target_values))
plt.plot(samples, sorted_predicted_values, marker='o', label='Predicted')
plt.plot(samples, sorted_target_values, 'r', label='Actual')
plt.text(5, 20, f'R$^2$={r2_score:.3f}', fontsize=20)
plt.xlabel('Samples')
plt.ylabel('Values')
plt.legend()
plt.show()
np.savetxt(OUTPUT_PATH + 'output_test.txt', (sorted_predicted_values, sorted_target_values), fmt='%.3f')