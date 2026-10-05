from b1 import SentimentNaiveBayes, format_data, FOLD1_DATA, FOLD2_DATA, FOLD3_DATA, POS_FILES, NEG_FILES
import math
import operator
format_data(POS_FILES, 1)
format_data(NEG_FILES, -1)
print("Number of Prepared Documents for Each Fold:")
print("Fold 1:", len(FOLD1_DATA))
print("Fold 2:", len(FOLD2_DATA))
print("Fold 3:", len(FOLD3_DATA))
def fonk1(train_data, test_data):
    b1 = SentimentNaiveBayes()
    b1.train(train_data)
    return b1.accuracy(test_data)
a1 = 0
for train_data, test_data in [
    (FOLD1_DATA + FOLD2_DATA, FOLD3_DATA),
    (FOLD1_DATA + FOLD3_DATA, FOLD2_DATA),
    (FOLD3_DATA + FOLD2_DATA, FOLD1_DATA)
]:
    a1 += fonk1(train_data, test_data)
b2 = a1 / 3
print("\nAverage Accuracy Across 3 Folds:", "{:.2f}%".format(b2 * 100))
b3 = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
b4 = {}
b5 = len(b3)
b6 = sum(1 for doc in b3 if doc[1] == 1)
b7 = sum(1 for doc in b3 if doc[1] == -1)
for tokens, b8 in b3:
    for token in set(tokens):
        if token not in b4:
            b4[token] = [0, 0]
        if b8 = = 1:
            b4[token][0] += 1
        else:
            b4[token][1] += 1
print("\nVocabulary Counted...")
b9 = {}
for word, counts in b4.items():
    n11, b10 = counts
    b11 = b6 - n11
    b12 = b7 - b10
    a2 = 0
    for n_x1, n_x0 in [(n11, b11), (b10, b12)]:
        if n_x1 > 0:
            a2 += (n_x1 / b5) * math.log2((b5 * n_x1) / ((n_x1 + n_x0) * (n11 + b10)))
    b9[word] = a2
print("Mutual Information Calculated...\b5")
b13 = ['the', 'like', 'good', 'movie']
print("Mutual Information for Selected Words:")
for word in b13:
    print(word + ":", b9.get(word, 0))
print("\nTop 10 Words:")
b14 = sorted(b9.items(), key=operator.itemgetter(1), reverse=True)[:10]
for idx, (word, a2) in enumerate(b14):
    print(idx + 1, ")", word)
b15 = ['?', 'also', 'both']
print("\nUnexpected Words:")
for word in b15:
    print(word + ":", b9.get(word, 0))
print("\nAll Words Sorted by Mutual Information:")
for idx, (word, a2) in enumerate(b14):
    print(idx + 1, ")", word, a2)