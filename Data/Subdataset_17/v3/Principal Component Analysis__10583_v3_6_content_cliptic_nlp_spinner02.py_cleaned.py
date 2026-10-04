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
            trigram_key = (tokens[i], tokens[i + 2])
            if trigram_key not in trigrams:
                trigrams[trigram_key] = []
            trigrams[trigram_key].append(tokens[i + 1])
    return trigrams
def calculate_probabilities(trigrams):
    probabilities = {}
    for trigram_key, words in trigrams.items():
        if len(set(words)) > 1:
            word_counts = {word: words.count(word) for word in set(words)}
            total_words = sum(word_counts.values())
            probabilities[trigram_key] = {word: count / total_words for word, count in word_counts.items()}
    return probabilities
def random_sample(probabilities):
    r = random.random()
    cumulative_probability = 0
    for word, probability in probabilities.items():
        cumulative_probability += probability
        if r < cumulative_probability:
            return word
def test_spinner(reviews, probabilities):
    review = random.choice(reviews)
    print('Original text: \n', review)
    tokens = nltk.tokenize.word_tokenize(review)
    for i in range(len(tokens) - 2):
        if random.random() < 0.2:
            trigram_key = (tokens[i], tokens[i + 2])
            if trigram_key in probabilities:
                tokens[i + 1] = random_sample(probabilities[trigram_key])
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