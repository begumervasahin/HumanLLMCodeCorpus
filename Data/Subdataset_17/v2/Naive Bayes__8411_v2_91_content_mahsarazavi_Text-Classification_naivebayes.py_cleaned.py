import re
import random
from collections import Counter, OrderedDict
from nltk.corpus import stopwords
import math
class1file = "raw_data_sport.txt"
class2file = "raw_data_politics.txt"
impWOrd85 = {}
impWOrd77 = {}
def randonPartitioner(text, percent):
    words = text.split(" ")
    partition_size = int(len(words) * percent)
    partition = random.sample(words, partition_size)
    remaining = [word for word in words if word not in partition]
    return ' '.join(remaining), ' '.join(partition)
def cleanText(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.replace("\n", " ").replace("-", "")
    stop_words = set(stopwords.words('english'))
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text
def normal_pdf(x, mean, std):
    return (1 / (math.sqrt(2 * math.pi) * std)) * math.exp(-((x - mean) ** 2) / (2 * std ** 2))
def calculate_probability(word, class_words, class_word_count, total_words, distinct_words):
    word_count = class_words.get(word, 0)
    return math.log10((word_count + 1) / (class_word_count + distinct_words))
def calculateP(text, pclass1, pclass2, countallword1, countallword2, countDistWords1, countDistWords2, class1words, class2words):
    text = cleanText(text).split()
    pWordInClass1 = pclass1
    pWordInClass2 = pclass2
    pmax1, pmax2 = -float('inf'), -float('inf')
    impword1, impword2 = '', ''
    for word in text:
        if len(word) < 3:
            continue
        p1 = calculate_probability(word, class1words, countallword1, countallword1, countDistWords1)
        p2 = calculate_probability(word, class2words, countallword2, countallword2, countDistWords2)
        if p1 > pmax1:
            pmax1 = p1
            impword1 = word
        if p2 > pmax2:
            pmax2 = p2
            impword2 = word
        pWordInClass1 += p1
        pWordInClass2 += p2
    if pWordInClass1 > pWordInClass2:
        impWOrd77[impword1] = pmax1
        return 1
    else:
        impWOrd85[impword2] = pmax2
        return 2
def countWords(train1, train2):
    class1words = Counter(re.findall(r'\w+', train1))
    class2words = Counter(re.findall(r'\w+', train2))
    return class1words, class2words
def stringifyEvery5Words(arr):
    LEN = len(arr)
    return [' '.join(arr[i * 50:(i + 1) * 50]) for i in range(LEN)] + [' '.join(arr[LEN * 50:])]
def classifier():
    with open(class1file, 'r', encoding='utf8', errors='ignore') as f:
        class1 = f.read()
    with open(class2file, 'r', encoding='utf8', errors='ignore') as f:
        class2 = f.read()
    class1, class2 = cleanText(class1), cleanText(class2)
    train1, test1 = randonPartitioner(class1, 0.10)
    train2, test2 = randonPartitioner(class2, 0.10)
    countSentence1 = len(re.findall(r'\w+', train1))
    countSentence2 = len(re.findall(r'\w+', train2))
    class1words, class2words = countWords(train1, train2)
    countallword1, countallword2 = sum(class1words.values()), sum(class2words.values())
    countDistWords1, countDistWords2 = len(class1words), len(class2words)
    pclass1 = countSentence1 / (countSentence1 + countSentence2)
    pclass2 = countSentence2 / (countSentence1 + countSentence2)
    sentence1 = stringifyEvery5Words(re.findall(r'\w+', test1))
    sentence2 = stringifyEvery5Words(re.findall(r'\w+', test2))
    tp, fn, fp, tn = 0, 0, 0, 0
    for sentence in sentence1:
        c = calculateP(sentence, pclass1, pclass2, countallword1, countallword2, countDistWords1, countDistWords2, class1words, class2words)
        if c == 1:
            tp += 1
        else:
            fn += 1
    for sentence in sentence2:
        c = calculateP(sentence, pclass1, pclass2, countallword1, countallword2, countDistWords1, countDistWords2, class1words, class2words)
        if c == 2:
            tn += 1
        else:
            fp += 1
    print(f'False Positives: {fp}, True Positives: {tp}, False Negatives: {fn}, True Negatives: {tn}')
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    print(f'Precision: {precision}, Recall: {recall}')
    print('Important words in class 1:', OrderedDict(impWOrd77))
    print('Important words in class 2:', OrderedDict(impWOrd85))
if __name__ == "__main__":
    classifier()