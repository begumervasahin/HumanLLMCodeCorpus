from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.util import ngrams
import glob
def word_kgrams(text, k):
    grams = ngrams(text.split(), k)
    gram_set = {' '.join(gram) for gram in grams}
    return gram_set
def vectorize_article(text):
    words = nltk.word_tokenize(text)
    stops = set(stopwords.words("english"))
    filtered_article = [word for word in words if word not in stops]
    count_vectorizer = CountVectorizer(ngram_range=(3, 3))
    bag_of_words = count_vectorizer.fit_transform(filtered_article)
    tfidf_transformer = TfidfTransformer()
    tfidf_matrix = tfidf_transformer.fit_transform(bag_of_words)
    return tfidf_matrix.toarray()
def save_kgrams(kgrams, article_name):
    with open(f'{article_name}_kgrams.txt', "w") as f:
        f.write(",".join(map(str, kgrams)))
text_files = glob.glob('/somePath/*.txt')
for file_name in text_files:
    with open(file_name) as file:
        article_text = file.read()
        article_kgrams = vectorize_article(article_text)
        save_kgrams(article_kgrams, file_name)