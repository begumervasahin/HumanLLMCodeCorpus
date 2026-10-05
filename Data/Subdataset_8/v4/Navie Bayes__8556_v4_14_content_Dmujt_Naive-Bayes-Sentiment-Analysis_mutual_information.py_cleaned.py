from model import SentimentNaiveBayes, format_data, FOLD1_DATA, FOLD2_DATA, FOLD3_DATA, POS_FILES, NEG_FILES
import math
import operator
format_data(POS_FILES, 1)
format_data(NEG_FILES, -1)
print("PREPARED FOLD 1 DOCS:", len(FOLD1_DATA))
print("PREPARED FOLD 2 DOCS:", len(FOLD2_DATA))
print("PREPARED FOLD 3 DOCS:", len(FOLD3_DATA))
def run_trial(train_data, test):
    model = SentimentNaiveBayes()
    model.train(train_data)
    return model.accuracy(test)
total_accuracy = 0
total_accuracy += run_trial((FOLD1_DATA + FOLD2_DATA), FOLD3_DATA)
total_accuracy += run_trial((FOLD1_DATA + FOLD3_DATA), FOLD2_DATA)
total_accuracy += run_trial((FOLD3_DATA + FOLD2_DATA), FOLD1_DATA)
average_accuracy = total_accuracy / 3
print("The average accuracy across 3 folds is", "{:.2f}%".format(average_accuracy * 100))
token_data = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
vocab = {}
n = len(token_data)
n_pos_count = sum(1 for doc in token_data if doc[1] == 1)
n_neg_count = sum(1 for doc in token_data if doc[1] == -1)
for doc in token_data:
    tokens = doc[0]
    c = doc[1]
    for token in set(tokens):
        if token not in vocab:
            vocab[token] = [0, 0]
        if c == 1:
            vocab[token][0] += 1
        else:
            vocab[token][1] += 1
print("Vocabulary counted...")
mutual_information_calculations = {}
for word, counts in vocab.items():
    n11, n01 = counts
    n10 = n_pos_count - n11
    n00 = n_neg_count - n01
    mi = 0
    for n_x1, n_x0 in [(n11, n10), (n01, n00)]:
        if n_x1 > 0:
            mi += (n_x1 / n) * math.log2((n * n_x1) / ((n_x1 + n_x0) * (n11 + n01)))
    mutual_information_calculations[word] = mi
print("Mutual information calculated...\n")
print("Mutual information for 'the':", mutual_information_calculations.get("the", 0))
print("Mutual information for 'like':", mutual_information_calculations.get("like", 0))
print("Mutual information for 'good':", mutual_information_calculations.get("good", 0))
print("Mutual information for 'movie':", mutual_information_calculations.get("movie", 0))
print("\nTop 10 Words:")
sorted_vocab = sorted(mutual_information_calculations.items(), key=operator.itemgetter(1))
top10words = sorted_vocab[-10:]
for idx, (word, _) in enumerate(reversed(top10words)):
    print(idx + 1, ")", word)
print("\nUnexpected:")
print("? ", mutual_information_calculations.get('?', 0))
print("also ", mutual_information_calculations.get('also', 0))
print("both ", mutual_information_calculations.get('both', 0))
print("\nAll Words Sorted by Mutual Information:")
for idx, (word, mi) in enumerate(reversed(sorted_vocab)):
    print(idx + 1, ")", word, mi)