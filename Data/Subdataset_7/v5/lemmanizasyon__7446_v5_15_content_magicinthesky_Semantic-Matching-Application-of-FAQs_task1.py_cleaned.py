import nltk
import re
from nltk.corpus import stopwords
def fonk1(b6):
    b1 = {}
    for word in b6:
        if word not in b1:
            b1[word] = 1
        else:
            b1[word] += 1
    return b1
def fonk2(b12, user_bags):
    b2 = {}
    for faq in b12:
        b2[faq] = []
        for word in user_bags:
            a1 = 0
            if word in b12[faq]:
                a1 = (user_bags[word] * b12[faq][word]) / sum(b12[faq].values())
            b2[faq].append(a1)
    return b2
def fonk3(file_path, b12, b10):
    with open(file_path) as data:
        for line in data:
            b4, b3 = line.rstrip("\n").split("?")
            b4 = b10.sub(' ', b4)
            b3 = b10.sub(' ', b3)
            b5 = (b4.lower() + " " + b3.lower()).split()
            b6 = nltk.word_tokenize(" ".join(b5))
            b12[b4] = fonk1(b6)
def fonk4(b17, user_bow_keys, b12):
    b7 = {}
    for b4 in b17:
        a2 = 0.0
        for word in user_bow_keys:
            b8 = sum(1 for bow in b12.values() if word in bow)
            if b8 != 0:
                b8 = 50.0 / b8
            a2 += b17[b4][user_bow_keys.index(word)] * b8
        b7[b4] = a2
    return b7
def fonk5(matched_weight_sorted, b11):
    for b9, b4 in enumerate(matched_weight_sorted):
        if b9 = = 10:
            break
        print("\n" + b4 + "? " + str(matched_weight_sorted[b4]))
        print(b11[b4])
        print("---")
b10 = re.compile('[^a-zA-Z]')
b11 = {}
b12 = {}
b13 = set(stopwords.words('english'))
fonk3("data.txt", b12, b10)
b14 = input("Enter a FAQ related to TOEFL: ")
b15 = b10.sub(' ', b14)
b15 = nltk.word_tokenize(b15.lower())
b16 = fonk1(b15)
b17 = fonk2(b12, b16)
b7 = fonk4(b17, b16.keys(), b12)
b18 = dict(sorted(b7.items(), key=lambda item: item[1], reverse=True))
print("\n+++++++++++++++++++++++++++")
print("+ Top 10 results for Task 2 +")
print("+++++++++++++++++++++++++++")
fonk5(b18, b11)