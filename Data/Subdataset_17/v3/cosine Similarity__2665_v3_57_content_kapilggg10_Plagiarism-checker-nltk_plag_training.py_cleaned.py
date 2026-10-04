import os
import string
from nltk.tokenize import word_tokenize
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
def read_files(directory_path):
    file_contents = []
    filenames = []
    for subdir, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(subdir, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation))
                file_contents.append(text)
                filenames.append(file)
    return file_contents, filenames
def train_tfidf_vectorizer(directory_path):
    file_contents, filenames = read_files(directory_path)
    tfidf_vectorizer = TfidfVectorizer(tokenizer=preprocessing, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(file_contents)
    return tfidf_vectorizer, tfidf_matrix, filenames
def main():
    directory_path = 'C:\\Users\\Kapil Goyal\\Desktop\\nlp_assignment\\files'
    tfidf_vectorizer, tfidf_matrix, files = train_tfidf_vectorizer(directory_path)
    print(f"Filenames: {files}")
    print(f"TF-IDF Matrix:\n{tfidf_matrix.toarray()}")
if __name__ == "__main__":
    main()