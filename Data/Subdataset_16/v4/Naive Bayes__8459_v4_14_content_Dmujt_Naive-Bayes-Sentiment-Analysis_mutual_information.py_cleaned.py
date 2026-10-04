from b1 import SentimentNaiveBayes, format_data, FOLD1_DATA, FOLD2_DATA, FOLD3_DATA, POS_FILES, NEG_FILES
import math
import operator
format_data(POS_FILES, 1)
format_data(NEG_FILES, -1)
print(f"PREPARED FOLD 1 DOCS: {len(FOLD1_DATA)}")
print(f"PREPARED FOLD 2 DOCS: {len(FOLD2_DATA)}")
print(f"PREPARED FOLD 3 DOCS: {len(FOLD3_DATA)}")
def fonk1(train_data, test_data):
    b1 = SentimentNaiveBayes()
    b1.train(train_data)
    return b1.accuracy(test_data)
a1 = 0
a1 += fonk1(FOLD1_DATA + FOLD2_DATA, FOLD3_DATA)
a1 += fonk1(FOLD1_DATA + FOLD3_DATA, FOLD2_DATA)
a1 += fonk1(FOLD3_DATA + FOLD2_DATA, FOLD1_DATA)
b2 = (a1 / 3) * 100
print(f"The average accuracy across 3-folds is {b2:.2f}%")
b3 = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
b4 = {}
b5 = len(b3)
b6 = sum(1 for doc in b3 if doc[1] == 1)
b7 = b5 - b6
for doc in b3:
    tokens, b8 = doc
    b9 = set()
    for token in tokens:
        if token not in b9:
            if token not in b4:
                b4[token] = [0, 0]
            b4[token][b8 = = 1] += 1
            b9.add(token)
print("Vocab Counted...")
b10 = {}
for token, counts in b4.items():
    b11 = counts[0]
    b12 = counts[1]
    b13 = b6 - b11
    b14 = b7 - b12
    a2 = 0
    if b11 > 0:
        a2 += (b11 / b5) * math.log2((b5 * b11) / ((b11 + b13) * (b11 + b12)))
    if b12 > 0:
        a2 += (b12 / b5) * math.log2((b5 * b12) / ((b12 + b14) * (b11 + b12)))
    if b13 > 0:
        a2 += (b13 / b5) * math.log2((b5 * b13) / ((b11 + b13) * (b13 + b14)))
    if b14 > 0:
        a2 += (b14 / b5) * math.log2((b5 * b14) / ((b12 + b14) * (b13 + b14)))
    b10[token] = a2
print("Mutual Information Calculated...\n")
print(f"Mutual information for 'the': {b10.get('the', 0):.4f}")
print(f"Mutual information for 'like': {b10.get('like', 0):.4f}")
print(f"Mutual information for 'good': {b10.get('good', 0):.4f}")
print(f"Mutual information for 'movie': {b10.get('movie', 0):.4f}")
print("\nTop 10 Words:")
b15 = sorted(b10.items(), key=operator.itemgetter(1), reverse=True)
b16 = b15[:10]
for idx, (word, a2) in enumerate(b16, b17 = 1):
    print(f"{idx}) {word}: {a2:.4f}")
print("Unexpected:")
print(f"? : {b10.get('?', 0):.4f}")
print(f"also : {b10.get('also', 0):.4f}")
print(f"both : {b10.get('both', 0):.4f}")
print("\nAll words sorted by mutual information:")
for idx, (word, a2) in enumerate(b15, b17 = 1):
    print(f"{idx}) {word}: {a2:.4f}")