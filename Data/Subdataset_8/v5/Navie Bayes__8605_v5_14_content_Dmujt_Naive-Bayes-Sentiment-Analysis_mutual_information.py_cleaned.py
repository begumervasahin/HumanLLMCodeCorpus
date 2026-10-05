from model import SentimentNaiveBayes, format_data, FOLD1_DATA, FOLD2_DATA, FOLD3_DATA, POS_FILES, NEG_FILES
import math
import operator
format_data(POS_FILES, 1)
format_data(NEG_FILES, -1)
print("Number of Prepared Documents for Each Fold:")
print("Fold 1:", len(FOLD1_DATA))
print("Fold 2:", len(FOLD2_DATA))
print("Fold 3:", len(FOLD3_DATA))
def run_trial(train_data, test_data):
    model = SentimentNaiveBayes()
    model.train(train_data)
    return model.accuracy(test_data)
accuracy_sum = 0
for train_data, test_data in [
    (FOLD1_DATA + FOLD2_DATA, FOLD3_DATA),
    (FOLD1_DATA + FOLD3_DATA, FOLD2_DATA),
    (FOLD3_DATA + FOLD2_DATA, FOLD1_DATA)
]:
    accuracy_sum += run_trial(train_data, test_data)
average_accuracy = accuracy_sum / 3
print("\nAverage Accuracy Across 3 Folds:", "{:.2f}%".format(average_accuracy * 100))
token_data = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
vocab = {}
n = len(token_data)
n_pos_count = sum(1 for doc in token_data if doc[1] == 1)
n_neg_count = sum(1 for doc in token_data if doc[1] == -1)
for tokens, c in token_data:
    for token in set(tokens):
        if token not in vocab:
            vocab[token] = [0, 0]
        if c == 1:
            vocab[token][0] += 1
        else:
            vocab[token][1] += 1
print("\nVocabulary Counted...")
mutual_information = {}
for word, counts in vocab.items():
    n11, n01 = counts
    n10 = n_pos_count - n11
    n00 = n_neg_count - n01
    mi = 0
    for n_x1, n_x0 in [(n11, n10), (n01, n00)]:
        if n_x1 > 0:
            mi += (n_x1 / n) * math.log2((n * n_x1) / ((n_x1 + n_x0) * (n11 + n01)))
    mutual_information[word] = mi
print("Mutual Information Calculated...\n")
selected_words = ['the', 'like', 'good', 'movie']
print("Mutual Information for Selected Words:")
for word in selected_words:
    print(word + ":", mutual_information.get(word, 0))
print("\nTop 10 Words:")
sorted_vocab = sorted(mutual_information.items(), key=operator.itemgetter(1), reverse=True)[:10]
for idx, (word, mi) in enumerate(sorted_vocab):
    print(idx + 1, ")", word)
unexpected_words = ['?', 'also', 'both']
print("\nUnexpected Words:")
for word in unexpected_words:
    print(word + ":", mutual_information.get(word, 0))
print("\nAll Words Sorted by Mutual Information:")
for idx, (word, mi) in enumerate(sorted_vocab):
    print(idx + 1, ")", word, mi)