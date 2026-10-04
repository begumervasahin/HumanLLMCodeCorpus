from collections import Counter
TRAIN_SIZE = 6000
TEST_SIZE = 15000
TRAIN_FILE = "news_train.txt"
TEST_FILE = "news_test.txt"
OUTPUT_FILE = "answer.txt"
categories = []
contents = []
with open(TRAIN_FILE, encoding='utf-8') as file:
    articles = file.readlines()
    for article in articles:
        category, content = article.split("\t", 1)
        categories.append(category)
        contents.append(content.strip())
category_names = list(set(categories))
def index_select(category_name):
    return [i for i in range(TRAIN_SIZE) if categories[i] == category_name]
def common_words_count(category_name, test_dict):
    test_counts = {word: 0 for word in test_dict}
    for i in index_select(category_name):
        train_dict = Counter(contents[i].split())
        for word in train_dict:
            if word in test_dict:
                test_counts[word] += train_dict[word]
    return test_counts
def prior_probability(category_name):
    return len(index_select(category_name)) / len(categories)
def words_and_vocabulary(category_name):
    total_words = 0
    vocab = set()
    for i in index_select(category_name):
        train_dict = Counter(contents[i].split())
        total_words += len(train_dict)
        vocab.update(train_dict.keys())
    return total_words, vocab
overall_vocab = set()
category_word_counts = []
for category_name in category_names:
    total_words, category_vocab = words_and_vocabulary(category_name)
    overall_vocab.update(category_vocab)
    category_word_counts.append(total_words)
total_words_per_category = dict(zip(category_names, category_word_counts))
vocab_length = len(overall_vocab)
def classify(test_dict):
    probabilities = []
    for category_name in category_names:
        test_counts = common_words_count(category_name, test_dict)
        conditional_probabilities = {word: 0 for word in test_counts}
        probability = 1
        for word in test_counts:
            conditional_probabilities[word] = (test_counts[word] + 1) / (total_words_per_category[category_name] + vocab_length)
            probability *= conditional_probabilities[word]
        probability *= prior_probability(category_name)
        probabilities.append(probability)
    return category_names[probabilities.index(max(probabilities))]
test_contents = []
with open(TEST_FILE, encoding='utf-8') as file:
    test_articles = file.readlines()
with open(OUTPUT_FILE, 'w', encoding="utf-8") as answer_file:
    for i in range(TEST_SIZE):
        test_dict = Counter(test_articles[i].split())
        predicted_category = classify(test_dict)
        answer_file.write(predicted_category + '\n')
print(f"Classification completed. Results written to {OUTPUT_FILE}")