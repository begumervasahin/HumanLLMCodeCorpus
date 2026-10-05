import re
import string
import random
from collections import Counter, OrderedDict
import math
class1file = "raw_data_sport.txt"
class2file = "raw_data_politics.txt"
impWOrd85 = {}
impWOrd77 = {}
def randomPartitioner(text, percent):
    firstPartition = text.split(" ")
    partitionedLength = len(firstPartition)
    secondPartitionLength = int(partitionedLength * percent)
    secondPartition = []
    for i in range(secondPartitionLength):
        r = random.randint(0, partitionedLength - i - 1)
        secondPartition.append(firstPartition[r])
        del firstPartition[r]
    firstPartitionStringified = ' '.join(firstPartition)
    secondPartitionStringified = ' '.join(secondPartition)
    return firstPartitionStringified, secondPartitionStringified
def cleanText(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.replace("\n", " ")
    text = text.replace("-", "")
    stop_words = set(stopwords.words('english'))
    for word in stop_words:
        text = text.replace(" " + word + " ", " ")
    return text
def pClass1(word, countallword1, countDistWords1, class1words):
    if word in class1words.keys():
        tmp = (class1words[word] + 1) / (countDistWords1 + countallword1)
        return math.log10(tmp + 1)
    else:
        tmp = 1 / (countDistWords1 + countallword1)
        return math.log10(tmp + 1)
def pClass2(word, countallword2, countDistWords2, class2words):
    if word in class2words.keys():
        tmp = (class2words[word] + 1) / (countDistWords2 + countallword2)
        return math.log10(tmp + 1)
    else:
        tmp = 1 / (countDistWords2 + countallword2)
        return math.log10(tmp + 1)
def calculateP(text, pclass1, pclass2, countallword1, countallword2, countDistWords1, countDistWords2, class1words, class2words):
    text = cleanText(text)
    text = text.split("," and "\n" and "." and ":" and "?" and "\"" and "â" and " ")
    pWordInClass1 = pclass1
    pWordInClass2 = pclass2
    pmax1 = 0
    pmax2 = 0
    impword2 = 0
    for word in text:
        if len(word) < 3:
            continue
        p = pClass1(word, countallword1, countDistWords1, class1words)
        if p > pmax1:
            pmax1 = p
            impword1 = word
        p = pClass2(word, countallword2, countDistWords2, class2words)
        if p > pmax2:
            pmax2 = p
            impword2 = word
        pWordInClass1 += pClass1(word, countallword1, countDistWords1, class1words)
        pWordInClass2 += pClass2(word, countallword2, countDistWords2, class2words)
    if pWordInClass1 > pWordInClass2:
        impWOrd77[impword1] = pmax1
        return 1
    else:
        impWOrd85[impword2] = pmax2
        return 2
def countWords(train1, train2):
    train1 = train1.split("," and "\n" and "." and ":" and "?" and "\"" and "â" and " ")
    counter1 = OrderedDict(Counter(train1))
    train2 = train2.split("," and "\n" and "." and ":" and "?" and "\"" and "â" and " ")
    counter2 = OrderedDict(Counter(train2))
    return counter1, counter2
def stringifyEvery5Words(arr):
    LEN = int(len(arr) / 50)
    result = []
    for i in range(LEN):
        result.append(" ".join(arr[:50]))
        del arr[:50]
    if len(" ".join(arr)):
        result.append(" ".join(arr))
    return result
def classifier():
    class1 = open(class1file).read()
    class2 = open(class2file).read()
    class1 = cleanText(class1)
    class2 = cleanText(class2)
    train1, test1 = randomPartitioner(class1, 0.10)
    train2, test2 = randomPartitioner(class2, 0.10)
    countSentence1 = sum(Counter(train1.split("." and "\n" and "\r" and "?" and "!" and ":")).values())
    countSentence2 = sum(Counter(train2.split("." and "\n" and "\r" and "?" and "!" and ":")).values())
    class1words, class2words = countWords(train1, train2)
    countallword1 = sum(class1words.values())
    countallword2 = sum(class2words.values())
    countDistWords1 = len(class1words.keys())
    countDistWords2 = len(class2words.keys())
    pclass1 = (countSentence1 / (countSentence1 + countSentence2))
    pclass2 = (countSentence2 / (countSentence1 + countSentence2))
    sentence1 = test1.split("." and "\n" and "\r" and "?" and "!" and ":" and " ")
    sentence2 = test2.split("." and "\n" and "\r" and "?" and "!" and ":" and " ")
    sentence1 = stringifyEvery5Words(sentence1)
    sentence2 = stringifyEvery5Words(sentence2)
    tp = 0
    fn = 0
    fp = 0
    tn = 0
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
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    print("Precision:", precision)
    print("Recall:", recall)
    print("False Positives:", fp)
    print("True Positives:", tp)
    print("False Negatives:", fn)
    print("True Negatives:", tn)
    print("Important Words in Class 1:", OrderedDict(impWOrd77))
    print("Important Words in Class 2:", OrderedDict(impWOrd85))
classifier()