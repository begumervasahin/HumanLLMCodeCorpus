import re
import string
import random
from collections import Counter, OrderedDict
import math
from nltk.corpus import stopwords
b1 = "raw_data_sport.txt"
b2 = "raw_data_politics.txt"
b3 = {}
b4 = {}
def fonk1(b9, percent):
    b5 = b9.split()
    b6 = int(len(b5) * percent)
    b7 = random.sample(b5, b6)
    b8 = [word for word in b5 if word not in b7]
    return ' '.join(b8), ' '.join(b7)
def fonk2(b9):
    b9 = b9.lower()
    b9 = re.sub(r'\d+', '', b9)
    b9 = b9.replace("\n", " ")
    b9 = b9.replace("-", "")
    b10 = set(stopwords.b5('english'))
    for word in b10:
        b9 = b9.replace(" " + word + " ", " ")
    return b9
def fonk3(word, count_all_words, count_distinct_words, class_words):
    if word in class_words:
        b11 = (class_words[word] + 1) / (count_distinct_words + count_all_words)
        return math.log10(b11 + 1)
    else:
        b11 = 1 / (count_distinct_words + count_all_words)
        return math.log10(b11 + 1)
def fonk4(b9, b29, b30, b25, b26, b27, b28, class1_words, b24):
    b9 = fonk2(b9)
    b5 = b9.split()
    b12 = b29
    b13 = b30
    a1 = 0
    a2 = 0
    for word in b5:
        if len(word) < 3:
            continue
        b14 = fonk3(word, b25, b27, class1_words)
        if b14 > a1:
            a1 = b14
            b3[word] = a1
        b14 = fonk3(word, b26, b28, b24)
        if b14 > a2:
            a2 = b14
            b4[word] = a2
        b12 += fonk3(word, b25, b27, class1_words)
        b13 += fonk3(word, b26, b28, b24)
    if b12 > b13:
        return 1
    else:
        return 2
def fonk5(train1, train2):
    b15 = OrderedDict(Counter(train1.split()))
    b16 = OrderedDict(Counter(train2.split()))
    return b15, b16
def fonk6(b5):
    b17 = []
    while len(b5) > 50:
        b17.append(' '.join(b5[:50]))
        del b5[:50]
    if b5:
        b17.append(' '.join(b5))
    return b17
def fonk7():
    b18 = open(b1).read()
    b19 = open(b2).read()
    train1, b20 = fonk1(b18, 0.10)
    train2, b21 = fonk1(b19, 0.10)
    b22 = sum(Counter(train1.split('.')).values())
    b23 = sum(Counter(train2.split('.')).values())
    class1_words, b24 = fonk5(train1, train2)
    b25 = sum(class1_words.values())
    b26 = sum(b24.values())
    b27 = len(class1_words)
    b28 = len(b24)
    b29 = b22 / (b22 + b23)
    b30 = b23 / (b22 + b23)
    b31 = fonk6(b20.split())
    b32 = fonk6(b21.split())
    b33 = false_negatives = false_positives = true_negatives = 0
    for sentence in b31:
        b34 = fonk4(sentence, b29, b30, b25, b26, b27, b28, class1_words, b24)
        if b34 = = 1:
            b33 += 1
        else:
            false_negatives += 1
    for sentence in b32:
        b34 = fonk4(sentence, b29, b30, b25, b26, b27, b28, class1_words, b24)
        if b34 = = 2:
            true_negatives += 1
        else:
            false_positives += 1
    b35 = b33 / (b33 + false_positives)
    b36 = b33 / (b33 + false_negatives)
    print("Precision:", b35)
    print("Recall:", b36)
    print("False Positives:", false_positives)
    print("True Positives:", b33)
    print("False Negatives:", false_negatives)
    print("True Negatives:", true_negatives)
    print("Important Words in Class 1:", OrderedDict(b3))
    print("Important Words in Class 2:", OrderedDict(b4))
fonk7()