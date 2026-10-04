import math
import operator
from model import SentimentNaiveBayes, format_data, FOLD1_DATA, FOLD2_DATA, FOLD3_DATA, POS_FILES, NEG_FILES
format_data(POS_FILES, 1)
format_data(NEG_FILES, -1)
print(f"PREPARED FOLD 1 DOCS: {len(FOLD1_DATA)}")
print(f"PREPARED FOLD 2 DOCS: {len(FOLD2_DATA)}")
print(f"PREPARED FOLD 3 DOCS: {len(FOLD3_DATA)}")
def run_trial(train_data, test_data):
    model = SentimentNaiveBayes()
    model.train(train_data)
    return model.accuracy(test_data)
total_accuracy = sum([
    run_trial(FOLD1_DATA + FOLD2_DATA, FOLD3_DATA),
    run_trial(FOLD1_DATA + FOLD3_DATA, FOLD2_DATA),
    run_trial(FOLD2_DATA + FOLD3_DATA, FOLD1_DATA)
])
average_accuracy = (total_accuracy / 3) * 100
print(f"The average accuracy across 3-folds is {average_accuracy:.2f}%")
token_data = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
vocab = {}
n = len(token_data)
n_pos_count = sum(1 for _, sentiment in token_data if sentiment == 1)
n_neg_count = n - n_pos_count
for tokens, sentiment in token_data:
    unique_tokens = set(tokens)
    for token in unique_tokens:
        if token not in vocab:
            vocab[token] = [0, 0]
        if sentiment == 1:
            vocab[token][0] += 1
        else:
            vocab[token][1] += 1
print("Vocab Counted...")
def calculate_mutual_information(n, n11, n01, n10, n00):
    mi = 0
    if n11 > 0:
        mi += (n11 / n) * math.log2((n * n11) / ((n11 + n10) * (n11 + n01)))
    if n01 > 0:
        mi += (n01 / n) * math.log2((n * n01) / ((n01 + n00) * (n11 + n01)))
    if n10 > 0:
        mi += (n10 / n) * math.log2((n * n10) / ((n11 + n10) * (n10 + n00)))
    if n00 > 0:
        mi += (n00 / n) * math.log2((n * n00) / ((n01 + n00) * (n10 + n00)))
    return mi
mutual_information_calculations = {}
for token, (n11, n01) in vocab.items():
    n10 = n_pos_count - n11
    n00 = n_neg_count - n01
    mi = calculate_mutual_information(n, n11, n01, n10, n00)
    mutual_information_calculations[token] = mi
print("Mutual Information Calculated...\n")
specific_words = ["the", "like", "good", "movie"]
for word in specific_words:
    print(f"Mutual information for '{word}': {mutual_information_calculations.get(word, 0):.6f}")
print("\nTop 10 Words:")
top_10_words = sorted(mutual_information_calculations.items(), key=operator.itemgetter(1), reverse=True)[:10]
for idx, (word, mi) in enumerate(top_10_words, start=1):
    print(f"{idx}) {word} (MI: {mi:.6f})")
unexpected_words = ["?", "also", "both"]
print("\nUnexpected:")
for word in unexpected_words:
    print(f"{word}: {mutual_information_calculations.get(word, 0):.6f}")
print("\nAll Words Sorted by Mutual Information:")
sorted_words = sorted(mutual_information_calculations.items(), key=operator.itemgetter(1), reverse=True)
for idx, (word, mi) in enumerate(sorted_words, start=1):
    print(f"{idx}) {word} (MI: {mi:.6f})")