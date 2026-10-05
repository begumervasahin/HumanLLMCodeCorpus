import base64
import csv
import gensim
from gensim import corpora
from gensim.models import TfidfModel
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import stop_words
def cosine_similarity(text1, text2):
    stop_words_da = set(stopwords.words('danish'))
    vectorizer = TfidfVectorizer(min_df=1, stop_words=stop_words_da)
    tfidf = vectorizer.fit_transform([text1, text2])
    similarity = ((tfidf * tfidf.T).A)[0, 1]
    return similarity
def write_csv_file(outpath, datadict):
    with open(outpath, "w", newline='') as outfile:
        csv_writer = csv.writer(outfile, delimiter=';', dialect='excel')
        for key, value in datadict.items():
            encoded_data = value.encode('utf-8')
            row = [str(key), encoded_data, str(datadict.dfs[key])]
            csv_writer.writerow(row)
def filter_words(documents):
    stop_words_list = stop_words.get_stop_words('danish')
    filtered_texts = [[word for word in document.lower().split() if word not in stop_words_list] for document in documents]
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in filtered_texts:
        for token in text:
            frequency[token] += 1
    filtered_texts = [[token for token in text if frequency[token] > 1] for text in filtered_texts]
    filtered_texts = [text for text in filtered_texts if text]
    return filtered_texts
def create_dict(texts):
    return corpora.Dictionary(texts)
def create_bow_corpus(dictionary, texts):
    return [dictionary.doc2bow(text) for text in texts]
def decrypt(text, cipher):
    try:
        decrypted = cipher.decrypt(base64.b64decode(text))
        return decrypted
    except Exception as e:
        print(e)
        return ''
text1 = "This is a sample text for cosine similarity."
text2 = "A similar text for testing cosine similarity."
similarity_score = cosine_similarity(text1, text2)
print("Cosine Similarity Score:", similarity_score)
documents = ["Sample document 1 for filtering words.",
             "Another document with words to filter out."]
filtered_texts = filter_words(documents)
print("Filtered Texts:", filtered_texts)
dictionary = create_dict(filtered_texts)
print("Dictionary:", dictionary)
bow_corpus = create_bow_corpus(dictionary, filtered_texts)
print("Bag of Words Corpus:", bow_corpus)
cipher = base64.b64encode(b'encryption_key')
encrypted_text = base64.b64encode(b'Hello, World!').decode('utf-8')
decrypted_text = decrypt(encrypted_text, cipher)
print("Decrypted Text:", decrypted_text)