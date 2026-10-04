import nltk
import random
from bs4 import BeautifulSoup
with open('electronics/positive.review', 'r') as file:
    positive_reviews = BeautifulSoup(file.read(), 'html.parser')
positive_reviews = positive_reviews.findAll("review_text")
trigrams = {}
for review in positive_reviews:
    review_text = review.text.lower()
    tokens = nltk.tokenize.word_tokenize(review_text)
    for i in range(len(tokens) - 3):
        key = (tokens[i], tokens[i + 2])
        if key not in trigrams:
            trigrams[key] = []
        trigrams[key].append(tokens[i + 1])
probabilities = {}
for key, words in trigrams.items():
    if len(set(words)) > 1:
        word_counts = {}
        total_count = 0
        for word in words:
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1
            total_count += 1
        probabilities[key] = {word: count / total_count for word, count in word_counts.items()}
def random_sample(prob_dist):
    rand_val = random.random()
    cumulative_prob = 0
    for word, prob in prob_dist.items():
        cumulative_prob += prob
        if rand_val < cumulative_prob:
            return word
def test_spinner():
    review = random.choice(positive_reviews).text.lower()
    print('Original text:\n', review)
    tokens = nltk.tokenize.word_tokenize(review)
    for i in range(len(tokens) - 3):
        if random.random() < 0.85:
            key = (tokens[i], tokens[i + 2])
            if key in probabilities:
                new_word = random_sample(probabilities[key])
                if nltk.pos_tag([new_word])[0][1] == nltk.pos_tag([tokens[i + 1]])[0][1]:
                    tokens[i + 1] = new_word
    spun_text = ' '.join(tokens)
    spun_text = spun_text.replace(" :", ":").replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace("  ' ", "'")
    print("Spun text:\n", spun_text)
test_spinner()