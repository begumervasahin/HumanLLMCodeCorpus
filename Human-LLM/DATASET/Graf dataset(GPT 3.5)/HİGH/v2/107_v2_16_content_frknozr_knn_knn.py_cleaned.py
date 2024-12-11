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
    b9 = b20.columns.tolist()
    b9.remove("label")
    return b9
def fonk2(b20):
    b9 = fonk1(b20)
    b10 = b20[b9]
    b11 = b20["label"]
    b12 = SelectKBest(score_func=chi2, k=5)
    b12.fit(b10, b11)
    b13 = b12.get_support(indices=True)
    b14 = [b9[i] for i in b13]
    print("[+] Selected b9 -> " + class1.b2 + str(b14) + class1.b6)
    return b20[b14]
def fonk3(b20):
    print(class1.b1 + class1.b8 + "Testing with selected b9" + class1.b6)
    b10 = fonk2(b20)
    b11 = b20["label"]
    X_train, X_test, y_train, b15 = train_test_split(b10, b11, random_state=0)
    b16 = KNeighborsClassifier(n_neighbors=5)
    b17 = time.time()
    b16.fit(X_train, y_train)
    print("[+] Classifier trained in " + class1.b3 + str(time.time() - b17) + class1.b6)
    b17 = time.time()
    b18 = b16.b18(X_test, b15)
    print("[+] Model evaluated in " + class1.b3 + str(time.time() - b17) + class1.b6)
    print("[!] Test b18 is " + class1.b2 + str(b18) + class1.b6)
    print(class1.b7 + class1.b4 + "-------------------------------------------------" + class1.b6)
def fonk4(b20):
    print(class1.b1 + class1.b8 + "Testing with full b20" + class1.b6)
    b10 = b20[fonk1(b20)]
    b11 = b20["label"]
    X_train, X_test, y_train, b15 = train_test_split(b10, b11, random_state=0)
    b16 = KNeighborsClassifier(n_neighbors=5)
    b17 = time.time()
    b16.fit(X_train, y_train)
    print("[+] Classifier trained in " + class1.b3 + str(time.time() - b17) + class1.b6)
    b17 = time.time()
    b18 = b16.b18(X_test, b15)
    print("[+] Model evaluated in " + class1.b3 + str(time.time() - b17) + class1.b6)
    print("[!] Test b18 is " + class1.b2 + str(b18) + class1.b6)
    print(class1.b7 + class1.b4 + "-------------------------------------------------" + class1.b6)
def fonk5():
    b19 = "preprocessed_kddcup_data"
    b20 = pd.read_csv(b19)
    fonk4(b20)
    fonk3(b20)
if b21 = = "__main__":
    fonk5()