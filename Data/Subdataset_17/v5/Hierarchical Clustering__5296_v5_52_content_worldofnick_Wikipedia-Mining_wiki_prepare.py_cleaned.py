import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, ngrams
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import glob
import os
nltk.download('punkt')
nltk.download('stopwords')
def extract_kgrams(text, k):
    tokens = word_tokenize(text)
    kgrams = {' '.join(gram) for gram in ngrams(tokens, k)}
    return kgrams
def vectorize_article(text, ngram_range=(3, 3)):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    count_vectorizer = CountVectorizer(ngram_range=ngram_range)
    bag_of_words = count_vectorizer.fit_transform([' '.join(filtered_tokens)])
    tfidf_transformer = TfidfTransformer()
    tfidf_matrix = tfidf_transformer.fit_transform(bag_of_words)
    return tfidf_matrix.toarray()
def save_kgrams(kgrams, article_name):
    output_filename = f'{article_name}_kgrams.txt'
    with open(output_filename, "w") as f:
        f.write(",".join(kgrams))
def process_text_files(file_pattern, k=3):
    text_files = glob.glob(file_pattern)
    for filepath in text_files:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            kgrams = extract_kgrams(text, k)
            tfidf_vector = vectorize_article(text, ngram_range=(k, k))
            base_filename = os.path.splitext(os.path.basename(filepath))[0]
            save_kgrams(kgrams, base_filename)
if __name__ == "__main__":
    process_text_files('/somePath/*.txt', k=3)