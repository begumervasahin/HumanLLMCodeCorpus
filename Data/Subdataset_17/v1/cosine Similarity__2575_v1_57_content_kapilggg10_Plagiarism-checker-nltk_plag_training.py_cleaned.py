import os
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
def get_tokenized(text):
    return word_tokenize(text)
def stemming(tokens, stemmer):
    return [stemmer.stem(token) for token in tokens]
def preprocessing(text):
    tokens = get_tokenized(text)
    stemmer = PorterStemmer()
    return stemming(tokens, stemmer)
def training_tfs(directory_path):
    file_contents = []
    filenames = []
    token_dictionary = {}
    for subdir, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(subdir, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                lowers = f.read().lower()
                no_punctuation = lowers.translate(str.maketrans('', '', string.punctuation))
                token_dictionary[file] = no_punctuation
                file_contents.append(no_punctuation)
                filenames.append(file)
    tfidf = TfidfVectorizer(tokenizer=preprocessing, stop_words='english')
    tfs = tfidf.fit_transform(file_contents)
    return tfidf, tfs, filenames
if __name__ == "__main__":
    directory_path = 'C:\\Users\\Kapil Goyal\\Desktop\\nlp_assignment\\files'
    tfidf_vectorizer, tfidf_matrix, files = training_tfs(directory_path)
    print(f"Filenames: {files}")
    print(f"TF-IDF Matrix: {tfidf_matrix.toarray()}")