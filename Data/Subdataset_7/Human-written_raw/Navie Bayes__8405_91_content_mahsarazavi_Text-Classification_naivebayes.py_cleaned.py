import re
import string
import io
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from collections import *
import json
import random
import math
b1 = "raw_data_sport.txt"
b2 = "raw_data_politics.txt"
b3 = {}
b4 = {}
def fonk1(b12, percent):
    b5 = b12.split(" ")
    b6 = len(b5)
    b7 = int(b6 * percent)
    b8 = []
    for i in range(b7):
        b9 = random.randint(0, b6 -i-1)
        b8.append(b5[b9])
        del b5[b9]
    b10 = ' '.join(b5)
    b11 = ' '.join(b8)
    return b10, b11
def fonk2(b12):
    b12 = b12.lower()
    b12 = re.sub(b9'\d+', '', b12)
    b12 = b12.replace("\n", " ")
    b12 = b12.replace("-", "")
    b13 = set(stopwords.words('english'))
    for word in b13:
        b12 = b12.replace(" " + word + " ", " ")
    return b12
def fonk3(word, b32, b34, class1words):
    if word in class1words.keys():
        b14 = (class1words[word]+1)/(b34+b32)
        return math.log10(b14 + 1)
    else:
        b14 = 1/(b34+b32)
        return math.log10(b14 + 1)
def fonk4(word, b33, b35, b31):
    if word in b31.keys():
        b14 = (b31[word]+1)/(b35+b33)
        return math.log10(b14 + 1)
    else:
        b14 = 1/(b35+b33)
        return math.log10(b14 + 1)
def fonk5(b12, b36, b37, b32, b33, b34,b35,class1words,b31):
    b12 = fonk2(b12)
    b12 = b12.split("," and "\n" and " " and ":" and "?" and "\"" and "â" and " ")
    b15 = b36
    b16 = b37
    a1 = 0
    a2 = 0
    a3 = 0
    for word in b12:
        if len(word) < 3:
            continue
        b17 = fonk3(word, b32, b34, class1words)
        if b17 > a1:
            a1 = b17
            b18 = word
        b17 = fonk4(word, b33, b35, b31)
        if b17 > a2:
            a2 = b17
            a3 = word
        b15 += fonk3(word, b32, b34, class1words)
        b16 += fonk4(word, b33, b35, b31)
    if b15 > b16:
        b4[b18] = a1
        return 1
    else:
        b3[a3] = a2
        return 2
def fonk6(b19, b21):
    b19 = b19.split("," and "\n" and "." and ":" and "?" and "\"" and "â" and " ")
    b20 = OrderedDict(Counter(b19))
    b21 = b21.split("," and "\n" and "." and ":" and "?" and "\"" and "â" and " ")
    b22 = OrderedDict(Counter(b21))
    return b20, b22
def fonk7(arr):
    b23 = int(len(arr) / 50)
    b24 = []
    for i in range(b23):
        b24.append(" ".join(arr[: 50]))
        del arr[: 50]
    if len(" ".join(arr)):
        b24.append(" ".join(arr))
    return b24
def fonk8():
    b25 = open(b1).read()
    b26 = open(b2).read()
    b25 = b25.decode("utf8", 'ignore')
    b26 = b26.decode("utf8", 'ignore')
    b25 = fonk2(b25)
    b26 = fonk2(b26)
    b19, b27 = fonk1(b25, 0.10)
    b21, b28 = fonk1(b26, 0.10)
    b29 = sum(Counter(b19.split("." and "\n" and "\b9" and "?" and "!" and ":")).values())
    b30 = sum(Counter(b21.split("." and "\n" and "\b9" and "?" and "!" and ":")).values())
    class1words, b31 = fonk6(b19, b21)
    b32 = sum(class1words.values())
    b33 = sum(b31.values())
    print (b32, "count words 1")
    print (b33, "count words 2")
    b34 = len(class1words.keys())
    b35 = len(b31.keys())
    b36 = (b29/(b29+b30))
    b37 = (b30/(b29+b30))
    print(b29,"Count sentence 1")
    b38 = b27.split("." and "\n" and "\b9" and "?" and "!" and ":" and " ")
    b39 = b28.split("." and "\n" and "\b9" and "?" and "!" and ":" and " ")
    b38 = fonk7(b38)
    b39 = fonk7(b39)
    print(b38)
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    for sentence in b38:
        b40 = fonk5(sentence, b36, b37, b32, b33, b34, b35, class1words, b31)
        if b40 = = 1:
            a4 += 1
        else:
            a5 += 1
    for sentence in b39:
        b40 = fonk5(sentence, b36, b37, b32, b33, b34, b35,
                   class1words, b31)
        if b40 = = 2:
            a7 += 1
        else:
            a6 += 1
    print(a6, a4, a5, a7)
    print(precision, recall)
    print(OrderedDict(b4))
    print(OrderedDict(b3))
fonk8()