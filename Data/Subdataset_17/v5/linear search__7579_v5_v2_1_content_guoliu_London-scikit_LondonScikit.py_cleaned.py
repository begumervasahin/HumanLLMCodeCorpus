import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
def load_data(train_path, train_labels_path, test_path):
    x_train = np.loadtxt(train_path, delimiter=",", skiprows=0)
    y_train = np.loadtxt(train_labels_path, delimiter=",", skiprows=0)
    x_test = np.loadtxt(test_path, delimiter=",", skiprows=0)
    return x_train, y_train, x_test
def perform_grid_search(x_train, y_train, param_grid):
    linear_svc = LinearSVC()
    grid_search = GridSearchCV(estimator=linear_svc, param_grid=param_grid, cv=5, verbose=3)
    grid_search.fit(x_train, y_train)
    return grid_search
def display_grid_search_results(grid_search):
    print("Best parameters found:")
    print(grid_search.best_params_)
    print("\nGrid scores:")
    for mean_score, params in zip(grid_search.cv_results_['mean_test_score'], grid_search.cv_results_['params']):
        print(f"{mean_score:.3f} for {params}")
def save_predictions(predictions, output_path):
    output = np.vstack((np.arange(len(predictions)).astype(int) + 1, predictions.astype(int))).T
    np.savetxt(output_path, output, header="Id,Solution", fmt="%d", comments="", delimiter=",")
    print(f"Predictions saved to '{output_path}'.")
def main():
    train_path = "train.csv"
    train_labels_path = "trainLabels.csv"
    test_path = "test.csv"
    output_path = "LinearSVMresult.csv"
    x_train, y_train, x_test = load_data(train_path, train_labels_path, test_path)
    param_grid = {'C': 10.0 ** np.arange(-5, 5)}
    x_train_split, x_val, y_train_split, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)
    grid_search = perform_grid_search(x_train_split, y_train_split, param_grid)
    display_grid_search_results(grid_search)
    best_svc = LinearSVC(C=grid_search.best_params_['C'])
    best_svc.fit(x_train, y_train)
    test_predictions = best_svc.predict(x_test)
    save_predictions(test_predictions, output_path)
if __name__ == "__main__":
    main()