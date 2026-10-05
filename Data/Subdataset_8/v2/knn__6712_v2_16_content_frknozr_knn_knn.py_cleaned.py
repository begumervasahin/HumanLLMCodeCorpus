import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, chi2
class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def get_features(data):
    features = data.columns.tolist()
    features.remove("label")
    return features
def feature_selection(data):
    features = get_features(data)
    X = data[features]
    y = data["label"]
    selector = SelectKBest(score_func=chi2, k=5)
    selector.fit(X, y)
    indexes_selected = selector.get_support(indices=True)
    selected_features = [features[i] for i in indexes_selected]
    print("[+] Selected features -> " + Color.OKBLUE + str(selected_features) + Color.ENDC)
    return data[selected_features]
def test_with_feature_selection(data):
    print(Color.HEADER + Color.UNDERLINE + "Testing with selected features" + Color.ENDC)
    X = feature_selection(data)
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    knn = KNeighborsClassifier(n_neighbors=5)
    start = time.time()
    knn.fit(X_train, y_train)
    print("[+] Classifier trained in " + Color.OKGREEN + str(time.time() - start) + Color.ENDC)
    start = time.time()
    score = knn.score(X_test, y_test)
    print("[+] Model evaluated in " + Color.OKGREEN + str(time.time() - start) + Color.ENDC)
    print("[!] Test score is " + Color.OKBLUE + str(score) + Color.ENDC)
    print(Color.BOLD + Color.WARNING + "-------------------------------------------------" + Color.ENDC)
def test_with_full_features(data):
    print(Color.HEADER + Color.UNDERLINE + "Testing with full data" + Color.ENDC)
    X = data[get_features(data)]
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    knn = KNeighborsClassifier(n_neighbors=5)
    start = time.time()
    knn.fit(X_train, y_train)
    print("[+] Classifier trained in " + Color.OKGREEN + str(time.time() - start) + Color.ENDC)
    start = time.time()
    score = knn.score(X_test, y_test)
    print("[+] Model evaluated in " + Color.OKGREEN + str(time.time() - start) + Color.ENDC)
    print("[!] Test score is " + Color.OKBLUE + str(score) + Color.ENDC)
    print(Color.BOLD + Color.WARNING + "-------------------------------------------------" + Color.ENDC)
def main():
    filename = "preprocessed_kddcup_data"
    data = pd.read_csv(filename)
    test_with_full_features(data)
    test_with_feature_selection(data)
if __name__ == "__main__":
    main()