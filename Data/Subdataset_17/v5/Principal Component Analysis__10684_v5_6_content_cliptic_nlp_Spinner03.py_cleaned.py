import nltk
import random
from bs4 import BeautifulSoup
def read_reviews(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    return soup.findAll("review_text")
def build_trigrams(reviews):
    trigrams = {}
    for review in reviews:
        review_text = review.text.lower()
        tokens = nltk.tokenize.word_tokenize(review_text)
        for i in range(len(tokens) - 3):
            key = (tokens[i], tokens[i + 2])
            if key not in trigrams:
                trigrams[key] = []
            trigrams[key].append(tokens[i + 1])
    return trigrams
def calculate_probabilities(trigrams):
    probabilities = {}
    for key, words in trigrams.items():
        if len(set(words)) > 1:
            word_counts = {word: words.count(word) for word in set(words)}
            total_count = sum(word_counts.values())
            probabilities[key] = {word: count / total_count for word, count in word_counts.items()}
    return probabilities
def random_sample(prob_dist):
    rand_val = random.random()
    cumulative_prob = 0
    for word, prob in prob_dist.items():
        cumulative_prob += prob
        if rand_val < cumulative_prob:
            return word
def spin_review(review, probabilities):
    review_text = review.text.lower()
    tokens = nltk.tokenize.word_tokenize(review_text)
    for i in range(len(tokens) - 3):
        if random.random() < 0.85:
            key = (tokens[i], tokens[i + 2])
            if key in probabilities:
                new_word = random_sample(probabilities[key])
                if nltk.pos_tag([new_word])[0][1] == nltk.pos_tag([tokens[i + 1]])[0][1]:
                    tokens[i + 1] = new_word
    spun_text = ' '.join(tokens)
    return spun_text.replace(" :", ":").replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace("  ' ", "'")
def test_spinner(reviews, probabilities):
    review = random.choice(reviews)
    print('Original text:\n', review.text.lower())
    spun_text = spin_review(review, probabilities)
    print("Spun text:\n", spun_text)
file_path = 'electronics/positive.review'
positive_reviews = read_reviews(file_path)
trigrams = build_trigrams(positive_reviews)
probabilities = calculate_probabilities(trigrams)
test_spinner(positive_reviews, probabilities)