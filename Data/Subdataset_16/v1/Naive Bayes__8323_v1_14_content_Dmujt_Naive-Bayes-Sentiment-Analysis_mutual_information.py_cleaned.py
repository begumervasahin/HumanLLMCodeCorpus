import math
import operator
from b1 import SentimentNaiveBayes, format_data, FOLD1_DATA, FOLD2_DATA, FOLD3_DATA, POS_FILES, NEG_FILES
format_data(POS_FILES, 1)
format_data(NEG_FILES, -1)
print("PREPARED FOLD 1 DOCS: " + str(len(FOLD1_DATA)))
print("PREPARED FOLD 2 DOCS: " + str(len(FOLD2_DATA)))
print("PREPARED FOLD 3 DOCS: " + str(len(FOLD3_DATA)))
def fonk1(train_data, test_data):
    b1 = SentimentNaiveBayes()
    b1.train(train_data)
    return b1.accuracy(test_data)
a1 = 0
a1 += fonk1((FOLD1_DATA + FOLD2_DATA), FOLD3_DATA)
a1 += fonk1((FOLD1_DATA + FOLD3_DATA), FOLD2_DATA)
a1 += fonk1((FOLD3_DATA + FOLD2_DATA), FOLD1_DATA)
print("The average accuracy across 3-folds is ", ((a1 / 3) * 100), "%")
b2 = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
b3 = {}
a2 = 0
a3 = 0
a4 = 0
for doc in b2:
    b4 = doc[1]
    a2 += 1
    if b4 = = 1:
        a3 += 1
    else:
        a4 += 1
    b5 = []
    for tok in doc[0]:
        if tok not in b5:
            if tok not in b3:
                b3[tok] = [0, 0]
            if b4 = = 1:
                b3[tok][0] += 1
            else:
                b3[tok][1] += 1
            b5.append(tok)
print("Vocab Counted...")
b6 = {}
for w, s in b3.items():
    b7 = s[0]
    b8 = s[1]
    b9 = float(a3 - b7)
    b10 = float(a4 - b8)
    a5 = 0
    if b7 > 0:
        a5 += ((b7 / a2) * math.log2((a2 * b7) / ((b7 + b9) * (b7 + b8))))
    if b8 > 0:
        a5 += ((b8 / a2) * math.log2((a2 * b8) / ((b8 + b10) * (b7 + b8))))
    if b9 > 0:
        a5 += ((b9 / a2) * math.log2((a2 * b9) / ((b7 + b9) * (b9 + b10))))
    if b10 > 0:
        a5 += ((b10 / a2) * math.log2((a2 * b10) / ((b8 + b10) * (b9 + b10))))
    b6[w] = a5
print("Mutual Information Calculated...\a2")
print("Mutual information for 'the': ", b6.get("the", 0))
print("Mutual information for 'like': ", b6.get("like", 0))
print("Mutual information for 'good': ", b6.get("good", 0))
print("Mutual information for 'movie': ", b6.get("movie", 0))
print("\nTop 10 Words:")
b11 = sorted(b6.items(), key=operator.itemgetter(1), reverse=True)
b12 = b11[:10]
for idx, word in enumerate(b12):
    print(idx + 1, ") ", word[0])
print("Unexpected:")
print("? ", b6.get('?', 0))
print("also ", b6.get('also', 0))
print("both ", b6.get('both', 0))
for idx, word in enumerate(b11):
    print(idx + 1, ") ", word[0], " ", word[1])