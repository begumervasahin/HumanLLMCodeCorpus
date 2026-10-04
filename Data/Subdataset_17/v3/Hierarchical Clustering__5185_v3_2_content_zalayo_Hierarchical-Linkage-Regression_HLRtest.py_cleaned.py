import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
model_path = './model/'
input_path = './input/'
output_path = './output/'
def load_linkage_data(file_path):
    with open(file_path) as file:
        return np.array([[float(value) for value in line.split()] for line in file])
def load_target_values(file_path):
    return np.genfromtxt(file_path)
def load_model(file_path):
    return joblib.load(file_path)
def predict_values(model, data):
    return model.predict(data)
def calculate_r2_score(true_values, predicted_values):
    return r2_score(true_values, predicted_values)
def sort_values_indices(values, predicted_values):
    sorted_indices = np.argsort(values)
    sorted_values = values[sorted_indices]
    sorted_predictions = predicted_values[sorted_indices]
    return sorted_indices, sorted_values, sorted_predictions
def plot_results(indices, sorted_predictions, sorted_values, r2_score_test):
    plt.figure(figsize=(10, 6))
    plt.plot(indices, sorted_predictions, marker='o', linestyle='-', label='Predicted Values')
    plt.plot(indices, sorted_values, color='red', linestyle='-', label='Actual Values')
    plt.text(5, 20, f'R$^2$ = {r2_score_test:.3f}', fontsize=20)
    plt.legend()
    plt.title('Predicted vs Actual Values')
    plt.xlabel('Sample Index')
    plt.ylabel('Values')
    plt.grid(True)
    plt.show()
def save_output_data(file_path, sorted_predictions, sorted_values):
    output_data = np.column_stack((sorted_predictions, sorted_values))
    np.savetxt(file_path, output_data, fmt='%.3f')
def main():
    linkage_data = load_linkage_data(input_path + 'linkages.txt')
    target_values = load_target_values(input_path + 'y.txt')
    regression_model = load_model(model_path + 'regression_model.sav')
    predicted_values = predict_values(regression_model, linkage_data)
    r2_score_test = calculate_r2_score(target_values, predicted_values)
    print(f'R^2 Score: {r2_score_test:.3f}')
    sorted_indices, sorted_targets, sorted_predictions = sort_values_indices(target_values, predicted_values)
    plot_results(sorted_indices, sorted_predictions, sorted_targets, r2_score_test)
    save_output_data(output_path + 'output_test.txt', sorted_predictions, sorted_targets)
if __name__ == "__main__":
    main()