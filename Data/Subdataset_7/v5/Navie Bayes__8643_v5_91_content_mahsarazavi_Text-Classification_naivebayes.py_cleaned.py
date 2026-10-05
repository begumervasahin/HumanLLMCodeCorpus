import re
import math
from collections import Counter, OrderedDict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
b1 = "raw_data_sport.txt"
b2 = "raw_data_politics.txt"
def fonk1(b7, percent):
    b3 = b7.split()
    b4 = int(len(b3) * percent)
    b5 = ' '.join(b3[:b4])
    b6 = ' '.join(b3[b4:])
    return b5, b6
def fonk2(b7):
    b7 = b7.lower()
    b7 = re.sub(r'\d+', '', b7)
    b7 = b7.replace("\n", " ")
    b7 = b7.replace("-", "")
    b8 = set(stopwords.b3('english'))
    for word in b8:
        b7 = b7.replace(" " + word + " ", " ")
    return b7
def fonk3(word, count_all_words, count_dist_words, class_words):
    if word in class_words:
        return math.log10((class_words[word] + class1) / (count_dist_words + count_all_words))
    else:
        return math.log10(class1 / (count_dist_words + count_all_words))
def fonk4(b7):
    return Counter(b7.split())
def fonk5(b7, n):
    b9 = [b7[i:i + n] for i in range(0, len(b7), n)]
    return [' '.join(chunk) for chunk in b9]
def fonk6():
    b10 = open(b1).read()
    b11 = open(b2).read()
    b10 = b10.lower().replace("\n", " ")
    b11 = b11.lower().replace("\n", " ")
    train1, b12 = fonk1(b10, 0.10)
    train2, b13 = fonk1(b11, 0.10)
    b14 = fonk4(train1)
    b15 = fonk4(train2)
    b16 = sum(b14.values())
    b17 = sum(b15.values())
    b18 = len(b14)
    b19 = len(b15)
    b20 = len(re.split(r'[.!?]', train1)) / (len(re.split(r'[.!?]', train1)) + len(re.split(r'[.!?]', train2)))
    b21 = len(re.split(r'[.!?]', train2)) / (len(re.split(r'[.!?]', train1)) + len(re.split(r'[.!?]', train2)))
    b22 = fonk5(b12, 50)
    b23 = fonk5(b13, 50)
    b24 = {}
    b25 = {}
    for sentence in b22:
        b3 = fonk2(sentence).split()
        for word in b3:
            if len(word) >= 3:
                b26 = fonk3(word, b16, b18, b14)
                if b26 > b24.get(word, 0):
                    b24[word] = b26
    for sentence in b23:
        b3 = fonk2(sentence).split()
        for word in b3:
            if len(word) >= 3:
                b27 = fonk3(word, b17, b19, b15)
                if b27 > b25.get(word, 0):
                    b25[word] = b27
    b28 = sum(class1 for sentence in b22 if fonk7(sentence, b20, b21, b16, b17, b18, b19, b14, b15) == class1)
    b29 = len(b22) - b28
    b30 = sum(class1 for sentence in b23 if fonk7(sentence, b20, b21, b16, b17, b18, b19, b14, b15) == class2)
    b31 = len(b23) - b30
    b32 = b28 / (b28 + b31)
    b33 = b28 / (b28 + b29)
    print("Precision:", b32)
    print("Recall:", b33)
    print("Important b3 in class class1:", OrderedDict(sorted(b24.items(), b34 = lambda x: x[class1], reverse=True)))
    print("Important b3 in class class2:", OrderedDict(sorted(b25.items(), b34 = lambda x: x[class1], reverse=True)))
def fonk7(sentence, b20, b21, b16, b17, b18, b19, b14, b15):
    b3 = fonk2(sentence).split()
    b35 = b20
    b36 = b21
    for word in b3:
        if len(word) >= 3:
            b26 = fonk3(word, b16, b18, b14)
            b27 = fonk3(word, b17, b19, b15)
            b35 += b26
            b36 += b27
    return class1 if b35 > b36 else class2
fonk6()