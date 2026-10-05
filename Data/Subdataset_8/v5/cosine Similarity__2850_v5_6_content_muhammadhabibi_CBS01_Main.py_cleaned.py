from __future__ import division
import numpy as np
import nltk
import yaml
import Preprocessing
import TF_IDF
import CosineSimilarity
pp = Preprocessing
cs = CosineSimilarity
with open('komentar.json', 'r') as file:
    komentar = yaml.safe_load(file)
with open('komentar_bersih.txt', 'r') as file:
    clean_comments = [line.strip() for line in file]
comment_vectors = [cs.TFIDF(comment) for comment in clean_comments]
test_sentences = [
    "sebaiknya waktu kuliahnya jangan terlalu sore",
    "lebih keras lagi suara",
    "buku rujuk kurang jelas mau pakai mana"
]
for sentence in test_sentences:
    print('---------------------------------------------------------------------------------------')
    print('Testing Sentence:', sentence)
    test_vector = cs.TFIDF(nltk.Text(str(sentence)))
    similarity_results = []
    for index, vector in enumerate(comment_vectors):
        similarity = cs.similarity(test_vector, vector)
        similarity_results.append((index, similarity, clean_comments[index]))
    most_similar = max(similarity_results, key=lambda x: x[1])
    print("Most Similar Comment:", most_similar)
    print("------------------------------------------------------------------------")
    for index, cosine, comment in similarity_results:
        if cosine >= 0.93:
            print(cosine, comment)