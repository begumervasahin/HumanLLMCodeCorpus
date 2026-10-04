from collections import Counter
TRAIN_SIZE = 6000
TEST_SIZE = 15000
TRAIN_FILE = "news_train.txt"
TEST_FILE = "news_test.txt"
OUTPUT_FILE = "answer.txt"
def load_data(file_path):
    categories = []
    contents = []
    with open(file_path, encoding='utf-8') as file:
        articles = file.readlines()
        for article in articles:
            category, content = article.split("\t", 1)
            categories.append(category)
            contents.append(content.strip())
    return categories, contents
categories, contents = load_data(TRAIN_FILE)
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
def compute_category_stats():
    overall_vocab = set()
    category_word_counts = []
    for category_name in category_names:
        total_words, category_vocab = words_and_vocabulary(category_name)
        overall_vocab.update(category_vocab)
        category_word_counts.append(total_words)
    return overall_vocab, dict(zip(category_names, category_word_counts))
overall_vocab, total_words_per_category = compute_category_stats()
vocab_length = len(overall_vocab)
def classify(test_dict):
    probabilities = []
    for category_name in category_names:
        test_counts = common_words_count(category_name, test_dict)
        probability = prior_probability(category_name)
        for word in test_dict:
            word_prob = (test_counts.get(word, 0) + 1) / (total_words_per_category[category_name] + vocab_length)
            probability *= word_prob
        probabilities.append(probability)
    return category_names[probabilities.index(max(probabilities))]
def classify_test_data():
    with open(TEST_FILE, encoding='utf-8') as file:
        test_articles = file.readlines()
    with open(OUTPUT_FILE, 'w', encoding="utf-8") as answer_file:
        for i in range(TEST_SIZE):
            test_dict = Counter(test_articles[i].split())
            predicted_category = classify(test_dict)
            answer_file.write(predicted_category + '\n')
    print(f"Classification completed. Results written to {OUTPUT_FILE}")
if __name__ == '__main__':
    classify_test_data()