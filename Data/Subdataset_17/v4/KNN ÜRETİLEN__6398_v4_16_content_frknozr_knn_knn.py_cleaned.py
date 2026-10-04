import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, chi2
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def get_features(data):
    features = list(data.columns)
    features.remove("label")
    return features
def feature_selection(data):
    features = get_features(data)
    X = data[features]
    y = data["label"]
    selector = SelectKBest(score_func=chi2, k=5)
    selector.fit(X, y)
    selected_features = [features[i] for i in selector.get_support(indices=True)]
    print(f"[+] Selected features -> {bcolors.OKBLUE}{selected_features}{bcolors.ENDC}")
    return data[selected_features]
def with_feature_selection(data):
    print(f"{bcolors.HEADER}{bcolors.UNDERLINE}Testing with selected features{bcolors.ENDC}")
    X = feature_selection(data)
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    knn = KNeighborsClassifier(n_neighbors=5)
    start = time.time()
    knn.fit(X_train, y_train)
    print(f"[+] Classifier trained in {bcolors.OKGREEN}{time.time() - start}{bcolors.ENDC}")
    start = time.time()
    score = knn.score(X_test, y_test)
    print(f"[+] Model evaluated in {bcolors.OKGREEN}{time.time() - start}{bcolors.ENDC}")
    print(f"[!] Test score is {bcolors.OKBLUE}{score}{bcolors.ENDC}")
    print(f"{bcolors.BOLD}{bcolors.WARNING}{'-' * 49}{bcolors.ENDC}")
def with_full_features(data):
    print(f"{bcolors.HEADER}{bcolors.UNDERLINE}Testing with full data{bcolors.ENDC}")
    features = get_features(data)
    X = data[features]
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    knn = KNeighborsClassifier(n_neighbors=5)
    start = time.time()
    knn.fit(X_train, y_train)
    print(f"[+] Classifier trained in {bcolors.OKGREEN}{time.time() - start}{bcolors.ENDC}")
    start = time.time()
    score = knn.score(X_test, y_test)
    print(f"[+] Model evaluated in {bcolors.OKGREEN}{time.time() - start}{bcolors.ENDC}")
    print(f"[!] Test score is {bcolors.OKBLUE}{score}{bcolors.ENDC}")
    print(f"{bcolors.BOLD}{bcolors.WARNING}{'-' * 49}{bcolors.ENDC}")
def test_with_real(data, test_filename):
    X = data[get_features(data)]
    y = data["label"]
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X, y)
    with open(test_filename, "r") as test_file:
        lines = [line.strip().split(",") for line in test_file]
    print(f"Number of test instances: {len(lines)}")
    test_results = [knn.predict([line])[0] for line in lines]
    count_dict = {}
    for result in test_results:
        count_dict[result] = count_dict.get(result, 0) + 1
    print(count_dict)
def main():
    filename = "preprocessed_kddcup_data"
    data = pd.read_csv(filename)
    with_full_features(data)
    with_feature_selection(data)
if __name__ == "__main__":
    main()