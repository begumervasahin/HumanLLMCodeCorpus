import numpy as np
import joblib
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
MODEL_PATH = './model/regression_model.sav'
LINKAGE_FILE_PATH = './input/linkages.txt'
TARGET_FILE_PATH = './input/y.txt'
OUTPUT_FILE_PATH = './output/output_test.txt'
def load_linkage_data(file_path):
    with open(file_path) as file:
        linkage_data = [list(map(float, line.split())) for line in file]
    return np.array(linkage_data)
def load_target_values(file_path):
    return np.genfromtxt(file_path)
def load_model(model_path):
    return joblib.load(model_path)
def predict_values(model, data):
    return model.predict(data)
def evaluate_r2_score(true_values, predicted_values):
    return r2_score(true_values, predicted_values)
def sort_values(true_values, predicted_values):
    sorted_indices = np.argsort(true_values)
    sorted_true_values = true_values[sorted_indices]
    sorted_predicted_values = predicted_values[sorted_indices]
    return sorted_true_values, sorted_predicted_values
def plot_sorted_values(sorted_true_values, sorted_predicted_values, r2_score_value):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(sorted_true_values)), sorted_predicted_values, marker='o', label='Predicted')
    plt.plot(range(len(sorted_true_values)), sorted_true_values, 'r', label='Actual')
    plt.text(5, 20, f'R$^2$ = {r2_score_value:.3f}', fontsize=20)
    plt.legend()
    plt.title('Predicted vs Actual Values')
    plt.xlabel('Sample Index')
    plt.ylabel('Values')
    plt.grid(True)
    plt.show()
def save_sorted_results(output_path, sorted_predicted_values, sorted_true_values):
    output_data = np.column_stack((sorted_predicted_values, sorted_true_values))
    np.savetxt(output_path, output_data, fmt='%.3f')
def main():
    linkage_data = load_linkage_data(LINKAGE_FILE_PATH)
    true_values = load_target_values(TARGET_FILE_PATH)
    model = load_model(MODEL_PATH)
    predicted_values = predict_values(model, linkage_data)
    r2_score_value = evaluate_r2_score(true_values, predicted_values)
    print(f'R^2 Score: {r2_score_value:.3f}')
    sorted_true_values, sorted_predicted_values = sort_values(true_values, predicted_values)
    plot_sorted_values(sorted_true_values, sorted_predicted_values, r2_score_value)
    save_sorted_results(OUTPUT_FILE_PATH, sorted_predicted_values, sorted_true_values)
if __name__ == "__main__":
    main()