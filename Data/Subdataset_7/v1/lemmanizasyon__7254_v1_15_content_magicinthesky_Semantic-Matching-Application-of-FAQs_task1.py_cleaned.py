import nltk
import re
from nltk.corpus import stopwords
def fonk1(b7, b3):
    for word in b7:
        if word not in b3:
            b3[word] = 1
        else:
            b3[word] += 1
    return b3
def fonk2(b11, user_bags):
    b1 = {}
    for faq in b11:
        b1[faq] = []
        for word in user_bags:
            a1 = 0
            if word in b11[faq]:
                a1 = float(user_bags[word] * b11[faq][word]) / sum(b11[faq].values())
            else:
                a1 = 0.0
            b1[faq].append(a1)
    return b1
def fonk3(b10, b11, b9):
    with open("data.txt") as data:
        for line in data:
            b2 = line.rstrip("\n").split("?")
            b10[b2[0]] = b2[1]
    for each in b10:
        b3 = {}
        b4 = b9.sub(' ', each)
        b5 = b9.sub(' ', b10[each])
        b6 = b4.lower() + " " + b5.lower()
        b7 = nltk.word_tokenize(b6)
        b11[each] = fonk1(b7, b3)
def fonk4(b17, user_bow_keys, b11):
    b8 = {}
    for b4 in b17:
        a2 = 0.0
        for i in range(len(user_bow_keys)):
            a3 = 0
            for bow in b11.values():
                if user_bow_keys[i] in bow:
                    a3 += 1
            if a3 != 0:
                a3 = 50.0 / a3
            a2 += b17[b4][i] * a3
        b8[b4] = a2
    return b8
def fonk5(b19, b10):
    a4 = 0
    for each in b19:
        if a4 = = 10:
            break
        print("\n" + each + "? " + str(b18[each]))
        print("" + b10[each])
        print("---")
        a4 += 1
b9 = re.compile('[^a-zA-Z]')
b10 = {}
b11 = {}
b12 = set(stopwords.words('english'))
fonk3(b10, b11, b9)
b13 = input("Enter a FAQ related to TOEFL: ")
b14 = b9.sub(' ', b13)
b15 = nltk.word_tokenize(b14.lower())
b16 = fonk1(b15, {})
b17 = fonk2(b11, b16)
b18 = fonk4(b17, b16.keys(), b11)
b19 = sorted(b18, key = b18.get, reverse = True)
print("\n+++++++++++++++++++++++++++")
print("+Top 10 results for Task 2+")
print("+++++++++++++++++++++++++++")
fonk5(b19, b10)