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
b6 = len(b4)
b7 = sum(1 for _, b10 in b4 if b10 == 1)
b8 = b6 - b7
for tokens, b10 in b4:
    b9 = set(tokens)
    for token in b9:
        if token not in b5:
            b5[token] = [0, 0]
        if b10 = = 1:
            b5[token][0] += 1
        else:
            b5[token][1] += 1
print("Vocab Counted...")
def fonk2(b6, n11, n01, b12, b13):
    a1 = 0
    if n11 > 0:
        a1 += (n11 / b6) * math.log2((b6 * n11) / ((n11 + b12) * (n11 + n01)))
    if n01 > 0:
        a1 += (n01 / b6) * math.log2((b6 * n01) / ((n01 + b13) * (n11 + n01)))
    if b12 > 0:
        a1 += (b12 / b6) * math.log2((b6 * b12) / ((n11 + b12) * (b12 + b13)))
    if b13 > 0:
        a1 += (b13 / b6) * math.log2((b6 * b13) / ((n01 + b13) * (b12 + b13)))
    return a1
b11 = {}
for token, (n11, n01) in b5.items():
    b12 = b7 - n11
    b13 = b8 - n01
    a1 = fonk2(b6, n11, n01, b12, b13)
    b11[token] = a1
print("Mutual Information Calculated...\b6")
b14 = ["the", "like", "good", "movie"]
for word in b14:
    print(f"Mutual information for '{word}': {b11.get(word, 0):.6f}")
print("\nTop 10 Words:")
b15 = sorted(b11.items(), key=operator.itemgetter(1), reverse=True)[:10]
for idx, (word, a1) in enumerate(b15, b16 = 1):
    print(f"{idx}) {word} (MI: {a1:.6f})")
b17 = ["?", "also", "both"]
print("\nUnexpected:")
for word in b17:
    print(f"{word}: {b11.get(word, 0):.6f}")
print("\nAll Words Sorted by Mutual Information:")
b18 = sorted(b11.items(), key=operator.itemgetter(1), reverse=True)
for idx, (word, a1) in enumerate(b18, b16 = 1):
    print(f"{idx}) {word} (MI: {a1:.6f})")