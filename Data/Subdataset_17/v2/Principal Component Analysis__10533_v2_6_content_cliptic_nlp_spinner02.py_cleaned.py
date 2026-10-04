import nltk
import random
from bs4 import BeautifulSoup
nltk.download('punkt')
def load_positive_reviews(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    return [review.text.lower() for review in soup.findAll("review_text")]
def generate_trigrams(reviews):
    trigrams = {}
    for review in reviews:
        tokens = nltk.tokenize.word_tokenize(review)
        for i in range(len(tokens) - 2):
            k = (tokens[i], tokens[i + 2])
            if k not in trigrams:
                trigrams[k] = []
            trigrams[k].append(tokens[i + 1])
    return trigrams
def calculate_probabilities(trigrams):
    probabilities = {}
    for k, words in trigrams.items():
        if len(set(words)) > 1:
            word_counts = {w: words.count(w) for w in set(words)}
            total_words = sum(word_counts.values())
            probabilities[k] = {w: count / total_words for w, count in word_counts.items()}
    return probabilities
def random_sample(probabilities):
    r = random.random()
    cumulative = 0
    for word, prob in probabilities.items():
        cumulative += prob
        if r < cumulative:
            return word
def test_spinner(reviews, probabilities):
    review = random.choice(reviews)
    print('Original text: \n', review)
    tokens = nltk.tokenize.word_tokenize(review)
    for i in range(len(tokens) - 2):
        if random.random() < 0.2:
            k = (tokens[i], tokens[i + 2])
            if k in probabilities:
                tokens[i + 1] = random_sample(probabilities[k])
    spun_text = ' '.join(tokens).replace(" :", ":").replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace("  ' ", "'")
    print("Spun: \n", spun_text)
def main():
    filepath = 'electronics/positive.review'
    reviews = load_positive_reviews(filepath)
    trigrams = generate_trigrams(reviews)
    probabilities = calculate_probabilities(trigrams)
    test_spinner(reviews, probabilities)
if __name__ == "__main__":
    main()