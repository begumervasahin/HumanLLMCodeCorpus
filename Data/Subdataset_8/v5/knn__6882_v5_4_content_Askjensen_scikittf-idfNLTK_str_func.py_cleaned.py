import base64
import csv
import gensim
import stop_words
from sklearn.feature_extraction.text import TfidfVectorizer
def cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer(min_df=1, stop_words='danish')
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]
def write_csv_file(output_path, data_dict):
    with open(output_path, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', dialect='excel')
        for idx, (key, value) in enumerate(data_dict.items()):
            writer.writerow([str(idx), key, str(value)])
def filter_words(documents):
    stopwords = stop_words.get_stop_words('danish')
    texts = [[word for word in document.lower().split() if word not in stopwords] for document in documents]
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]
    texts = [txt for txt in texts if txt]
    return texts
def create_gensim_dictionary(texts):
    return gensim.corpora.Dictionary(texts)
def create_gensim_corpus(dictionary, texts):
    return [dictionary.doc2bow(text) for text in texts]
def decrypt_text(text, cipher):
    try:
        return cipher.decrypt(base64.b64decode(text))
    except Exception as e:
        return ''
