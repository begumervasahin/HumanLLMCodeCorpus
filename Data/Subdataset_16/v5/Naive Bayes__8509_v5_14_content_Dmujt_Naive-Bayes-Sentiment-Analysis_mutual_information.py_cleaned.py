from b1 import SentimentNaiveBayes, format_data, FOLD1_DATA, FOLD2_DATA, FOLD3_DATA, POS_FILES, NEG_FILES
import math
import operator
def fonk1():
    format_data(POS_FILES, 1)
    format_data(NEG_FILES, -1)
    print(f"PREPARED FOLD 1 DOCS: {len(FOLD1_DATA)}")
    print(f"PREPARED FOLD 2 DOCS: {len(FOLD2_DATA)}")
    print(f"PREPARED FOLD 3 DOCS: {len(FOLD3_DATA)}")
def fonk2(train_data, test_data):
    b1 = SentimentNaiveBayes()
    b1.train(train_data)
    return b1.accuracy(test_data)
def fonk3():
    a1 = 0
    a1 += fonk2(FOLD1_DATA + FOLD2_DATA, FOLD3_DATA)
    a1 += fonk2(FOLD1_DATA + FOLD3_DATA, FOLD2_DATA)
    a1 += fonk2(FOLD3_DATA + FOLD2_DATA, FOLD1_DATA)
    b2 = (a1 / 3) * 100
    print(f"The average accuracy across 3-folds is {b2:.2f}%")
def fonk4(b18):
    b3 = {}
    b4 = len(b18)
    b5 = sum(1 for doc in b18 if doc[1] == 1)
    b6 = b4 - b5
    for tokens, b8 in b18:
        b7 = set()
        for token in tokens:
            if token not in b7:
                if token not in b3:
                    b3[token] = [0, 0]
                b3[token][b8 = = 1] += 1
                b7.add(token)
    print("Vocab Counted...")
    b9 = {}
    for token, counts in b3.items():
        b10 = counts[0]
        b11 = counts[1]
        b12 = b5 - b10
        b13 = b6 - b11
        a2 = 0
        if b10 > 0:
            a2 += (b10 / b4) * math.log2((b4 * b10) / ((b10 + b12) * (b10 + b11)))
        if b11 > 0:
            a2 += (b11 / b4) * math.log2((b4 * b11) / ((b11 + b13) * (b10 + b11)))
        if b12 > 0:
            a2 += (b12 / b4) * math.log2((b4 * b12) / ((b10 + b12) * (b12 + b13)))
        if b13 > 0:
            a2 += (b13 / b4) * math.log2((b4 * b13) / ((b11 + b13) * (b12 + b13)))
        b9[token] = a2
    print("Mutual Information Calculated...\n")
    return b9
def fonk5(b9):
    print(f"Mutual information for 'the': {b9.get('the', 0):.4f}")
    print(f"Mutual information for 'like': {b9.get('like', 0):.4f}")
    print(f"Mutual information for 'good': {b9.get('good', 0):.4f}")
    print(f"Mutual information for 'movie': {b9.get('movie', 0):.4f}")
    print("\nTop 10 Words:")
    b14 = sorted(b9.items(), key=operator.itemgetter(1), reverse=True)
    b15 = b14[:10]
    for idx, (word, a2) in enumerate(b15, b16 = 1):
        print(f"{idx}) {word}: {a2:.4f}")
    print("Unexpected:")
    print(f"? : {b9.get('?', 0):.4f}")
    print(f"also : {b9.get('also', 0):.4f}")
    print(f"both : {b9.get('both', 0):.4f}")
    print("\nAll words sorted by mutual information:")
    for idx, (word, a2) in enumerate(b14, b16 = 1):
        print(f"{idx}) {word}: {a2:.4f}")
if b17 = = "__main__":
    fonk1()
    fonk3()
    b18 = FOLD1_DATA + FOLD2_DATA + FOLD3_DATA
    b9 = fonk4(b18)
    fonk5(b9)