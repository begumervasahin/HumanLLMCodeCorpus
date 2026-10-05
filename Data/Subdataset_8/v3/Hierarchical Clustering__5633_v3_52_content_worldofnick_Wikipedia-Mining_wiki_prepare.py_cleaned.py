import glob
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def generate_word_kgrams(text, k):
    grams = ngrams(text.split(), k)
    gram_set = {' '.join(gram) for gram in grams}
    return gram_set
def vectorize_text(text):
    words = nltk.word_tokenize(text)
    stops = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stops]
    count_vectorizer = CountVectorizer(ngram_range=(3, 3))
    bag_of_words = count_vectorizer.fit_transform(filtered_words)
    tfidf_transformer = TfidfTransformer()
    tfidf_matrix = tfidf_transformer.fit_transform(bag_of_words)
    return tfidf_matrix.toarray()
def save_kgrams(kgrams, file_name):
    with open(f'{file_name}_kgrams.txt', "w") as file:
        file.write(",".join(map(str, kgrams)))
text_files = glob.glob('/somePath/*.txt')
for file_name in text_files:
    with open(file_name) as file:
        article_text = file.read()
        article_kgrams = vectorize_text(article_text)
        save_kgrams(article_kgrams, file_name)