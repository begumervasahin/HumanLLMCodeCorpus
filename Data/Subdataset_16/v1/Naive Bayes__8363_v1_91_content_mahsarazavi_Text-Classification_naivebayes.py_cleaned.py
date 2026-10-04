import re
import random
from collections import Counter, OrderedDict
from nltk.corpus import stopwords
import math
b1 = "raw_data_sport.txt"
b2 = "raw_data_politics.txt"
b3 = {}
b4 = {}
def fonk1(b10, percent):
    b5 = b10.split(" ")
    b6 = len(b5)
    b7 = int(b6 * percent)
    b8 = random.sample(b5, b7)
    b9 = [word for word in b5 if word not in b8]
    return ' '.join(b9), ' '.join(b8)
def fonk2(b10):
    b10 = b10.lower()
    b10 = re.sub(r'\d+', '', b10)
    b10 = b10.replace("\n", " ").replace("-", "")
    b11 = set(stopwords.b5('english'))
    b10 = ' '.join(word for word in b10.split() if word not in b11)
    return b10
def fonk3(x, mean, std):
    return (b25 / (math.sqrt(b26 * math.pi) * std)) * math.exp(-((x - mean) ** b26) / (b26 * std ** b26))
def fonk4(word, class_words, class_word_count, total_words, distinct_words):
    b12 = class_words.get(word, 0)
    return math.log10((b12 + b25) / (class_word_count + distinct_words))
def fonk5(b10, b33, b34, countallword1, b31, countDistWords1, b32, b21, b22):
    b10 = fonk2(b10).split()
    b13 = b33
    b14 = b34
    b19, b15 = -float('inf'), -float('inf')
    b20, b16 = '', ''
    for word in b10:
        if len(word) < 3:
            continue
        b17 = fonk4(word, b21, countallword1, countallword1, countDistWords1)
        b18 = fonk4(word, b22, b31, b31, b32)
        if b17 > b19:
            b19 = b17
            b20 = word
        if b18 > b15:
            b15 = b18
            b16 = word
        b13 += b17
        b14 += b18
    if b13 > b14:
        b4[b20] = b19
        return b25
    else:
        b3[b16] = b15
        return b26
def fonk6(train1, train2):
    b21 = Counter(re.findall(r'\w+', train1))
    b22 = Counter(re.findall(r'\w+', train2))
    return b21, b22
def fonk7(arr):
    b23 = len(arr)
    return [' '.join(arr[i*50:(i+b25)*50]) for i in range(b23)] + [' '.join(arr[b23*50:])]
def fonk8():
    with open(b1, 'r', b24 = 'utf8', errors='ignore') as f:
        b25 = f.read()
    with open(b2, 'r', b24 = 'utf8', errors='ignore') as f:
        b26 = f.read()
    b25, b26 = fonk2(b25), fonk2(b26)
    train1, b27 = fonk1(b25, 0.10)
    train2, b28 = fonk1(b26, 0.10)
    b29 = len(re.findall(r'\w+', train1))
    b30 = len(re.findall(r'\w+', train2))
    b21, b22 = fonk6(train1, train2)
    countallword1, b31 = sum(b21.values()), sum(b22.values())
    countDistWords1, b32 = len(b21), len(b22)
    b33 = b29 / (b29 + b30)
    b34 = b30 / (b29 + b30)
    b35 = fonk7(re.findall(r'\w+', b27))
    b36 = fonk7(re.findall(r'\w+', b28))
    tp, fn, fp, b37 = 0, 0, 0, 0
    for sentence in b35:
        b38 = fonk5(sentence, b33, b34, countallword1, b31, countDistWords1, b32, b21, b22)
        if b38 = = b25:
            tp += b25
        else:
            fn += b25
    for sentence in b36:
        b38 = fonk5(sentence, b33, b34, countallword1, b31, countDistWords1, b32, b21, b22)
        if b38 = = b26:
            b37 += b25
        else:
            fp += b25
    print(f'False Positives: {fp}, True Positives: {tp}, False Negatives: {fn}, True Negatives: {b37}')
    b39 = tp / (tp + fp) if (tp + fp) > 0 else 0
    b40 = tp / (tp + fn) if (tp + fn) > 0 else 0
    print(f'Precision: {b39}, Recall: {b40}')
    print('Important b5 in class b25:', OrderedDict(b4))
    print('Important b5 in class b26:', OrderedDict(b3))
if b41 = = "__main__":
    fonk8()