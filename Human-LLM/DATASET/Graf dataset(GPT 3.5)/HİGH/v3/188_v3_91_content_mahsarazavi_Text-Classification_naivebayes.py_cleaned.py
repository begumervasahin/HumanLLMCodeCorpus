import re
import random
import math
from collections import Counter, OrderedDict
from nltk.corpus import stopwords
b1 = "raw_data_sport.txt"
b2 = "raw_data_politics.txt"
b3 = {}
b4 = {}
def fonk1(b9, percent):
    '''Randomly partition the b9 into two parts based on the given percentage.'''
    b5 = b9.split()
    b6 = int(len(b5) * percent)
    b7 = random.sample(b5, b6)
    b8 = [word for word in b5 if word not in b7]
    return ' '.join(b8), ' '.join(b7)
def fonk2(b9):
    '''Clean and preprocess the b9 by converting to lowercase, removing digits, punctuation, and stop b5.'''
    b9 = b9.lower()
    b9 = re.sub(r'\d+', '', b9)
    b9 = b9.replace("\n", " ").replace("-", "")
    b10 = set(stopwords.b5('english'))
    for word in b10:
        b9 = b9.replace(" " + word + " ", " ")
    return b9
def fonk3(word_count, total_word_count, distinct_word_count):
    '''Calculate the log probability of a word given the class.'''
    b11 = (word_count + 1) / (distinct_word_count + total_word_count)
    return math.log10(b11 + 1)
def fonk4(b9, b30, b31, b26, b27, b28, b29, class1_words, b25):
    '''Calculate the probability of the b9 belonging to each class.'''
    b9 = fonk2(b9)
    b5 = b9.split()
    b12 = b30
    b13 = b31
    a1 = 0
    a2 = 0
    for word in b5:
        if len(word) < 3:
            continue
        b14 = fonk3(class1_words.get(word, 0), b26, b28)
        if b14 > a1:
            a1 = b14
            b3[word] = a1
        b14 = fonk3(b25.get(word, 0), b27, b29)
        if b14 > a2:
            a2 = b14
            b4[word] = a2
        b12 += fonk3(class1_words.get(word, 0), b26, b28)
        b13 += fonk3(b25.get(word, 0), b27, b29)
    return 1 if b12 > b13 else 2
def fonk5(train1, train2):
    '''Count the occurrences of b5 in the training data for each class.'''
    b15 = OrderedDict(Counter(train1.split()))
    b16 = OrderedDict(Counter(train2.split()))
    return b15, b16
def fonk6(b5, b17 = 50):
    '''Convert a list of b5 into strings of a specified chunk size.'''
    b18 = []
    while len(b5) > b17:
        b18.append(' '.join(b5[:b17]))
        del b5[:b17]
    if b5:
        b18.append(' '.join(b5))
    return b18
def fonk7():
    '''Classify the test data into classes and evaluate the performance.'''
    b19 = open(b1).read()
    b20 = open(b2).read()
    train1, b21 = fonk1(b19, 0.10)
    train2, b22 = fonk1(b20, 0.10)
    b23 = sum(Counter(train1.split('.')).values())
    b24 = sum(Counter(train2.split('.')).values())
    class1_words, b25 = fonk5(train1, train2)
    b26 = sum(class1_words.values())
    b27 = sum(b25.values())
    b28 = len(class1_words)
    b29 = len(b25)
    b30 = b23 / (b23 + b24)
    b31 = b24 / (b23 + b24)
    b32 = fonk6(b21.split())
    b33 = fonk6(b22.split())
    b34 = false_negatives = false_positives = true_negatives = 0
    for sentence in b32:
        b35 = fonk4(sentence, b30, b31, b26, b27, b28, b29, class1_words, b25)
        if b35 = = 1:
            b34 += 1
        else:
            false_negatives += 1
    for sentence in b33:
        b35 = fonk4(sentence, b30, b31, b26, b27, b28, b29, class1_words, b25)
        if b35 = = 2:
            true_negatives += 1
        else:
            false_positives += 1
    b36 = b34 / (b34 + false_positives)
    b37 = b34 / (b34 + false_negatives)
    print("Precision:", b36)
    print("Recall:", b37)
    print("False Positives:", false_positives)
    print("True Positives:", b34)
    print("False Negatives:", false_negatives)
    print("True Negatives:", true_negatives)
    print("Important Words in Class 1:", OrderedDict(b3))
    print("Important Words in Class 2:", OrderedDict(b4))
fonk7()