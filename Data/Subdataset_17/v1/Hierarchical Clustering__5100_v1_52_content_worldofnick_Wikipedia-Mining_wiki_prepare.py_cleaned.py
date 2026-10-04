import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, ngrams
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import glob
nltk.download('punkt')
nltk.download('stopwords')
def extract_kgrams(text, k):
    tokens = word_tokenize(text)
    grams = ngrams(tokens, k)
    gram_set = set(' '.join(gram) for gram in grams)
    return gram_set
def vectorize_article(text, ngram_range=(3, 3)):
    words = word_tokenize(text)
    stops = set(stopwords.words("english"))
    filtered_article = [word for word in words if word.lower() not in stops]
    count_vectorizer = CountVectorizer(ngram_range=ngram_range)
    bag_of_words = count_vectorizer.fit_transform([' '.join(filtered_article)])
    tfidf_transformer = TfidfTransformer()
    tfidf_matrix = tfidf_transformer.fit_transform(bag_of_words)
    return tfidf_matrix.toarray()
def save_kgrams(kgrams, article_name):
    with open(f'{article_name}_kgrams.txt', "w") as f:
        f.write(",".join(map(str, kgrams)))
def process_text_files(file_pattern, k=3):
    text_files = glob.glob(file_pattern)
    for filename in text_files:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            article_kgrams = extract_kgrams(text, k)
            tfidf_vector = vectorize_article(text, ngram_range=(k, k))
            save_kgrams(article_kgrams, filename)
if __name__ == "__main__":
    process_text_files('/somePath/*.txt', k=3)