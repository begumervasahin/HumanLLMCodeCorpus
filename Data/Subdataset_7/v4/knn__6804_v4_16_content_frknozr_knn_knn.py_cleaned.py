import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
class class1:
    b1 = '\033[95m'
    b2 = '\033[94m'
    b3 = '\033[92m'
    b4 = '\033[93m'
    b5 = '\033[91m'
    b6 = '\033[0m'
    b7 = '\033[1m'
    b8 = '\033[4m'
def fonk1(b23):
    b9 = list(b23.columns)
    b9.remove("label")
    return b9
def fonk2(b23):
    from sklearn.feature_selection import SelectKBest, chi2
    b9 = fonk1(b23)
    b10 = b23[b9]
    b11 = b23["label"]
    b12 = SelectKBest(score_func=chi2, k=5)
    b12.fit(b10, b11)
    b13 = b12.get_support(indices=True)
    b14 = [b9[i] for i in b13]
    print("[+] Selected b9 -> " + class1.b2 + str(b14) + class1.b6)
    return b23[b14]
def fonk3(b23):
    print(class1.b1 + class1.b8 + "Testing with selected b9" + class1.b6)
    b10 = fonk2(b23)
    b11 = b23["label"]
    X_train, X_test, y_train, b15 = train_test_split(b10, b11, random_state=0)
    b16 = KNeighborsClassifier(n_neighbors=5)
    b17 = time.time()
    b16.fit(X_train, y_train)
    print("[+] Classifier trained in " + class1.b3 + str(time.time() - b17) + class1.b6)
    b17 = time.time()
    b18 = b16.b18(X_test, b15)
    print("[+] Model Evaluated in " + class1.b3 + str(time.time() - b17) + class1.b6)
    print("[!] Test b18 is " + class1.b2 + str(b18) + class1.b6)
    print(class1.b7 + class1.b4 + "-------------------------------------------------" + class1.b6)
def fonk4(b23):
    print(class1.b1 + class1.b8 + "Testing with full b23" + class1.b6)
    b10 = b23[fonk1(b23)]
    b11 = b23["label"]
    X_train, X_test, y_train, b15 = train_test_split(b10, b11, random_state=0)
    b16 = KNeighborsClassifier(n_neighbors=5)
    b17 = time.time()
    b16.fit(X_train, y_train)
    print("[+] Classifier trained in " + class1.b3 + str(time.time() - b17) + class1.b6)
    b17 = time.time()
    b18 = b16.b18(X_test, b15)
    print("[+] Model Evaluated in " + class1.b3 + str(time.time() - b17) + class1.b6)
    print("[!] Test b18 is " + class1.b2 + str(b18) + class1.b6)
    print(class1.b7 + class1.b4 + "-------------------------------------------------" + class1.b6)
def fonk5(b23, test_filename):
    b10 = b23[fonk1(b23)]
    b11 = b23["label"]
    b16 = KNeighborsClassifier(n_neighbors=5)
    b16.fit(b10, b11)
    with open(test_filename, "r") as test_file:
        b19 = [line.strip().split(",") for line in test_file]
    print(len(b19))
    b20 = []
    for i, line in enumerate(b19):
        print(i)
        print(line)
        b20.append(b16.predict([line]))
    b21 = {}
    for result in b20:
        try:
            b21[result[0]] += 1
        except KeyError:
            b21[result[0]] = 1
    print(b21)
def fonk6():
    b22 = "preprocessed_kddcup_data"
    b23 = pd.read_csv(b22)
    fonk4(b23)
    fonk3(b23)
if b24 = = "__main__":
    fonk6()