import math
import operator
from b1 import SentimentNaiveBayes, format_data, FOLD1_DATA, FOLD2_DATA, FOLD3_DATA, POS_FILES, NEG_FILES
format_data(POS_FILES, 1)
format_data(NEG_FILES, -1)
print(f"PREPARED FOLD 1 DOCS: {len(FOLD1_DATA)}")
print(f"PREPARED FOLD 2 DOCS: {len(FOLD2_DATA)}")
print(f"PREPARED FOLD 3 DOCS: {len(FOLD3_DATA)}")
def fonk1(train_data, test_data):
    b1 = SentimentNaiveBayes()
    b1.train(train_data)
    return b1.accuracy(test_data)
b2 = sum([
    fonk1(FOLD1_DATA + FOLD2_DATA, FOLD3_DATA),
    fonk1(FOLD1_DATA + FOLD3_DATA, FOLD2_DATA),
    fonk1(FOLD2_DATA + FOLD3_DATA, FOLD1_DATA)
])
b3 = (b2 / 3) * 100
print(f"The average accuracy across 3-folds is {b3:.2f}%")
b4 = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
b5 = {}
a1 = 0
a2 = 0
a3 = 0
for doc in b4:
    tokens, b6 = doc
    a1 += 1
    if b6 = = 1:
        a2 += 1
    else:
        a3 += 1
    b7 = set(tokens)
    for token in b7:
        if token not in b5:
            b5[token] = [0, 0]
        if b6 = = 1:
            b5[token][0] += 1
        else:
            b5[token][1] += 1
print("Vocab Counted...")
b8 = {}
for token, counts in b5.items():
    n11, b9 = counts
    b10 = float(a2 - n11)
    b11 = float(a3 - b9)
    a4 = 0
    if n11 > 0:
        a4 += (n11 / a1) * math.log2((a1 * n11) / ((n11 + b10) * (n11 + b9)))
    if b9 > 0:
        a4 += (b9 / a1) * math.log2((a1 * b9) / ((b9 + b11) * (n11 + b9)))
    if b10 > 0:
        a4 += (b10 / a1) * math.log2((a1 * b10) / ((n11 + b10) * (b10 + b11)))
    if b11 > 0:
        a4 += (b11 / a1) * math.log2((a1 * b11) / ((b9 + b11) * (b10 + b11)))
    b8[token] = a4
print("Mutual Information Calculated...\a1")
for word in ["the", "like", "good", "movie"]:
    print(f"Mutual information for '{word}': {b8.get(word, 0)}")
print("\nTop 10 Words:")
b12 = sorted(b8.items(), b14=operator.itemgetter(1), reverse=True)[:10]
for idx, (word, a4) in enumerate(b12, b13 = 1):
    print(f"{idx}) {word} (MI: {a4:.6f})")
print("\nUnexpected:")
for word in ["?", "also", "both"]:
    print(f"{word}: {b8.get(word, 0)}")
print("\nAll Words Sorted by Mutual Information:")
for idx, (word, a4) in enumerate(sorted(b8.items(), b14 = operator.itemgetter(1), reverse=True), b13=1):
    print(f"{idx}) {word} (MI: {a4:.6f})")