import base64
import csv
import gensim
import stop_words
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
def cosine_sim(text1, text2):
    vectorizer = TfidfVectorizer(min_df=1, stop_words='danish')
    tfidf = vectorizer.fit_transform([text1, text2])
    return (tfidf * tfidf.T).A[0, 1]
def write_csv_file_from_text_dict(outpath, datadict):
    with open(outpath, "w", newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile, delimiter=';', dialect='excel')
        for i, (text, dfs) in enumerate(datadict.items()):
            row = [str(i), text, str(dfs)]
            csv_writer.writerow(row)
def filter_words_in_documents(documents):
    stopwords = stop_words.get_stop_words('danish')
    texts = [[word for word in document.lower().split() if word not in stopwords] for document in documents]
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    filtered_texts = [[token for token in text if frequency[token] > 1] for text in texts]
    filtered_texts = [text for text in filtered_texts if text]
    return filtered_texts
def create_dictionary(texts):
    return gensim.corpora.Dictionary(texts)
def create_corpus(dictionary, texts):
    return [dictionary.doc2bow(text) for text in texts]
def decrypt_text(text, cipher):
    try:
        return cipher.decrypt(base64.b64decode(text)).decode('utf-8')
    except Exception as e:
        print(f"Decryption failed: {e}")
        return ''