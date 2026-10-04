import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, chi2
class class1:
    b1 = '\033[95m'
    b2 = '\033[94m'
    b3 = '\033[92m'
    b4 = '\033[93m'
    b5 = '\033[91m'
    b6 = '\033[0m'
    b7 = '\033[1m'
    b8 = '\033[4m'
def fonk1(b22):
    b9 = list(b22.columns)
    b9.remove("label")
    return b9
def fonk2(b22):
    b9 = fonk1(b22)
    b10 = b22[b9]
    b11 = b22["label"]
    b12 = SelectKBest(score_func=chi2, k=5)
    b12.fit(b10, b11)
    b13 = [b9[i] for i in b12.get_support(indices=True)]
    print(f"[+] Selected b9 -> {class1.b2}{b13}{class1.b6}")
    return b22[b13]
def fonk3(b10, b11):
    X_train, X_test, y_train, b14 = train_test_split(b10, b11, random_state=0)
    b15 = KNeighborsClassifier(n_neighbors=5)
    b16 = time.time()
    b15.fit(X_train, y_train)
    print(f"[+] Classifier trained in {class1.b3}{time.time() - b16:.4f}{class1.b6} seconds")
    b16 = time.time()
    b17 = b15.b17(X_test, b14)
    print(f"[+] Model evaluated in {class1.b3}{time.time() - b16:.4f}{class1.b6} seconds")
    print(f"[!] Test b17 is {class1.b2}{b17:.4f}{class1.b6}")
    print(f"{class1.b7}{class1.b4}{'-' * 49}{class1.b6}")
def fonk4(b22):
    print(f"{class1.b1}{class1.b8}Testing with selected b9{class1.b6}")
    b10 = fonk2(b22)
    b11 = b22["label"]
    fonk3(b10, b11)
def fonk5(b22):
    print(f"{class1.b1}{class1.b8}Testing with full b22{class1.b6}")
    b9 = fonk1(b22)
    b10 = b22[b9]
    b11 = b22["label"]
    fonk3(b10, b11)
def fonk6(b22, test_filename):
    b10 = b22[fonk1(b22)]
    b11 = b22["label"]
    b15 = KNeighborsClassifier(n_neighbors=5)
    b15.fit(b10, b11)
    with open(test_filename, "r") as test_file:
        b18 = [line.strip().split(",") for line in test_file]
    print(f"Number of test instances: {len(b18)}")
    b19 = [b15.predict([line])[0] for line in b18]
    b20 = {}
    for result in b19:
        b20[result] = b20.get(result, 0) + 1
    print(b20)
def fonk7():
    b21 = "preprocessed_kddcup_data"
    b22 = pd.read_csv(b21)
    fonk5(b22)
    fonk4(b22)
if b23 = = "__main__":
    fonk7()