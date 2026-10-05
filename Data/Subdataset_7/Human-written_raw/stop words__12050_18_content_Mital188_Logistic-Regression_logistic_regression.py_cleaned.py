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
	ef slice_bag(b12,a2):
    a1 = 0
    for word in list(b12):
        if b12[word] < 2 and a1 <a2:
            a1+=1
            del b12[word]
    return b12
def fonk2(b24):
    b11 = fonk1(b2, b24, 1)
    b12 = b11
    b12 = slice_bag(b12,a2=4000)
    b13 = []
    b14 = []
    for file_name in b1:
        b15 = {}
        b16 = open(file_name)
        b17 = b16.read()
        b17 = b17.split(" ")
        b17 = Counter(b17)
        for words in b12:
            b15[words] =(b17[words])
        b15["Probability_of_class"] = 0.0
        b15["Class_of_file"] = 0
        b14.append(b15)
    for file_name in b2:
        b15 = {}
        b16 = open(file_name)
        b17 = b16.read()
        b17 = b17.split(" ")
        b17 = Counter(b17)
        for words in b12:
            b15[words] = (b17[words])
        b15["Probability_of_class"] = 0.0
        b15["Class_of_file"] = 1
        b14.append(b15)
    return b14, b13, b12
def fonk3(a5,weights, feature_mat):
    a2 = 0
    for b15 in feature_mat:
        a3 = 0
        a2+=1
        for words in weights:
            a3 += weights[words] * b15[words]
        if a3 < 700:
            b18 = numpy.exp(numpy.array(a5 + a3, dtype=numpy.float)) /(1 + numpy.exp(numpy.array(a5 + a3,dtype=numpy.float)))
        else:
            b18 = 1.0
        b15["Probability_of_class"] = b18
    return feature_mat
def fonk4(weights,n,lam,b14):
    for b22 in weights:
        a4 = 0.0
        for b15 in b14:
            a4 += b15[b22]*(b15["Class_of_file"] - b15["Probability_of_class"])
        weights[b22] = weights[b22] + n*a4 - n*lam*weights[b22]
    return weights
def fonk5(weights):
    b19 = 0;
    b20 = 0;
    for file_name in b4:
        b16 = open(file_name)
        b17 = b16.read()
        b17 = b17.split(" ")
        b17 = Counter(b17)
        a3 = 0
        b20 += 1
        for words in weights:
            a3 += weights[words] * b17[words]
        if a3 < 700:
            b18 = numpy.exp(numpy.array(1 + a3, dtype=numpy.float)) /(1 + numpy.exp(numpy.array(1 + a3,dtype=numpy.float)))
        else:
            b18 = 1.0
        if b18 > 0.9:
            b19 += 1
    for file_name in b3:
        b16 = open(file_name)
        b17 = b16.read()
        b17 = b17.split(" ")
        b17 = Counter(b17)
        a3 = 0
        b20 += 1
        for words in weights:
            a3 += weights[words] * b17[words]
        if a3 < 700:
            b18 = numpy.exp(numpy.array(1 + a3, dtype=numpy.float)) /(1 + numpy.exp(numpy.array(1 + a3,dtype=numpy.float)))
        else:
            b18 = 1.0
        if b18 < 0.9:
            b19 += 1
    return b19/b20
def fonk6(b25,n,lam,b24):
    global b14
    b14, b13, b12 = fonk2(b24)
    a5 = 1.0
    b21 = {}
    for word in b12:
        b21[word] = 1.0
    b14 = fonk3(a5,b21,b14)
    b22 = b21
    for i in range(b25):
        b22 = fonk4(b22,n,lam,b14)
        b14 = fonk3(a5, b22, b14)
    b23 = fonk5(b22)
    if b24 = = 1:
        try:
            print("Logistic Regression - filtered - Total Accuracy - " + str(b23 * 100))
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
    else:
        try:
            print("Logistic Regression - unfiltered - Total Accuracy - " + str(b23 * 100))
        except ZeroDivisionError as err:
            print('Handling run-time error:', err)
fonk6(b25 = int(b6), n=float(b7), lam=float(b5), b24=0)
fonk6(b25 = int(b6), n=float(b7), lam=float(b5), b24=1)