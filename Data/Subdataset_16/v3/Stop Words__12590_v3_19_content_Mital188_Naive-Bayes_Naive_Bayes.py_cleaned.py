import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import sys
def fonk1(filenames, b1 = False):
    b2 = ""
    for filename in filenames:
        with open(filename, 'r') as file:
            b2 += file.read()
    b3 = str.maketrans('', '', string.punctuation + string.digits)
    b4 = b2.translate(b3)
    b5 = Counter(b4.split())
    if b1:
        b6 = set(stopwords.words('english'))
        b5 = Counter([word for word in b5 if word not in b6])
    return b5
def fonk2(b5):
    b7 = sum(b5.values())
    return {word: count / b7 for word, count in b5.items()}
def fonk3(b5, b12):
    return {word: b5.get(word, 0) / (b12.get(word, 0) + len(b12)) for word in b12}
def fonk4(test_files, b14, b15, b12):
    a1 = 0
    a2 = 0
    for filename in test_files:
        with open(filename, 'r') as file:
            b8 = file.read()
        b9 = Counter(b8.split())
        a3 = 1.0
        a4 = 1.0
        for word in b9:
            if word in b12:
                a3 *= b14.get(word, 1)
                a4 *= b15.get(word, 1)
        if a3 + a4 > 0:
            if a3 / (a3 + a4) > 0.5:
                a1 += 1
            else:
                a2 += 1
    return a1, a2
def fonk5(train_ham, train_spam, b12):
    for word in b12:
        train_ham[word] += 1
        train_spam[word] += 1
    return train_ham, train_spam
def fonk6(ham_train, spam_train, ham_test, spam_test, b1):
    b10 = fonk1(ham_train, b1)
    b11 = fonk1(spam_train, b1)
    b12 = b10 + b11
    smoothed_ham_counts, b13 = fonk5(b10, b11, b12)
    b14 = fonk3(smoothed_ham_counts, b12)
    b15 = fonk3(b13, b12)
    a1, a2 = fonk4(ham_test, b14, b15, b12)
    b16 = a1 / len(ham_test) if ham_test else 0
    b17 = a2 / len(spam_test) if spam_test else 0
    print(f"Ham Accuracy: {b16:.2f}")
    print(f"Spam Accuracy: {b17:.2f}")
if b18 = = "__main__":
    b19 = glob.glob(sys.argv[1] + "/*.txt")
    b20 = glob.glob(sys.argv[2] + "/*.txt")
    b21 = glob.glob(sys.argv[3] + "/*.txt")
    b22 = glob.glob(sys.argv[4] + "/*.txt")
    b23 = float(sys.argv[5])
    b24 = int(sys.argv[6])
    b25 = float(sys.argv[7])
    print("Evaluating without stopword removal:")
    fonk6(b19, b20, b21, b22, b1 = False)
    print("\nEvaluating with stopword removal:")
    fonk6(b19, b20, b21, b22, b1 = True)