import glob
from collections import Counter
from nltk.corpus import stopwords
import string
import numpy
import sys
b1 = sys.argv[1]
b2 = sys.argv[2]
b3 = sys.argv[3]
b4 = sys.argv[4]
b5 = sys.argv[5]
b6 = sys.argv[6]
b7 = sys.argv[7]
b1 = glob.glob(b1+"/*.txt")
b2 = glob.glob(b2+"/*.txt")
b3 = glob.glob(b3+"/*.txt")
b4 = glob.glob(b4+"/*.txt")
def fonk1(filename, stop_words, bayes):
    b8 = ""
    for file_names in filename:
        b9 = open(file_names)
        b8 += b9.read()
    b10 = str.maketrans('', '', string.punctuation)
    b8 = b8.translate(b10)
    b10 = str.maketrans('', '', string.digits)
    b8 = b8.translate(b10)
    b8 = Counter(b8.split())
    if stop_words:
        b8 = Counter([word for word in b8 if word not in stopwords.words('english')])
    return b8
def fonk2(unique_words):
    b11 = {}
    a1 = 0
    for i in unique_words:
        a1 += unique_words[i]
    for i in unique_words:
        b11[i] = float(unique_words[i]) / int(a1)
    return b11
def fonk3(unique_word):
    b12 = {}
    for word_bag in bag_of_words:
        b12[word_bag] = float(unique_word[word_bag]) / float(bag_of_words[word_bag] + len(bag_of_words))
    return b12
def fonk4(test_file):
    a2 = 0.0
    a3 = 0.0
    for file_name in test_file:
        a4 = 0.0
        a5 = 0.0
        a6 = 1.0
        a7 = 1.0
        b13 = open(file_name)
        b14 = b13.read()
        b14 = Counter(b14.split())
        for word in b14:
            if word in bag_of_words:
                a6 = a6 * prob_ham_given_word[word]
                a7 = a7 * prob_spam_given_word[word]
        if a6 + a7:
            if a6 / (a6 + a7) > 0.5:
                a3 += 1
            else:
                a2 += 1
    return a3, a2
def fonk5(train_1, train_2, bag):
    for word in bag:
        train_1[word] += 1
        train_2[word] += 1
    return train_1, train_2
def fonk6(b17):
    b15 = fonk1(b1, b17, 0)
    b16 = fonk1(b2, b17, 0)
fonk6(b17 = 0)
fonk6(b17 = 1)