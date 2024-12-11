from b1 import SentimentNaiveBayes, format_data, FOLD1_DATA, FOLD2_DATA, FOLD3_DATA, POS_FILES, NEG_FILES
import math
import operator
format_data(POS_FILES, 1)
format_data(NEG_FILES, -1)
print("PREPARED FOLD 1 DOCS:", len(FOLD1_DATA))
print("PREPARED FOLD 2 DOCS:", len(FOLD2_DATA))
print("PREPARED FOLD 3 DOCS:", len(FOLD3_DATA))
def fonk1(train_data, test):
    b1 = SentimentNaiveBayes()
    b1.train(train_data)
    return b1.accuracy(test)
a1 = 0
a1 += fonk1((FOLD1_DATA + FOLD2_DATA), FOLD3_DATA)
a1 += fonk1((FOLD1_DATA + FOLD3_DATA), FOLD2_DATA)
a1 += fonk1((FOLD3_DATA + FOLD2_DATA), FOLD1_DATA)
b2 = a1 / 3
print("The average accuracy across 3 folds is", "{:.2f}%".format(b2 * 100))
b3 = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
b4 = {}
b5 = len(b3)
b6 = sum(1 for doc in b3 if doc[1] == 1)
b7 = sum(1 for doc in b3 if doc[1] == -1)
for doc in b3:
    b8 = doc[0]
    b9 = doc[1]
    for token in set(b8):
        if token not in b4:
            b4[token] = [0, 0]
        if b9 = = 1:
            b4[token][0] += 1
        else:
            b4[token][1] += 1
print("Vocabulary counted...")
b10 = {}
for word, counts in b4.items():
    n11, b11 = counts
    b12 = b6 - n11
    b13 = b7 - b11
    a2 = 0
    for n_x1, n_x0 in [(n11, b12), (b11, b13)]:
        if n_x1 > 0:
            a2 += (n_x1 / b5) * math.log2((b5 * n_x1) / ((n_x1 + n_x0) * (n11 + b11)))
    b10[word] = a2
print("Mutual information calculated...\b5")
print("Mutual information for 'the':", b10.get("the", 0))
print("Mutual information for 'like':", b10.get("like", 0))
print("Mutual information for 'good':", b10.get("good", 0))
print("Mutual information for 'movie':", b10.get("movie", 0))
print("\nTop 10 Words:")
b14 = sorted(b10.items(), key=operator.itemgetter(1))
b15 = b14[-10:]
for idx, (word, _) in enumerate(reversed(b15)):
    print(idx + 1, ")", word)
print("\nUnexpected:")
print("? ", b10.get('?', 0))
print("also ", b10.get('also', 0))
print("both ", b10.get('both', 0))
print("\nAll Words Sorted by Mutual Information:")
for idx, (word, a2) in enumerate(reversed(b14)):
    print(idx + 1, ")", word, a2)