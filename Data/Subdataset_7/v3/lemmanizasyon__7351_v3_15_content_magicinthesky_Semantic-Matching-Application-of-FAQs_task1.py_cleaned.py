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
def fonk2(bags_dict, user_bags):
    b1 = {}
    for faq, faq_bow in bags_dict.items():
        b1[faq] = []
        for word in user_bags:
            a1 = 0
            if word in faq_bow:
                a1 = float(user_bags[word] * faq_bow[word]) / sum(faq_bow.values())
            b1[faq].append(a1)
    return b1
def fonk3(table, bags_dict, b10):
    with open("data.txt") as data_file:
        for line in data_file:
            question, b2 = line.rstrip("\n").split("?")
            table[question] = b2
    for question, b2 in table.items():
        b3 = {}
        b4 = b10.sub(' ', question).lower()
        b5 = b10.sub(' ', b2).lower()
        b6 = b4 + " " + b5
        b7 = nltk.word_tokenize(b6)
        bags_dict[question] = fonk1(b7, b3)
def fonk4(b1, user_bow_keys, bags_dict):
    b8 = {}
    for faq, weights in b1.items():
        a2 = 0.0
        for i, word in enumerate(user_bow_keys):
            b9 = sum(1 for bow in bags_dict.values() if word in bow)
            if b9:
                b9 = 50.0 / b9
            a2 += weights[i] * b9
        b8[faq] = a2
    return b8
def fonk5(b18, b11):
    for faq in b18[:10]:
        print("\nQuestion: " + faq + "\nMatching Score: " + str(b17[faq]))
        print("Answer: " + b11[faq])
        print("---")
b10 = re.compile('[^a-zA-Z]')
b11 = {}
b12 = {}
fonk3(b11, b12, b10)
b13 = input("Enter a FAQ related to TOEFL: ")
b14 = b10.sub(' ', b13).lower()
b15 = fonk1(nltk.word_tokenize(b14), {})
b16 = fonk2(b12, b15)
b17 = fonk4(b16, b15.keys(), b12)
b18 = sorted(b17, key=b17.get, reverse=True)
print("\n+++++++++++++++++++++++++++")
print("+Top 10 results for Task 2+")
print("+++++++++++++++++++++++++++")
fonk5(b18, b11)