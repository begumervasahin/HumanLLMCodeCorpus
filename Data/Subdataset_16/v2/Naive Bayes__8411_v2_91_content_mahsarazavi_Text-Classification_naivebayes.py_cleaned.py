import re
import random
from collections import Counter, OrderedDict
from nltk.corpus import stopwords
import math
b1 = "raw_data_sport.txt"
b2 = "raw_data_politics.txt"
b3 = {}
b4 = {}
def fonk1(b9, percent):
    b5 = b9.split(" ")
    b6 = int(len(b5) * percent)
    b7 = random.sample(b5, b6)
    b8 = [word for word in b5 if word not in b7]
    return ' '.join(b8), ' '.join(b7)
def fonk2(b9):
    b9 = b9.lower()
    b9 = re.sub(r'\d+', '', b9)
    b9 = b9.replace("\n", " ").replace("-", "")
    b10 = set(stopwords.b5('english'))
    b9 = ' '.join(word for word in b9.split() if word not in b10)
    return b9
def fonk3(x, mean, std):
    return (b24 / (math.sqrt(b25 * math.pi) * std)) * math.exp(-((x - mean) ** b25) / (b25 * std ** b25))
def fonk4(word, class_words, class_word_count, total_words, distinct_words):
    b11 = class_words.get(word, 0)
    return math.log10((b11 + b24) / (class_word_count + distinct_words))
def fonk5(b9, b32, b33, countallword1, b30, countDistWords1, b31, b20, b21):
    b9 = fonk2(b9).split()
    b12 = b32
    b13 = b33
    b18, b14 = -float('inf'), -float('inf')
    b19, b15 = '', ''
    for word in b9:
        if len(word) < 3:
            continue
        b16 = fonk4(word, b20, countallword1, countallword1, countDistWords1)
        b17 = fonk4(word, b21, b30, b30, b31)
        if b16 > b18:
            b18 = b16
            b19 = word
        if b17 > b14:
            b14 = b17
            b15 = word
        b12 += b16
        b13 += b17
    if b12 > b13:
        b4[b19] = b18
        return b24
    else:
        b3[b15] = b14
        return b25
def fonk6(train1, train2):
    b20 = Counter(re.findall(r'\w+', train1))
    b21 = Counter(re.findall(r'\w+', train2))
    return b20, b21
def fonk7(arr):
    b22 = len(arr)
    return [' '.join(arr[i * 50:(i + b24) * 50]) for i in range(b22)] + [' '.join(arr[b22 * 50:])]
def fonk8():
    with open(b1, 'r', b23 = 'utf8', errors='ignore') as f:
        b24 = f.read()
    with open(b2, 'r', b23 = 'utf8', errors='ignore') as f:
        b25 = f.read()
    b24, b25 = fonk2(b24), fonk2(b25)
    train1, b26 = fonk1(b24, 0.10)
    train2, b27 = fonk1(b25, 0.10)
    b28 = len(re.findall(r'\w+', train1))
    b29 = len(re.findall(r'\w+', train2))
    b20, b21 = fonk6(train1, train2)
    countallword1, b30 = sum(b20.values()), sum(b21.values())
    countDistWords1, b31 = len(b20), len(b21)
    b32 = b28 / (b28 + b29)
    b33 = b29 / (b28 + b29)
    b34 = fonk7(re.findall(r'\w+', b26))
    b35 = fonk7(re.findall(r'\w+', b27))
    tp, fn, fp, b36 = 0, 0, 0, 0
    for sentence in b34:
        b37 = fonk5(sentence, b32, b33, countallword1, b30, countDistWords1, b31, b20, b21)
        if b37 = = b24:
            tp += b24
        else:
            fn += b24
    for sentence in b35:
        b37 = fonk5(sentence, b32, b33, countallword1, b30, countDistWords1, b31, b20, b21)
        if b37 = = b25:
            b36 += b24
        else:
            fp += b24
    print(f'False Positives: {fp}, True Positives: {tp}, False Negatives: {fn}, True Negatives: {b36}')
    b38 = tp / (tp + fp) if (tp + fp) > 0 else 0
    b39 = tp / (tp + fn) if (tp + fn) > 0 else 0
    print(f'Precision: {b38}, Recall: {b39}')
    print('Important b5 in class b24:', OrderedDict(b4))
    print('Important b5 in class b25:', OrderedDict(b3))
if b40 = = "__main__":
    fonk8()