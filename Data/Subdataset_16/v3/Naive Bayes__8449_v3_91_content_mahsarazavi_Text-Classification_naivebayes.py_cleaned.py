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
    b5 = b9.split()
    b6 = int(len(b5) * percent)
    b7 = random.sample(b5, b6)
    b8 = [word for word in b5 if word not in b7]
    return ' '.join(b8), ' '.join(b7)
def fonk2(b9):
    b9 = b9.lower()
    b9 = re.sub(r'\d+', '', b9)
    b9 = b9.replace("\b22", " ").replace("-", "")
    b10 = set(stopwords.b5('english'))
    b9 = ' '.join(word for word in b9.split() if word not in b10)
    return b9
def fonk3(x, mean, std):
    return (b25 / (math.sqrt(b26 * math.pi) * std)) * math.exp(-((x - mean) ** b26) / (b26 * std ** b26))
def fonk4(word, class_words, class_word_count, total_words, distinct_words):
    b11 = class_words.get(word, 0)
    return math.log10((b11 + b25) / (class_word_count + distinct_words))
def fonk5(b9, b33, b34, countallword1, b29, count_dist_words1, count_dist_words2, b20, b21):
    b9 = fonk2(b9).split()
    b12 = b33
    b13 = b34
    b18, b14 = -float('inf'), -float('inf')
    b19, b15 = '', ''
    for word in b9:
        if len(word) < 3:
            continue
        b16 = fonk4(word, b20, countallword1, countallword1, count_dist_words1)
        b17 = fonk4(word, b21, b29, b29, count_dist_words2)
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
        return b25
    else:
        b3[b15] = b14
        return b26
def fonk6(train1, train2):
    b20 = Counter(re.findall(r'\w+', train1))
    b21 = Counter(re.findall(r'\w+', train2))
    return b20, b21
def fonk7(arr, b22 = 50):
    b23 = len(arr)
    return [' '.join(arr[i * b22:(i + b25) * b22]) for i in range(b23)] + [' '.join(arr[b23 * b22:])]
def fonk8():
    with open(b1, 'r', b24 = 'utf8', errors='ignore') as f:
        b25 = f.read()
    with open(b2, 'r', b24 = 'utf8', errors='ignore') as f:
        b26 = f.read()
    b25, b26 = fonk2(b25), fonk2(b26)
    train1, b27 = fonk1(b25, 0.10)
    train2, b28 = fonk1(b26, 0.10)
    b20, b21 = fonk6(train1, train2)
    countallword1, b29 = sum(b20.values()), sum(b21.values())
    countDistWords1, b30 = len(b20), len(b21)
    b31 = len(re.findall(r'\w+', train1))
    b32 = len(re.findall(r'\w+', train2))
    b33 = b31 / (b31 + b32)
    b34 = b32 / (b31 + b32)
    b35 = fonk7(re.findall(r'\w+', b27))
    b36 = fonk7(re.findall(r'\w+', b28))
    tp, fn, fp, b37 = 0, 0, 0, 0
    for sentence in b35:
        b38 = fonk5(sentence, b33, b34, countallword1, b29, countDistWords1, b30, b20, b21)
        if b38 = = b25:
            tp += b25
        else:
            fn += b25
    for sentence in b36:
        b38 = fonk5(sentence, b33, b34, countallword1, b29, countDistWords1, b30, b20, b21)
        if b38 = = b26:
            b37 += b25
        else:
            fp += b25
    print(f'False Positives: {fp}, True Positives: {tp}, False Negatives: {fn}, True Negatives: {b37}')
    b39 = tp / (tp + fp) if (tp + fp) > 0 else 0
    b40 = tp / (tp + fn) if (tp + fn) > 0 else 0
    print(f'Precision: {b39}, Recall: {b40}')
    print('Important b5 in class b25:', OrderedDict(sorted(b4.items(), b41 = lambda x: x[b25], reverse=True)))
    print('Important b5 in class b26:', OrderedDict(sorted(b3.items(), b41 = lambda x: x[b25], reverse=True)))
if b42 = = "__main__":
    fonk8()