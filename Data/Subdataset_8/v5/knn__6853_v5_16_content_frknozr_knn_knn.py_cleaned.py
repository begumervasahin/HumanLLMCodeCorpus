import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, chi2
class TextColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def get_features(data):
    return [col for col in data.columns if col != "label"]
def feature_selection(data):
    X = data[get_features(data)]
    y = data["label"]
    selector = SelectKBest(score_func=chi2, k=5)
    selector.fit(X, y)
    selected_features = X.columns[selector.get_support()]
    print("[+] Selected features -> " + TextColors.OKBLUE + str(selected_features.tolist()) + TextColors.ENDC)
    return data[selected_features]
def test_classifier(knn, X_test, y_test):
    start = time.time()
    knn.fit(X_train, y_train)
    print("[+] Classifier trained in " + TextColors.OKGREEN + f"{time.time() - start:.2f}" + TextColors.ENDC)
    start = time.time()
    score = knn.score(X_test, y_test)
    print("[+] Model evaluated in " + TextColors.OKGREEN + f"{time.time() - start:.2f}" + TextColors.ENDC)
    print("[!] Test score is " + TextColors.OKBLUE + f"{score:.4f}" + TextColors.ENDC)
    print(TextColors.BOLD + TextColors.WARNING + "-------------------------------------------------" + TextColors.ENDC)
def test_with_real_data(data, test_filename):
    X = data[get_features(data)]
    y = data["label"]
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X, y)
    with open(test_filename, "r") as test_file:
        lines = [line.strip().split(",") for line in test_file]
    print(len(lines))
    test_results = []
    for i, line in enumerate(lines):
        print(i)
        print(line)
        test_results.append(knn.predict([line]))
    count_dict = {}
    for result in test_results:
        count_dict[result[0]] = count_dict.get(result[0], 0) + 1
    print(count_dict)
def main():
    filename = "preprocessed_kddcup_data"
    data = pd.read_csv(filename)
    print(TextColors.HEADER + TextColors.UNDERLINE + "Testing with full data" + TextColors.ENDC)
    X = data[get_features(data)]
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    knn = KNeighborsClassifier(n_neighbors=5)
    test_classifier(knn, X_test, y_test)
    print(TextColors.HEADER + TextColors.UNDERLINE + "Testing with selected features" + TextColors.ENDC)
    data_selected = feature_selection(data)
    X = data_selected[get_features(data_selected)]
    y = data_selected["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    knn = KNeighborsClassifier(n_neighbors=5)
    test_classifier(knn, X_test, y_test)
if __name__ == "__main__":
    main()