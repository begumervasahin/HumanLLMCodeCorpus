from __future__ import print_function, division
from future.utils import iteritems
from builtins import range
import nltk
import random
import numpy as np
from bs4 import BeautifulSoup
def load_reviews(file_path):
    with open(file_path) as f:
        return BeautifulSoup(f.read(), 'html.parser').findAll('review_text')
def build_trigrams(reviews):
    trigrams = {}
    for review in reviews:
        review_text = review.text.lower()
        tokens = nltk.tokenize.word_tokenize(review_text)
        for i in range(len(tokens) - 2):
            key = (tokens[i], tokens[i + 2])
            if key not in trigrams:
                trigrams[key] = []
            trigrams[key].append(tokens[i + 1])
    return trigrams
def calculate_trigram_probabilities(trigrams):
    trigram_probabilities = {}
    for key, words in iteritems(trigrams):
        if len(set(words)) > 1:
            word_counts = {}
            total_count = 0
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
                total_count += 1
            word_probabilities = {word: float(count) / total_count for word, count in iteritems(word_counts)}
            trigram_probabilities[key] = word_probabilities
    return trigram_probabilities
def random_sample(probabilities):
    r = random.random()
    cumulative = 0
    for word, probability in iteritems(probabilities):
        cumulative += probability
        if r < cumulative:
            return word
def spin_text(review, trigram_probabilities, spin_chance=0.2):
    tokens = nltk.tokenize.word_tokenize(review.text.lower())
    for i in range(len(tokens) - 2):
        if random.random() < spin_chance:
            key = (tokens[i], tokens[i + 2])
            if key in trigram_probabilities:
                tokens[i + 1] = random_sample(trigram_probabilities[key])
    return " ".join(tokens).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!")
def test_spinner(reviews, trigram_probabilities):
    review = random.choice(reviews)
    original_text = review.text.lower()
    print("Original:", original_text)
    spun_text = spin_text(review, trigram_probabilities)
    print("Spun:", spun_text)
if __name__ == '__main__':
    reviews = load_reviews('electronics/positive.review')
    trigrams = build_trigrams(reviews)
    trigram_probabilities = calculate_trigram_probabilities(trigrams)
    test_spinner(reviews, trigram_probabilities)