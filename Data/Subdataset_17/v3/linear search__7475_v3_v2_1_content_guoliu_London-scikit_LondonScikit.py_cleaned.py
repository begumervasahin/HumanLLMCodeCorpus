import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
def load_data(train_file, train_labels_file, test_file):
    x_train = np.loadtxt(open(train_file, "rb"), delimiter=",", skiprows=0)
    y_train = np.loadtxt(open(train_labels_file, "rb"), delimiter=",", skiprows=0)
    x_test = np.loadtxt(open(test_file, "rb"), delimiter=",", skiprows=0)
    return x_train, y_train, x_test
def tune_hyperparameters(x_train_split, y_train_split):
    tuned_parameters = {'C': 10. ** np.arange(-5, 5)}
    classifier = LinearSVC()
    grid_search = GridSearchCV(classifier, tuned_parameters, cv=5, verbose=3)
    grid_search.fit(x_train_split, y_train_split)
    return grid_search
def display_best_params(grid_search):
    print("Best parameters found:")
    print(grid_search.best_params_)
def display_grid_scores(grid_search):
    print("\nGrid scores:")
    for mean_score, params in zip(grid_search.cv_results_['mean_test_score'], grid_search.cv_results_['params']):
        print(f"{mean_score:.3f} (+/-{grid_search.cv_results_['std_test_score'][0] * 2:.03f}) for {params}")
def train_best_model(x_train, y_train, best_params):
    best_classifier = LinearSVC(C=best_params['C'])
    best_classifier.fit(x_train, y_train)
    return best_classifier
def save_predictions(predictions, output_file):
    output = np.vstack((np.arange(len(predictions)).astype(int) + 1, predictions.astype(int))).T
    np.savetxt(output_file, output, header="Id,Solution", fmt="%d", comments="", delimiter=",")
def main():
    x_train, y_train, x_test = load_data("train.csv", "trainLabels.csv", "test.csv")
    x_train_split, x_val, y_train_split, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)
    grid_search = tune_hyperparameters(x_train_split, y_train_split)
    display_best_params(grid_search)
    display_grid_scores(grid_search)
    best_classifier = train_best_model(x_train, y_train, grid_search.best_params_)
    predictions = best_classifier.predict(x_test)
    save_predictions(predictions, "LinearSVMresult.csv")
if __name__ == "__main__":
    main()