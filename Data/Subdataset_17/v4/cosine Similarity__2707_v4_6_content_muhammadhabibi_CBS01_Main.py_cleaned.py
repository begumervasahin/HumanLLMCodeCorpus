import math
import numpy as np
import nltk
import json
import yaml
import Preprocessing as pp
import TF_IDF as tfidf
import CosineSimilarity as cs
def load_comments(json_path, txt_path):
    with open(json_path, 'r') as output_file:
        komentar = yaml.safe_load(output_file)
    with open(txt_path, 'r') as komentar_bersih:
        data = komentar_bersih.read().split('\n')
    komen_bersih = [komen for komen in data if komen]
    return komentar, komen_bersih
def compute_tfidf_vectors(comments):
    return [tfidf.TFIDF(comment) for comment in comments]
def find_similar_comments(test_sentences, tfidf_vectors, comments):
    for test in test_sentences:
        print('---------------------------------------------------------------------------------------')
        print('Data Testing:', test)
        input_vector = tfidf.TFIDF(nltk.Text(test))
        results = []
        for i, vector in enumerate(tfidf_vectors):
            similarity_score = cs.similarity(input_vector, vector)
            results.append((i, similarity_score, comments[i]))
        best_match = sorted(results, key=lambda x: x[1], reverse=True)[0]
        print('Best Match:', best_match)
        print('------------------------------------------------------------------------')
        for index, cosine, comment in results:
            if cosine >= 0.93:
                print(cosine, comment)
if __name__ == "__main__":
    komentar, komen_bersih = load_comments('komentar.json', 'komentar_bersih.txt')
    tfidf_vectors = compute_tfidf_vectors(komen_bersih)
    test_sentences = [
        "sebaiknya waktu kuliahnya jangan terlalu sore",
        "lebih keras lagi suara",
        "buku rujukan kurang jelas mau pakai mana"
    ]
    find_similar_comments(test_sentences, tfidf_vectors, komen_bersih)