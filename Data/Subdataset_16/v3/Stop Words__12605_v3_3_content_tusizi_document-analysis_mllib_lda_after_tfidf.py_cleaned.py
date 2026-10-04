import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import lda
def fonk1():
    b1 = fonk2('/vagrant/data/160928/6335045150218551554')
    b2 = fonk3(b1)
    topic_word_matrix, b3 = fonk4(b2)
    fonk5(b2, b3)
    fonk6(b3)
    fonk7(topic_word_matrix)
def fonk2(file_path):
    b1 = []
    with open(file_path, 'r') as file:
        for line in file:
            b4 = json.loads(line)['b4']
            b1.append(b4.strip())
    return b1
def fonk3(b1):
    b5 = CountVectorizer()
    b6 = b5.fit_transform(b1)
    return b6.toarray()
def fonk4(b2):
    b7 = lda.LDA(n_topics=2, n_iter=500, random_state=1)
    b7.fit(b2)
    return b7.topic_word_, b7.doc_topic_
def fonk5(b2, b3):
    print(f"Weight matrix shape: {b2.shape}")
    print("First 5 rows and columns of the weight matrix:")
    print(b2[:5, :5])
    print(f"type(b3): {type(b3)}")
    print(f"shape: {b3.shape}")
    for doc_index in range(10):
        b8 = b3[doc_index].argmax()
        print(f"doc: {doc_index} topic: {b8}")
def fonk6(b3):
    fig, b9 = plt.subplots(6, 1, figsize=(8, 8), sharex=True)
    b10 = [0, 1, 2, 3, 8, 9]
    for i, doc_index in enumerate(b10):
        b9[i].stem(b3[doc_index, :], b11 = 'r-', markerfmt='ro', basefmt='w-')
        b9[i].set_xlim(-1, 2)
        b9[i].set_ylim(0, 1.2)
        b9[i].set_ylabel("Prob")
        b9[i].set_title(f"Document {doc_index}")
    b9[5].set_xlabel("Topic")
    plt.tight_layout()
    plt.show()
def fonk7(topic_word_matrix):
    fig, b9 = plt.subplots(2, 1, figsize=(6, 6), sharex=True)
    for i, topic_index in enumerate([0, 1]):
        b9[i].stem(topic_word_matrix[topic_index, :], b11 = 'b-', markerfmt='bo', basefmt='w-')
        b9[i].set_xlim(-2, 20)
        b9[i].set_ylim(0, 1)
        b9[i].set_ylabel("Prob")
        b9[i].set_title(f"Topic {topic_index}")
    b9[1].set_xlabel("Word")
    plt.tight_layout()
    plt.show()
if b12 = = "__main__":
    fonk1()