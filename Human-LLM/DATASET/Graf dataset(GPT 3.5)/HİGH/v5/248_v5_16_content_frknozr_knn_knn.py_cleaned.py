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
def fonk1(b20):
    return [col for col in b20.columns if col != "label"]
def fonk2(b20):
    b9 = b20[fonk1(b20)]
    b10 = b20["label"]
    b11 = SelectKBest(score_func=chi2, k=5)
    b11.fit(b9, b10)
    b12 = b9.columns[b11.get_support()]
    print("[+] Selected features -> " + class1.b2 + str(b12.tolist()) + class1.b6)
    return b20[b12]
def fonk3(b15, X_test, b21):
    b13 = time.time()
    b15.fit(X_train, y_train)
    print("[+] Classifier trained in " + class1.b3 + f"{time.time() - b13:.2f}" + class1.b6)
    b13 = time.time()
    b14 = b15.b14(X_test, b21)
    print("[+] Model evaluated in " + class1.b3 + f"{time.time() - b13:.2f}" + class1.b6)
    print("[!] Test b14 is " + class1.b2 + f"{b14:.4f}" + class1.b6)
    print(class1.b7 + class1.b4 + "-------------------------------------------------" + class1.b6)
def fonk4(b20, test_filename):
    b9 = b20[fonk1(b20)]
    b10 = b20["label"]
    b15 = KNeighborsClassifier(n_neighbors=5)
    b15.fit(b9, b10)
    with open(test_filename, "r") as test_file:
        b16 = [line.strip().split(",") for line in test_file]
    print(len(b16))
    b17 = []
    for i, line in enumerate(b16):
        print(i)
        print(line)
        b17.append(b15.predict([line]))
    b18 = {}
    for result in b17:
        b18[result[0]] = b18.get(result[0], 0) + 1
    print(b18)
def fonk5():
    b19 = "preprocessed_kddcup_data"
    b20 = pd.read_csv(b19)
    print(class1.b1 + class1.b8 + "Testing with full b20" + class1.b6)
    b9 = b20[fonk1(b20)]
    b10 = b20["label"]
    X_train, X_test, y_train, b21 = train_test_split(b9, b10, random_state=0)
    b15 = KNeighborsClassifier(n_neighbors=5)
    fonk3(b15, X_test, b21)
    print(class1.b1 + class1.b8 + "Testing with selected features" + class1.b6)
    b22 = fonk2(b20)
    b9 = b22[fonk1(b22)]
    b10 = b22["label"]
    X_train, X_test, y_train, b21 = train_test_split(b9, b10, random_state=0)
    b15 = KNeighborsClassifier(n_neighbors=5)
    fonk3(b15, X_test, b21)
if b23 = = "__main__":
    fonk5()