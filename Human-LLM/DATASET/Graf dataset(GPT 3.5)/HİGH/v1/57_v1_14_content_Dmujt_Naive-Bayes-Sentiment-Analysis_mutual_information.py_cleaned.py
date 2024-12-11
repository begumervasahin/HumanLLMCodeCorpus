import math
import operator
def fonk1(files, b6):
    b1 = []
    for file in files:
        with open(file, 'r', b2 = 'utf-8') as f:
            b3 = f.read()
            b4 = b3.split()
            b1.append((b4, b6))
    return b1
class class1:
    def fonk2(self):
        self.b5 = {}
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk3(self, train_data):
        for doc in train_data:
            b4, b6 = doc
            self.a1 += 1
            if b6 = = 1:
                self.a2 += 1
            else:
                self.a3 += 1
            b7 = set()
            for token in b4:
                if token not in b7:
                    if token not in self.b5:
                        self.b5[token] = [0, 0]
                    if b6 = = 1:
                        self.b5[token][0] += 1
                    else:
                        self.b5[token][1] += 1
                    b7.add(token)
    def fonk4(self, test_data):
        a4 = 0
        for doc in test_data:
            b4, b8 = doc
            b9 = self.fonk5(b4, 1)
            b10 = self.fonk5(b4, -1)
            b11 = 1 if b9 > b10 else -1
            if b11 = = b8:
                a4 += 1
        return a4 / len(test_data)
    def fonk5(self, b4, b6):
        b12 = self.a2 / self.a1
        b13 = self.a3 / self.a1
        a5 = 0
        for token in b4:
            if token in self.b5:
                b14 = self.b5[token][0]
                b15 = self.b5[token][1]
                b9 = (b14 + 1) / (self.a2 + len(self.b5))
                b10 = (b15 + 1) / (self.a3 + len(self.b5))
                a5 += math.log(b9) if b6 = = 1 else math.log(b10)
            else:
                a5 += math.log(1 / (self.a2 + len(self.b5))) if b6 = = 1 else math.log(1 / (self.a3 + len(self.b5)))
        return math.log(b12) + a5 if b6 = = 1 else math.log(b13) + a5
b16 = ["pos1.txt", "pos2.txt"]
b17 = ["neg1.txt", "neg2.txt"]
b18 = fonk1(b16, 1) + fonk1(b17, -1)
b19 = fonk1(b16, 1) + fonk1(b17, -1)
b20 = fonk1(b16, 1) + fonk1(b17, -1)
def fonk6(train_data, test):
    b21 = class1()
    b21.fonk3(train_data)
    return b21.fonk4(test)
a6 = 0
a6 += fonk6((b18 + b19), b20)
a6 += fonk6((b18 + b20), b19)
a6 += fonk6((b20 + b19), b18)
b22 = a6 / 3
print("The average accuracy across 3-folds is ", (b22 * 100), "%")
b23 = b18 + b19 + b20
b5 = {}
a1 = 0
a2 = 0
a3 = 0
for doc in b23:
    b4, b6 = doc
    a1 += 1
    if b6 = = 1:
        a2 += 1
    else:
        a3 += 1
    b7 = set()
    for token in b4:
        if token not in b7:
            if token not in b5:
                b5[token] = [0, 0]
            if b6 = = 1:
                b5[token][0] += 1
            else:
                b5[token][1] += 1
            b7.add(token)
b24 = {}
for word, counts in b5.items():
    b25 = counts[0]
    b26 = counts[1]
    b27 = a2 - b25
    b28 = a3 - b26
    a7 = 0
    if b25 > 0:
         a7 += ((b25 / a1) * math.log2((a1 * b25) / ((b25 + b27) * (b25 + b26))))
    if b26 > 0:
        a7 += ((b26 / a1) * math.log2((a1 * b26) / ((b26 + b28) * (b25 + b26))))
    if b27 > 0:
        a7 += ((b27 / a1) * math.log2((a1 * b27) / ((b25 + b27) * (b27 + b28))))
    if b28 > 0:
        a7 += ((b28 / a1) * math.log2((a1 * b28) / ((b26 + b28) * (b27 + b28))))
    b24[word] = a7
print("Mutual information calculated for selected words:")
print("Mutual information for 'the': ", b24.get("the", 0))
print("Mutual information for 'like': ", b24.get("like", 0))
print("Mutual information for 'good': ", b24.get("good", 0))
print("Mutual information for 'movie': ", b24.get("movie", 0))
print("\nTop 10 Words:")
b29 = sorted(b24.items(), key=operator.itemgetter(1))
b30 = reversed(b29[-10:])
for idx, word in enumerate(b30):
    print(idx + 1, ") ", word[0])
print("\nUnexpected:")
print("? ", b24.get('?', 0))
print("also ", b24.get('also', 0))
print("both ", b24.get('both', 0))