from collections import Counter
TRAIN_SIZE = 6000
TEST_SIZE = 15000
TRAIN_FILE = "news_train.txt"
TEST_FILE = "news_test.txt"
class NaiveBayesClassifier:
    def __init__(self):
        self.categories = []
        self.contents = []
        self.unique_categories = []
        self.vocabulary = []
        self.total_words_per_category = []
        self.total_words_dict = {}
        self.vocabulary_length = 0
    def read_training_data(self):
        with open(TRAIN_FILE, encoding='utf-8') as file:
            articles = file.readlines()
            for article in articles:
                category, content = article.split("\t", 1)
                self.categories.append(category)
                self.contents.append(content.strip())
    def index_select(self, category_name):
        return [i for i, cat in enumerate(self.categories) if cat == category_name]
    def words_and_vocabulary(self, category):
        total_words = 0
        vocabulary = []
        for i in self.index_select(category):
            train_dict = dict(Counter(self.contents[i].split()))
            total_words += len(train_dict.keys())
            vocabulary.extend(train_dict.keys())
        return total_words, list(set(vocabulary))
    def compute_vocabulary_and_total_words(self):
        for category_name in self.unique_categories:
            total_words, vocab = self.words_and_vocabulary(category_name)
            self.vocabulary.extend(vocab)
            self.total_words_per_category.append(total_words)
    def compute_prior_probability(self, category):
        return len(self.index_select(category)) / len(self.categories)
    def compute_common_words(self, category, test_dict):
        test_counts = Counter(test_dict)
        test_counts.update({word: 0 for word in self.vocabulary})
        for i in self.index_select(category):
            train_dict = dict(Counter(self.contents[i].split()))
            for word in train_dict:
                if word in test_counts:
                    test_counts[word] += train_dict[word]
        return test_counts
    def compute_conditional_probability(self, test_counts, category):
        conditional_probabilities = {}
        for word, count in test_counts.items():
            conditional_probabilities[word] = 10000 * (count + 1) / (self.total_words_dict[category] + self.vocabulary_length)
        return conditional_probabilities
    def classify_article(self, test_dict):
        probabilities = []
        for category_name in self.unique_categories:
            test_counts = self.compute_common_words(category_name, test_dict)
            conditional_probs = self.compute_conditional_probability(test_counts, category_name)
            probability = 1
            for word, cond_prob in conditional_probs.items():
                probability *= cond_prob
            probability *= self.compute_prior_probability(category_name)
            probabilities.append(probability)
        max_probability, max_index = max((prob, idx) for (idx, prob) in enumerate(probabilities))
        return self.unique_categories[max_index]
    def classify_test_articles(self):
        test_contents = []
        with open(TEST_FILE, encoding='utf-8') as file:
            test_articles = file.readlines()
        with open('answer.txt', 'w', encoding="utf8") as answer_file:
            for article in test_articles:
                test_dict = Counter(article.split())
                predicted_category = self.classify_article(test_dict)
                answer_file.write(predicted_category + '\n')
    def train_classifier(self):
        self.unique_categories = list(set(self.categories))
        self.compute_vocabulary_and_total_words()
        self.total_words_dict = dict(zip(self.unique_categories, self.total_words_per_category))
        self.vocabulary_length = len(set(self.vocabulary))
if __name__ == '__main__':
    classifier = NaiveBayesClassifier()
    classifier.read_training_data()
    classifier.train_classifier()
    classifier.classify_test_articles()