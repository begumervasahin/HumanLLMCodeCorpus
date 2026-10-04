import base64
import csv
import gensim
from stop_words import get_stop_words
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
def cosine_sim(text1, text2):
    vectorizer = TfidfVectorizer(min_df=1, stop_words='danish')
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]
def writeCSVfileFromTextDict(outpath, datadict):
    with open(outpath, "w", newline='', encoding='utf-8') as outfile:
        csv_file = csv.writer(outfile, delimiter=';', dialect='excel')
        for i in range(len(datadict)):
            row = [str(i), datadict[i].encode('utf-8'), str(datadict.dfs[i])]
            csv_file.writerow(row)
def filterWordsInDocuments(documents):
    stopwords = get_stop_words('danish')
    texts = [[word for word in document.lower().split() if word not in stopwords] for document in documents]
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]
    texts = [itxt for itxt in texts if itxt]
    return texts
def createDictionary(texts):
    return gensim.corpora.Dictionary(texts)
def createCorpus(dictionary, texts):
    return [dictionary.doc2bow(text) for text in texts]
def decrypt_text(text, cipher):
    try:
        return cipher.decrypt(base64.b64decode(text))
    except:
        return ''
if __name__ == "__main__":
    text1 = "Dette er en test tekst."
    text2 = "Dette er en anden test tekst."
    similarity = cosine_sim(text1, text2)
    print(f"Cosine similarity: {similarity}")
    datadict = {0: "text1", 1: "text2"}
    datadict.dfs = [0.5, 0.8]
    writeCSVfileFromTextDict("output.csv", datadict)
    documents = ["Dette er et dokument.", "Dette er et andet dokument."]
    filtered_texts = filterWordsInDocuments(documents)
    print(f"Filtered texts: {filtered_texts}")
    dictionary = createDictionary(filtered_texts)
    corpus = createCorpus(dictionary, filtered_texts)
    print(f"Dictionary: {dictionary.token2id}")
    print(f"Corpus: {corpus}")
