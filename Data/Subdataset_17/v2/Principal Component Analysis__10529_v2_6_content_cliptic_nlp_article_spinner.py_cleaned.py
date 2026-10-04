from __future__ import print_function, division
from future.utils import iteritems
from builtins import range
import nltk
import random
from bs4 import BeautifulSoup
def read_positive_reviews(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return BeautifulSoup(file.read(), 'html.parser').findAll('review_text')
def construct_trigrams(reviews):
    trigrams = {}
    for review in reviews:
        tokens = nltk.tokenize.word_tokenize(review.text.lower())
        for i in range(len(tokens) - 2):
            k = (tokens[i], tokens[i+2])
            if k not in trigrams:
                trigrams[k] = []
            trigrams[k].append(tokens[i+1])
    return trigrams
def calculate_trigram_probabilities(trigrams):
    trigram_probabilities = {}
    for k, words in iteritems(trigrams):
        if len(set(words)) > 1:
            word_count = {}
            total_count = 0
            for w in words:
                if w not in word_count:
                    word_count[w] = 0
                word_count[w] += 1
                total_count += 1
            word_probabilities = {w: float(c) / total_count for w, c in iteritems(word_count)}
            trigram_probabilities[k] = word_probabilities
    return trigram_probabilities
def random_sample(d):
    r = random.random()
    cumulative = 0
    for w, p in iteritems(d):
        cumulative += p
        if r < cumulative:
            return w
def test_spinner(reviews, trigram_probabilities):
    review = random.choice(reviews)
    original_text = review.text.lower()
    print("Original:", original_text)
    tokens = nltk.tokenize.word_tokenize(original_text)
    for i in range(len(tokens) - 2):
        if random.random() < 0.2:
            k = (tokens[i], tokens[i+2])
            if k in trigram_probabilities:
                tokens[i+1] = random_sample(trigram_probabilities[k])
    spun_text = " ".join(tokens).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!")
    print("Spun:")
    print(spun_text)
if __name__ == '__main__':
    filepath = 'electronics/positive.review'
    positive_reviews = read_positive_reviews(filepath)
    trigrams = construct_trigrams(positive_reviews)
    trigram_probabilities = calculate_trigram_probabilities(trigrams)
    test_spinner(positive_reviews, trigram_probabilities)