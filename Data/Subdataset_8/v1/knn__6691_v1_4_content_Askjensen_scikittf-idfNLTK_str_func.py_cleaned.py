import base64
import csv
import gensim
import stop_words
from gensim import corpora
from gensim.models import TfidfModel
from nltk.corpus import stopwords
def cosine_sim(text1, text2):
    stop_words = set(stopwords.words('danish'))
    vectorizer = TfidfVectorizer(min_df=1, stop_words=stop_words)
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]
def write_csv_file_from_text_dict(outpath, datadict):
    with open(outpath, "w", newline='') as outfile:
        csv_file = csv.writer(outfile, delimiter=';', dialect='excel')
        for i, data in datadict.items():
            row = [str(i), data.encode('utf-8'), str(datadict.dfs[i])]
            csv_file.writerow(row)
def filter_words_in_documents(documents):
    stop_words_list = stop_words.get_stop_words('danish')
    texts = [[word for word in document.lower().split() if word not in stop_words_list] for document in documents]
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]
    texts = [itxt for itxt in texts if itxt]
    return texts
def create_dictionary(texts):
    return corpora.Dictionary(texts)
def create_corpus(dictionary, texts):
    return [dictionary.doc2bow(text) for text in texts]
def decrypt_text(text, cipher):
    try:
        return cipher.decrypt(base64.b64decode(text))
    except Exception as e:
        print(e)
        return ''
text1 = "This is a sample text for cosine similarity."
text2 = "A similar text for testing cosine similarity."
similarity_score = cosine_sim(text1, text2)
print("Cosine Similarity Score:", similarity_score)
documents = ["Sample document 1 for filtering words.",
             "Another document with words to filter out."]
filtered_texts = filter_words_in_documents(documents)
print("Filtered Texts:", filtered_texts)
dictionary = create_dictionary(filtered_texts)
print("Dictionary:", dictionary)
corpus = create_corpus(dictionary, filtered_texts)
print("Corpus:", corpus)
cipher = base64.b64encode(b'encryption_key')
encrypted_text = base64.b64encode(b'Hello, World!').decode('utf-8')
decrypted_text = decrypt_text(encrypted_text, cipher)
print("Decrypted Text:", decrypted_text)