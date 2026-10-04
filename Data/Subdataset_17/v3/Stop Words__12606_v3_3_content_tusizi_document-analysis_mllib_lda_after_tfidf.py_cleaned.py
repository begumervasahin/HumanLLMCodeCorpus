import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import lda
def main():
    corpus = load_corpus('/vagrant/data/160928/6335045150218551554')
    weight_matrix = vectorize_corpus(corpus)
    topic_word_matrix, doc_topic_matrix = perform_lda(weight_matrix)
    display_matrix_info(weight_matrix, doc_topic_matrix)
    plot_document_topics(doc_topic_matrix)
    plot_topic_words(topic_word_matrix)
def load_corpus(file_path):
    corpus = []
    with open(file_path, 'r') as file:
        for line in file:
            content = json.loads(line)['content']
            corpus.append(content.strip())
    return corpus
def vectorize_corpus(corpus):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    return X.toarray()
def perform_lda(weight_matrix):
    model = lda.LDA(n_topics=2, n_iter=500, random_state=1)
    model.fit(weight_matrix)
    return model.topic_word_, model.doc_topic_
def display_matrix_info(weight_matrix, doc_topic_matrix):
    print(f"Weight matrix shape: {weight_matrix.shape}")
    print("First 5 rows and columns of the weight matrix:")
    print(weight_matrix[:5, :5])
    print(f"type(doc_topic_matrix): {type(doc_topic_matrix)}")
    print(f"shape: {doc_topic_matrix.shape}")
    for doc_index in range(10):
        most_probable_topic = doc_topic_matrix[doc_index].argmax()
        print(f"doc: {doc_index} topic: {most_probable_topic}")
def plot_document_topics(doc_topic_matrix):
    fig, axes = plt.subplots(6, 1, figsize=(8, 8), sharex=True)
    selected_docs = [0, 1, 2, 3, 8, 9]
    for i, doc_index in enumerate(selected_docs):
        axes[i].stem(doc_topic_matrix[doc_index, :], linefmt='r-', markerfmt='ro', basefmt='w-')
        axes[i].set_xlim(-1, 2)
        axes[i].set_ylim(0, 1.2)
        axes[i].set_ylabel("Prob")
        axes[i].set_title(f"Document {doc_index}")
    axes[5].set_xlabel("Topic")
    plt.tight_layout()
    plt.show()
def plot_topic_words(topic_word_matrix):
    fig, axes = plt.subplots(2, 1, figsize=(6, 6), sharex=True)
    for i, topic_index in enumerate([0, 1]):
        axes[i].stem(topic_word_matrix[topic_index, :], linefmt='b-', markerfmt='bo', basefmt='w-')
        axes[i].set_xlim(-2, 20)
        axes[i].set_ylim(0, 1)
        axes[i].set_ylabel("Prob")
        axes[i].set_title(f"Topic {topic_index}")
    axes[1].set_xlabel("Word")
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()