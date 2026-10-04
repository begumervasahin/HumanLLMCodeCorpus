import math
import numpy as np
import json
import yaml
import nltk
from Preprocessing import preprocess
from TF_IDF import compute_tfidf
from CosineSimilarity import compute_similarity
def load_and_preprocess_comments(json_path, txt_path):
    with open(json_path, 'r') as output_file:
        komentar = yaml.safe_load(output_file)
    with open(txt_path, 'r') as komentar_bersih:
        data = komentar_bersih.read().split('\n')
    komen_bersih = [preprocess(komen) for komen in data]
    return komen_bersih
def compute_tfidf_vectors(comments):
    return [compute_tfidf(comment) for comment in comments]
def find_similar_comments(test_sentences, tfidf_vectors, comments):
    for test in test_sentences:
        print('---------------------------------------------------------------------------------------')
        print('Data Testing:', test)
        input_vector = compute_tfidf(nltk.Text(str(test)))
        results = []
        for i, vector in enumerate(tfidf_vectors):
            similarity_score = compute_similarity(input_vector, vector)
            results.append((i, similarity_score, comments[i]))
        best_match = sorted(results, key=lambda x: x[1], reverse=True)[0]
        print('Best Match:', best_match)
        print('------------------------------------------------------------------------')
        for index, cosine, kal in results:
            if cosine >= 0.93:
                print(cosine, kal)
if __name__ == "__main__":
    komen_bersih = load_and_preprocess_comments('komentar.json', 'komentar_bersih.txt')
    tfidf_vectors = compute_tfidf_vectors(komen_bersih)
    test_sentences = [
        "sebaiknya waktu kuliahnya jangan terlalu sore",
        "lebih keras lagi suara",
        "buku rujukan kurang jelas mau pakai mana"
    ]
    find_similar_comments(test_sentences, tfidf_vectors, komen_bersih)