import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
model_path = './model/'
input_path = './input/'
output_path = './output/'
with open(input_path + 'linkages.txt') as file:
    linkage_data = np.array([[float(value) for value in line.split()] for line in file])
target_values = np.genfromtxt(input_path + 'y.txt')
regression_model = joblib.load(model_path + 'regression_model.sav')
predicted_values = regression_model.predict(linkage_data)
r2_score_test = r2_score(target_values, predicted_values)
print(f'R^2 Score: {r2_score_test:.3f}')
sorted_indices = np.argsort(target_values)
sorted_targets = target_values[sorted_indices]
sorted_predictions = predicted_values[sorted_indices]
plt.figure(figsize=(10, 6))
plt.plot(sorted_indices, sorted_predictions, marker='o', linestyle='-', label='Predicted Values')
plt.plot(sorted_indices, sorted_targets, color='red', linestyle='-', label='Actual Values')
plt.text(5, 20, f'R$^2$ = {r2_score_test:.3f}', fontsize=20)
plt.legend()
plt.title('Predicted vs Actual Values')
plt.xlabel('Sample Index')
plt.ylabel('Values')
plt.grid(True)
plt.show()
output_data = np.column_stack((sorted_predictions, sorted_targets))
np.savetxt(output_path + 'output_test.txt', output_data, fmt='%.3f')