import os
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import lda
def fonk1(b13):
    b1 = []
    with open(b13, 'r') as file:
        for line in file:
            b2 = json.loads(line)['content']
            b1.append(b2.strip())
    return b1
def fonk2(b1):
    b3 = CountVectorizer()
    b4 = b3.fit_transform(b1)
    return b4.toarray(), b3
def fonk3(b3, weight):
    print(b3)
    print(len(weight))
    print(weight[:5, :5])
def fonk4(weight, b5 = 2, n_iter=500):
    b6 = lda.LDA(b5=b5, n_iter=n_iter, random_state=1)
    b6.fit(weight)
    return b6
def fonk5(b15, b7 = 10):
    print("type(b15): {}".format(type(b15)))
    print("shape: {}".format(b15.shape))
    b8 = []
    for n in range(b7):
        b9 = b15[n].argmax()
        b8.append(b9)
        print("doc: {} topic: {}".format(n, b9))
    return b8
def fonk6(b15, doc_indices):
    f, b10 = plt.subplots(len(doc_indices), 1, figsize=(8, 8), sharex=True)
    for i, k in enumerate(doc_indices):
        b10[i].stem(b15[k, :], b11 = 'r-', markerfmt='ro', basefmt='w-')
        b10[i].set_xlim(-1, 2)
        b10[i].set_ylim(0, 1.2)
        b10[i].set_ylabel("Prob")
        b10[i].set_title("Document {}".format(k))
    b10[-1].set_xlabel("Topic")
    plt.tight_layout()
    plt.show()
def fonk7(b14, topic_indices):
    f, b10 = plt.subplots(len(topic_indices), 1, figsize=(6, 6), sharex=True)
    for i, k in enumerate(topic_indices):
        b10[i].stem(b14[k, :], b11 = 'b-', markerfmt='bo', basefmt='w-')
        b10[i].set_xlim(-2, 20)
        b10[i].set_ylim(0, 1)
        b10[i].set_ylabel("Prob")
        b10[i].set_title("Topic {}".format(k))
    b10[-1].set_xlabel("Word")
    plt.tight_layout()
    plt.show()
if b12 = = "__main__":
    b13 = '/vagrant/data/160928/6335045150218551554'
    b1 = fonk1(b13)
    weight, b3 = fonk2(b1)
    fonk3(b3, weight)
    b6 = fonk4(weight)
    b14 = b6.topic_word_
    b15 = b6.doc_topic_
    fonk5(b15)
    fonk6(b15, [0, 1, 2, 3, 8, 9])
    fonk7(b14, [0, 1])