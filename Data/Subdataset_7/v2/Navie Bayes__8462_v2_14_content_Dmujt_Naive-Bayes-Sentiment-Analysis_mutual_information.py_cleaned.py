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
        for b4, b6 in train_data:
            self.a1 += 1
            if b6 = = 1:
                self.a2 += 1
            else:
                self.a3 += 1
            for token in set(b4):
                self.b5.setdefault(token, [0, 0])
                if b6 = = 1:
                    self.b5[token][0] += 1
                else:
                    self.b5[token][1] += 1
    def fonk4(self, test_data):
        a4 = 0
        for b4, true_label in test_data:
            b7 = self.fonk5(b4, 1)
            b8 = self.fonk5(b4, -1)
            b9 = 1 if b7 > b8 else -1
            if b9 = = true_label:
                a4 += 1
        return a4 / len(test_data)
    def fonk5(self, b4, b6):
        b10 = self.a2 / self.a1
        b11 = self.a3 / self.a1
        a5 = 0
        for token in b4:
            if token in self.b5:
                pos_count, b12 = self.b5[token]
                b7 = (pos_count + 1) / (self.a2 + len(self.b5))
                b8 = (b12 + 1) / (self.a3 + len(self.b5))
                a5 += math.log(b7) if b6 = = 1 else math.log(b8)
            else:
                a5 += math.log(1 / (self.a2 + len(self.b5))) if b6 = = 1 else math.log(1 / (self.a3 + len(self.b5)))
        return math.log(b10) + a5 if b6 = = 1 else math.log(b11) + a5
b13 = ["pos1.txt", "pos2.txt"]
b14 = ["neg1.txt", "neg2.txt"]
b15 = fonk1(b13, 1) + fonk1(b14, -1)
b16 = fonk1(b13, 1) + fonk1(b14, -1)
b17 = fonk1(b13, 1) + fonk1(b14, -1)
def fonk6(train_data, test):
    b18 = class1()
    b18.fonk3(train_data)
    return b18.fonk4(test)
a6 = 0
a6 += fonk6((b15 + b16), b17)
a6 += fonk6((b15 + b17), b16)
a6 += fonk6((b17 + b16), b15)
b19 = a6 / 3
print("The average accuracy across 3-folds is", (b19 * 100), "%")
b20 = b15 + b16 + b17
b5 = {}
a1 = 0
a2 = 0
a3 = 0
for b4, b6 in b20:
    a1 += 1
    if b6 = = 1:
        a2 += 1
    else:
        a3 += 1
    for token in set(b4):
        b5.setdefault(token, [0, 0])
        if b6 = = 1:
            b5[token][0] += 1
        else:
            b5[token][1] += 1
b21 = {}
for word, counts in b5.items():
    b22 = counts[0]
    b23 = counts[1]
    b24 = a2 - b22
    b25 = a3 - b23
    a7 = 0
    if b22 > 0:
        a7 += ((b22 / a1) * math.log2((a1 * b22) / ((b22 + b24) * (b22 + b23))))
    if b23 > 0:
        a7 += ((b23 / a1) * math.log2((a1 * b23) / ((b23 + b25) * (b22 + b23))))
    if b24 > 0:
        a7 += ((b24 / a1) * math.log2((a1 * b24) / ((b22 + b24) * (b24 + b25))))
    if b25 > 0:
        a7 += ((b25 / a1) * math.log2((a1 * b25) / ((b23 + b25) * (b24 + b25))))
    b21[word] = a7
print("\nMutual information calculated for selected words:")
print("Mutual information for 'the':", b21.get("the", 0))
print("Mutual information for 'like':", b21.get("like", 0))
print("Mutual information for 'good':", b21.get("good", 0))
print("Mutual information for 'movie':", b21.get("movie", 0))
print("\nTop 10 Words:")
b26 = sorted(b21.items(), key=operator.itemgetter(1))
b27 = reversed(b26[-10:])
for idx, word in enumerate(b27):
    print(idx + 1, ")", word[0])
print("\nUnexpected:")
print("? ", b21.get('?', 0))
print("also ", b21.get('also', 0))
print("both ", b21.get('both', 0))