import math
import numpy as np
import nltk
import json
import yaml
import Preprocessing as pp
import TF_IDF as tfidf
import CosineSimilarity as cs
STOPWORDS = [
    'em', 'gonna', 'huh', 'yep', 'goin', 'hi', 'inaudible', 'crosstalk', 'laughter',
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself',
    'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
    'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be',
    'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
    'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',
    'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
    'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',
    'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
    'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o',
    're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma',
    'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'
]
def preprocess_text(text):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word not in STOPWORDS]
    stemmer = nltk.PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    return stemmed_tokens
def load_and_preprocess_comments(json_path, txt_path):
    with open(json_path, 'r') as output_file:
        komentar = yaml.safe_load(output_file)
    with open(txt_path, 'r') as komentar_bersih:
        data = komentar_bersih.read().split('\n')
    komen_bersih = [preprocess_text(komen) for komen in data if komen]
    return komentar, komen_bersih
def compute_tfidf_vectors(comments):
    return [tfidf.TFIDF(' '.join(comment)) for comment in comments]
def find_similar_comments(test_sentences, tfidf_vectors, comments):
    for test in test_sentences:
        print('---------------------------------------------------------------------------------------')
        print('Data Testing:', test)
        input_vector = tfidf.TFIDF(' '.join(preprocess_text(test)))
        results = []
        for i, vector in enumerate(tfidf_vectors):
            similarity_score = cs.similarity(input_vector, vector)
            results.append((i, similarity_score, ' '.join(comments[i])))
        best_match = sorted(results, key=lambda x: x[1], reverse=True)[0]
        print('Best Match:', best_match)
        print('------------------------------------------------------------------------')
        for index, cosine, comment in results:
            if cosine >= 0.93:
                print(cosine, comment)
if __name__ == "__main__":
    komentar, komen_bersih = load_and_preprocess_comments('komentar.json', 'komentar_bersih.txt')
    tfidf_vectors = compute_tfidf_vectors(komen_bersih)
    test_sentences = [
        "sebaiknya waktu kuliahnya jangan terlalu sore",
        "lebih keras lagi suara",
        "buku rujukan kurang jelas mau pakai mana"
    ]
    find_similar_comments(test_sentences, tfidf_vectors, komen_bersih)