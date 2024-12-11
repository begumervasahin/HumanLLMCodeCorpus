import re
import random
import math
from collections import Counter, OrderedDict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
b1 = "raw_data_sport.txt"
b2 = "raw_data_politics.txt"
b3 = {}
b4 = {}
def fonk1(b10, percent):
    b5 = b10.split()
    b6 = len(b5)
    b7 = int(b6 * percent)
    b8 = b5[:b7]
    b9 = b5[b7:]
    return ' '.join(b8), ' '.join(b9)
def fonk2(b10):
    b10 = b10.lower()
    b10 = re.sub(r'\d+', '', b10)
    b10 = b10.replace("\n", " ")
    b10 = b10.replace("-", "")
    b11 = set(stopwords.b5('english'))
    for word in b11:
        b10 = b10.replace(" " + word + " ", " ")
    return b10
def fonk3(b10, b30, b31, b26, b27, b28, b29, class1_words, b25):
    b10 = fonk2(b10)
    b5 = b10.split()
    b12 = b30
    b13 = b31
    a1 = 0
    a2 = 0
    for word in b5:
        if len(word) < 3:
            continue
        b14 = fonk4(word, b26, b28, class1_words)
        if b14 > a1:
            a1 = b14
            b3[word] = b14
        b15 = fonk4(word, b27, b29, b25)
        if b15 > a2:
            a2 = b15
            b4[word] = b15
        b12 += b14
        b13 += b15
    if b12 > b13:
        return class1
    else:
        return class2
def fonk4(word, count_all_words, count_dist_words, class_words):
    if word in class_words:
        return math.log10((class_words[word] + class1) / (count_dist_words + count_all_words))
    else:
        return math.log10(class1 / (count_dist_words + count_all_words))
def fonk5(train1, train2):
    b16 = Counter(train1.split())
    b17 = Counter(train2.split())
    return b16, b17
def fonk6(b5):
    a3 = 50
    b18 = [b5[i:i + a3] for i in range(0, len(b5), a3)]
    return [' '.join(chunk) for chunk in b18]
def fonk7():
    b19 = open(b1).read()
    b20 = open(b2).read()
    b19 = b19.lower().replace("\n", " ")
    b20 = b20.lower().replace("\n", " ")
    train1, b21 = fonk1(b19, 0.10)
    train2, b22 = fonk1(b20, 0.10)
    b23 = sum(Counter(re.split(r'[.!?]', train1)).values())
    b24 = sum(Counter(re.split(r'[.!?]', train2)).values())
    class1_words, b25 = fonk5(train1, train2)
    b26 = sum(class1_words.values())
    b27 = sum(b25.values())
    b28 = len(class1_words)
    b29 = len(b25)
    b30 = b23 / (b23 + b24)
    b31 = b24 / (b23 + b24)
    b32 = fonk6(b21.split())
    b33 = fonk6(b22.split())
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    for sentence in b32:
        b34 = fonk3(sentence, b30, b31, b26, b27, b28, b29, class1_words, b25)
        if b34 = = class1:
            a4 += class1
        else:
            a5 += class1
    for sentence in b33:
        b34 = fonk3(sentence, b30, b31, b26, b27, b28, b29, class1_words, b25)
        if b34 = = class2:
            a7 += class1
        else:
            a6 += class1
    b35 = a4 / (a4 + a6)
    b36 = a4 / (a4 + a5)
    print("Precision:", b35)
    print("Recall:", b36)
    print("Important b5 in class class1:", OrderedDict(sorted(b3.items(), b37 = lambda x: x[class1], reverse=True)))
    print("Important b5 in class class2:", OrderedDict(sorted(b4.items(), b37 = lambda x: x[class1], reverse=True)))
fonk7()