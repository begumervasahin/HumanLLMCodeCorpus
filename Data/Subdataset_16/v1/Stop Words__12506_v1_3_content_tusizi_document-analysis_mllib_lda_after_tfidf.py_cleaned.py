import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import lda
def fonk1():
    b1 = []
    with open('/vagrant/data/160928/6335045150218551554', 'r') as file:
        for line in file:
            b2 = json.loads(line)['content']
            b1.append(b2.strip())
    b3 = CountVectorizer()
    b4 = b3.fit_transform(b1)
    b5 = b4.toarray()
    print(f"Weight matrix shape: {b5.shape}")
    print("First 5 rows and columns of the b5 matrix:")
    print(b5[:5, :5])
    print('LDA:')
    b6 = lda.LDA(n_topics=2, n_iter=500, random_state=1)
    b6.fit(b5)
    b7 = b6.topic_word_
    b8 = b6.doc_topic_
    print(f"type(b8): {type(b8)}")
    print(f"shape: {b8.shape}")
    b9 = []
    for n in range(10):
        b10 = b8[n].argmax()
        b9.append(b10)
        print(f"doc: {n} topic: {b10}")
    fonk2(b8)
    fonk3(b7)
def fonk2(b8):
    f, b11 = plt.subplots(6, 1, figsize=(8, 8), sharex=True)
    for i, k in enumerate([0, 1, 2, 3, 8, 9]):
        b11[i].stem(b8[k, :], b12 = 'r-', markerfmt='ro', basefmt='w-')
        b11[i].set_xlim(-1, 2)
        b11[i].set_ylim(0, 1.2)
        b11[i].set_ylabel("Prob")
        b11[i].set_title(f"Document {k}")
    b11[5].set_xlabel("Topic")
    plt.tight_layout()
    plt.show()
def fonk3(b7):
    f, b11 = plt.subplots(2, 1, figsize=(6, 6), sharex=True)
    for i, k in enumerate([0, 1]):
        b11[i].stem(b7[k, :], b12 = 'b-', markerfmt='bo', basefmt='w-')
        b11[i].set_xlim(-2, 20)
        b11[i].set_ylim(0, 1)
        b11[i].set_ylabel("Prob")
        b11[i].set_title(f"Topic {k}")
    b11[1].set_xlabel("Word")
    plt.tight_layout()
    plt.show()
if b13 = = "__main__":
    fonk1()