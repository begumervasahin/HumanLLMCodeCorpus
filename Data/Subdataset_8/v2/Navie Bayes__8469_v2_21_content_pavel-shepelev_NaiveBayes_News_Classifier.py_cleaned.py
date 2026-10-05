from collections import Counter
TRAIN_SIZE = 6000
TEST_SIZE = 15000
TRAIN_FILE = "news_train.txt"
TEST_FILE = "news_test.txt"
categories = []
contents = []
with open(TRAIN_FILE, encoding='utf-8') as file:
    articles = file.readlines()
    for article in articles:
        category, content = article.split("\t", 1)
        categories.append(category)
        contents.append(content.strip())
unique_categories = list(set(categories))
def index_select(category_name):
    indices = []
    for i in range(TRAIN_SIZE):
        if categories[i] == category_name:
            indices.append(i)
    return indices
def common_words(category, test_dict):
    test_counts = dict.fromkeys(test_dict, 0)
    for i in index_select(category):
        train_dict = dict(Counter(contents[i].split()))
        for key in train_dict:
            if key in test_dict:
                test_counts[key] += train_dict[key]
    return test_counts
def prior_probability(category):
    return len(index_select(category)) / len(categories)
def words_and_vocabulary(category):
    total_words = 0
    vocabulary = []
    for i in index_select(category):
        train_dict = dict(Counter(contents[i].split()))
        total_words += len(train_dict.keys())
        vocabulary = list(set(vocabulary + list(train_dict.keys())))
    return total_words, vocabulary
vocabulary = []
total_words_per_category = []
for category_name in unique_categories:
    total_words, vocab = words_and_vocabulary(category_name)
    vocabulary = list(set(vocab + vocabulary))
    total_words_per_category.append(total_words)
total_words_dict = dict(zip(unique_categories, total_words_per_category))
vocabulary_length = len(vocabulary)
def classify(test_dict):
    probabilities = []
    for category_name in unique_categories:
        test_counts = common_words(category_name, test_dict)
        conditional_probabilities = dict.fromkeys(test_counts, 0)
        probability = 1
        for word in test_counts:
            conditional_probabilities[word] = 10000 * (test_counts[word] + 1) / (total_words_dict[category_name] + vocabulary_length)
            probability *= conditional_probabilities[word]
        probability *= prior_probability(category_name)
        probabilities.append(probability)
    max_probability, max_index = max((prob, idx) for (idx, prob) in enumerate(probabilities))
    return unique_categories[max_index]
test_contents = []
with open(TEST_FILE, encoding='utf-8') as file:
    test_articles = file.readlines()
with open('answer.txt', 'w', encoding="utf8") as answer_file:
    for article in test_articles:
        test_dict = dict(Counter(article.split()))
        predicted_category = classify(test_dict)
        answer_file.write(predicted_category + '\n')