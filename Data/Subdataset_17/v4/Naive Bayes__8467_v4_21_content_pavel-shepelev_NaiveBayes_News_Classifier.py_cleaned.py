from collections import Counter
TRAIN_SIZE = 6000
TEST_SIZE = 15000
TRAIN_FILE = "news_train.txt"
TEST_FILE = "news_test.txt"
OUTPUT_FILE = "answer.txt"
categories = []
contents = []
with open(TRAIN_FILE, encoding='utf-8') as f:
    articles = f.readlines()
    for article in articles:
        category, content = article.split("\t", 1)
        categories.append(category)
        contents.append(content.strip())
unique_categories = list(set(categories))
def index_select(name):
    indices = [i for i in range(TRAIN_SIZE) if categories[i] == name]
    return indices
def common_words(category, test_dict):
    test_counts = dict.fromkeys(test_dict, 0)
    for i in index_select(category):
        train_dict = Counter(contents[i].split())
        for word, count in train_dict.items():
            if word in test_dict:
                test_counts[word] += count
    return test_counts
def prior(category):
    return len(index_select(category)) / len(categories)
def words_and_vocabulary(category):
    total_words = 0
    vocabulary = set()
    for i in index_select(category):
        train_dict = Counter(contents[i].split())
        total_words += len(train_dict)
        vocabulary.update(train_dict.keys())
    return total_words, vocabulary
total_words = {}
vocabulary = set()
for category in unique_categories:
    words, vocab = words_and_vocabulary(category)
    vocabulary.update(vocab)
    total_words[category] = words
vocabulary_length = len(vocabulary)
print(f"Vocabulary length: {vocabulary_length}")
print(f"Total words: {total_words}")
def main(test_dict):
    probabilities = []
    for category in unique_categories:
        test_counts = common_words(category, test_dict)
        cond_prob = {word: (test_counts[word] + 1) / (total_words[category] + vocabulary_length) for word in test_counts}
        probability = prior(category)
        for word in cond_prob:
            probability *= cond_prob[word]
        probabilities.append(probability)
    best_prob = max(probabilities)
    best_category = unique_categories[probabilities.index(best_prob)]
    return best_category
with open(TEST_FILE, encoding='utf-8') as f:
    test_articles = f.readlines()
with open(OUTPUT_FILE, 'w', encoding="utf-8") as answer_file:
    for i in range(TEST_SIZE):
        test_dict = Counter(test_articles[i].split())
        predicted_category = main(test_dict)
        answer_file.write(predicted_category + '\n')
print("Classification completed and results written to", OUTPUT_FILE)