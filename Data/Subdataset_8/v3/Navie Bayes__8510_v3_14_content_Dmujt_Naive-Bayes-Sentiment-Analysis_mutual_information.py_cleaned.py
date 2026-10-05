import math
import operator
def format_data(files, label):
    data = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            tokens = content.split()
            data.append((tokens, label))
    return data
class SentimentNaiveBayes:
    def __init__(self):
        self.vocab = {}
        self.n = 0
        self.n_pos_count = 0
        self.n_neg_count = 0
    def train(self, train_data):
        for tokens, label in train_data:
            self.n += 1
            if label == 1:
                self.n_pos_count += 1
            else:
                self.n_neg_count += 1
            for token in set(tokens):
                self.vocab.setdefault(token, [0, 0])
                if label == 1:
                    self.vocab[token][0] += 1
                else:
                    self.vocab[token][1] += 1
    def accuracy(self, test_data):
        correct = 0
        for tokens, true_label in test_data:
            pos_prob = self.calculate_probability(tokens, 1)
            neg_prob = self.calculate_probability(tokens, -1)
            predicted_label = 1 if pos_prob > neg_prob else -1
            if predicted_label == true_label:
                correct += 1
        return correct / len(test_data)
    def calculate_probability(self, tokens, label):
        pos_prior = self.n_pos_count / self.n
        neg_prior = self.n_neg_count / self.n
        log_prob = 0
        for token in tokens:
            if token in self.vocab:
                pos_count, neg_count = self.vocab[token]
                pos_prob = (pos_count + 1) / (self.n_pos_count + len(self.vocab))
                neg_prob = (neg_count + 1) / (self.n_neg_count + len(self.vocab))
                log_prob += math.log(pos_prob) if label == 1 else math.log(neg_prob)
            else:
                log_prob += math.log(1 / (self.n_pos_count + len(self.vocab))) if label == 1 else math.log(1 / (self.n_neg_count + len(self.vocab)))
        return math.log(pos_prior) + log_prob if label == 1 else math.log(neg_prior) + log_prob
POS_FILES = ["pos1.txt", "pos2.txt"]
NEG_FILES = ["neg1.txt", "neg2.txt"]
FOLD1_DATA = format_data(POS_FILES, 1) + format_data(NEG_FILES, -1)
FOLD2_DATA = format_data(POS_FILES, 1) + format_data(NEG_FILES, -1)
FOLD3_DATA = format_data(POS_FILES, 1) + format_data(NEG_FILES, -1)
def run_trial(train_data, test):
    model = SentimentNaiveBayes()
    model.train(train_data)
    return model.accuracy(test)
total_accuracy = 0
total_accuracy += run_trial((FOLD1_DATA + FOLD2_DATA), FOLD3_DATA)
total_accuracy += run_trial((FOLD1_DATA + FOLD3_DATA), FOLD2_DATA)
total_accuracy += run_trial((FOLD3_DATA + FOLD2_DATA), FOLD1_DATA)
average_accuracy = total_accuracy / 3
print("The average accuracy across 3-folds is", (average_accuracy * 100), "%")
def calculate_mutual_information(vocab, n, n_pos_count, n_neg_count):
    mutual_information = {}
    for word, counts in vocab.items():
        n11 = counts[0]
        n01 = counts[1]
        n10 = n_pos_count - n11
        n00 = n_neg_count - n01
        mi = 0
        if n11 > 0:
            mi += ((n11 / n) * math.log2((n * n11) / ((n11 + n10) * (n11 + n01))))
        if n01 > 0:
            mi += ((n01 / n) * math.log2((n * n01) / ((n01 + n00) * (n11 + n01))))
        if n10 > 0:
            mi += ((n10 / n) * math.log2((n * n10) / ((n11 + n10) * (n10 + n00))))
        if n00 > 0:
            mi += ((n00 / n) * math.log2((n * n00) / ((n01 + n00) * (n10 + n00))))
        mutual_information[word] = mi
    return mutual_information
token_data = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
vocab = {}
n = 0
n_pos_count = 0
n_neg_count = 0
for tokens, label in token_data:
    n += 1
    if label == 1:
        n_pos_count += 1
    else:
        n_neg_count += 1
    for token in set(tokens):
        vocab.setdefault(token, [0, 0])
        if label == 1:
            vocab[token][0] += 1
        else:
            vocab[token][1] += 1
mutual_information = calculate_mutual_information(vocab, n, n_pos_count, n_neg_count)
print("\nMutual information calculated for selected words:")
print("Mutual information for 'the':", mutual_information.get("the", 0))
print("Mutual information for 'like':", mutual_information.get("like", 0))
print("Mutual information for 'good':", mutual_information.get("good", 0))
print("Mutual information for 'movie':", mutual_information.get("movie", 0))
print("\nTop 10 Words:")
sorted_vocab = sorted(mutual_information.items(), key=operator.itemgetter(1))
top10words = reversed(sorted_vocab[-10:])
for idx, word in enumerate(top10words):
    print(idx + 1, ")", word[0])
print("\nUnexpected:")
print("? ", mutual_information.get('?', 0))
print("also ", mutual_information.get('also', 0))
print("both ", mutual_information.get('both', 0))