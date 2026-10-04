import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import lda
def main():
    corpus = load_corpus('/vagrant/data/160928/6335045150218551554')
    weight = vectorize_corpus(corpus)
    topic_word, doc_topic = perform_lda(weight)
    display_information(weight, doc_topic)
    plot_doc_topics(doc_topic)
    plot_topic_words(topic_word)
def load_corpus(file_path):
    corpus = []
    with open(file_path, 'r') as file:
        for line in file:
            content_ = json.loads(line)['content']
            corpus.append(content_.strip())
    return corpus
def vectorize_corpus(corpus):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    return X.toarray()
def perform_lda(weight):
    model = lda.LDA(n_topics=2, n_iter=500, random_state=1)
    model.fit(weight)
    return model.topic_word_, model.doc_topic_
def display_information(weight, doc_topic):
    print(f"Weight matrix shape: {weight.shape}")
    print("First 5 rows and columns of the weight matrix:")
    print(weight[:5, :5])
    print(f"type(doc_topic): {type(doc_topic)}")
    print(f"shape: {doc_topic.shape}")
    for n in range(10):
        topic_most_pr = doc_topic[n].argmax()
        print(f"doc: {n} topic: {topic_most_pr}")
def plot_doc_topics(doc_topic):
    fig, axes = plt.subplots(6, 1, figsize=(8, 8), sharex=True)
    for i, k in enumerate([0, 1, 2, 3, 8, 9]):
        axes[i].stem(doc_topic[k, :], linefmt='r-', markerfmt='ro', basefmt='w-')
        axes[i].set_xlim(-1, 2)
        axes[i].set_ylim(0, 1.2)
        axes[i].set_ylabel("Prob")
        axes[i].set_title(f"Document {k}")
    axes[5].set_xlabel("Topic")
    plt.tight_layout()
    plt.show()
def plot_topic_words(topic_word):
    fig, axes = plt.subplots(2, 1, figsize=(6, 6), sharex=True)
    for i, k in enumerate([0, 1]):
        axes[i].stem(topic_word[k, :], linefmt='b-', markerfmt='bo', basefmt='w-')
        axes[i].set_xlim(-2, 20)
        axes[i].set_ylim(0, 1)
        axes[i].set_ylabel("Prob")
        axes[i].set_title(f"Topic {k}")
    axes[1].set_xlabel("Word")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()