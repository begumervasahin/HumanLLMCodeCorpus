import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures
from string import punctuation
from collections import defaultdict
with open('rev.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    reviewsList = [line[3] for line in csv_reader]
ps = PorterStemmer()
stemsList = []
for review in reviewsList:
    tokens = word_tokenize(review)
    stems = [ps.stem(word) for word in tokens]
    stemsList.append(stems)
stop_words = set(stopwords.words('english'))
filteredReviews = []
for stems in stemsList:
    filtered_words = [word for word in stems if word not in stop_words]
    filteredReviews.append(filtered_words)
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_words = [word for word in tokens if word not in stop_words and word not in punctuation]
    return filtered_words
reviewsText = ' '.join(reviewsList)
preprocessedText = preprocess(reviewsText)
most_common_words = FreqDist(preprocessedText).most_common(10)
def list_ngrams(lst, n):
    return [tuple(lst[i:i+n]) for i in range(len(lst)-(n-1))]
def list_freq_ngrams(lst, frequency, n):
    freq_dist = FreqDist(lst)
    return [ng for ng, freq in freq_dist.items() if freq == frequency][:n]
bigram_list = list_ngrams(preprocessedText, 2)
freq_bigram_list = list_freq_ngrams(bigram_list, 2, 10)
def score_bigrams(bigrams):
    bgm = BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(bigrams)
    scored = finder.score_ngrams(bgm.likelihood_ratio)
    return [score[0] for score in scored]
scored_bigram_list = score_bigrams(freq_bigram_list)
text_tokens = word_tokenize(reviewsText)
tagged_list = nltk.pos_tag(text_tokens)
tag_freq = FreqDist(tag for _, tag in tagged_list)
most_common_tags = tag_freq.most_common()
pronouns = [word for (word, tag) in tagged_list if tag == 'PRP']
print("Most common words:", most_common_words)
print("Most common POS tags:", most_common_tags)
print("Pronouns:", pronouns)