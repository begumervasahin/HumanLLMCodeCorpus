import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures
from string import punctuation
def read_reviews_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        reviews = [line[3] for line in csv_reader]
    return reviews
def tokenize_and_stem(texts):
    ps = PorterStemmer()
    stemmed_texts = []
    for text in texts:
        tokens = word_tokenize(text)
        stemmed = [ps.stem(word) for word in tokens]
        stemmed_texts.append(stemmed)
    return stemmed_texts
def remove_stopwords(texts):
    stop_words = set(stopwords.words('english'))
    filtered_texts = []
    for text in texts:
        filtered = [word for word in text if word not in stop_words]
        filtered_texts.append(filtered)
    return filtered_texts
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_words = [word for word in tokens if word not in stop_words and word not in punctuation]
    return filtered_words
def most_common_words(texts, n=10):
    preprocessed_text = preprocess(' '.join(texts))
    return FreqDist(preprocessed_text).most_common(n)
def find_freq_ngrams(texts, n, frequency, top_n=10):
    ngrams = [tuple(text[i:i+n]) for text in texts for i in range(len(text)-(n-1))]
    freq_dist = FreqDist(ngrams)
    return [ng for ng, freq in freq_dist.items() if freq == frequency][:top_n]
def score_bigrams(texts):
    bgm = BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(' '.join(texts))
    scored = finder.score_ngrams(bgm.likelihood_ratio)
    return [score[0] for score in scored]
def most_common_tags_and_pronouns(text):
    tokens = word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    tag_freq = FreqDist(tag for _, tag in tagged_tokens)
    most_common_tags = tag_freq.most_common()
    pronouns = [word for (word, tag) in tagged_tokens if tag == 'PRP']
    return most_common_tags, pronouns
if __name__ == "__main__":
    reviews_list = read_reviews_from_csv('rev.csv')
    stemmed_reviews = tokenize_and_stem(reviews_list)
    filtered_reviews = remove_stopwords(stemmed_reviews)
    print("Most common words:", most_common_words(filtered_reviews))
    print("Frequent bigrams:", find_freq_ngrams(filtered_reviews, 2, 2))
    print("Scored bigrams:", score_bigrams(filtered_reviews))
    tags, pronouns = most_common_tags_and_pronouns(' '.join(reviews_list))
    print("Most common POS tags:", tags)
    print("Pronouns:", pronouns)