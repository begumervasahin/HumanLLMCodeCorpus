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
def fonk1(b26):
    b9 = list(b26.columns)
    b9.remove("label")
    return b9
def fonk2(b26):
    b9 = fonk1(b26)
    b10 = b26[b9]
    b11 = b26["label"]
    b12 = SelectKBest(score_func=chi2, k=5)
    b12.fit(b10, b11)
    b13 = b12.get_support(indices=True)
    b14 = [b9[i] for i in b13]
    print("[+] Selected b9 -> " + class1.b2 + str(b14) + class1.b6)
    return b26[b14]
def fonk3(b26):
    print(class1.b1 + class1.b8 + "Testing with selected b9" + class1.b6)
    b9 = fonk1(b26)
    b10 = fonk2(b26)
    b11 = b26["label"]
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
def fonk4(b26):
    print(class1.b1 + class1.b8 + "Testing with full b26" + class1.b6)
    b9 = fonk1(b26)
    b10 = b26[b9]
    b11 = b26["label"]
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
def fonk5(b26, test_filename):
    b10 = b26[fonk1(b26)]
    b11 = b26["label"]
    b16 = KNeighborsClassifier(n_neighbors=5)
    b16.fit(b10, b11)
    b19 = open(test_filename, "r")
    b20 = []
    for b21 in b19:
        b21 = b21.strip()
        b22 = b21.split(",")
        b20.append([float(token) for token in b22])
    b19.close()
    print(len(b20))
    b23 = []
    for i in range(len(b20)):
        print(i)
        print(b20[i])
        b23.append(b16.predict([b20[i]])[0])
    b24 = {}
    for i in b23:
        try:
            b24[i] += 1
        except:
            b24[i] = 1
    print(b24)
def fonk6():
    b25 = "preprocessed_kddcup_data.csv"
    b26 = pd.read_csv(b25)
    fonk4(b26)
    fonk3(b26)
if b27 = = "__main__":
    fonk6()