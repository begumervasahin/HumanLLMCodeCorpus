from collections import Counter
a1 = 6000
a2 = 15000
b1 = "news_train.txt"
b2 = "news_test.txt"
b3 = "answer.txt"
b4 = []
b5 = []
with open(b1, b6 = 'utf-8') as f:
    b7 = f.readlines()
    for article in b7:
        category, b8 = article.split("\t", 1)
        b4.append(category)
        b5.append(b8.strip())
b9 = list(set(b4))
def fonk1(name):
    b10 = [i for i in range(a1) if b4[i] == name]
    return b10
def fonk2(category, b22):
    b11 = dict.fromkeys(b22, 0)
    for i in fonk1(category):
        b12 = Counter(b5[i].split())
        for word, count in b12.items():
            if word in b22:
                b11[word] += count
    return b11
def fonk3(category):
    return len(fonk1(category)) / len(b4)
def fonk4(category):
    a3 = 0
    b13 = set()
    for i in fonk1(category):
        b12 = Counter(b5[i].split())
        a3 += len(b12)
        b13.update(b12.keys())
    return a3, b13
a3 = {}
b13 = set()
for category in b9:
    words, b14 = fonk4(category)
    b13.update(b14)
    a3[category] = words
b15 = len(b13)
print(f"Vocabulary length: {b15}")
print(f"Total words: {a3}")
def fonk5(b22):
    b16 = []
    for category in b9:
        b11 = fonk2(category, b22)
        b17 = {word: (b11[word] + 1) / (a3[category] + b15) for word in b11}
        b18 = fonk3(category)
        for word in b17:
            b18 *= b17[word]
        b16.append(b18)
    b19 = max(b16)
    b20 = b9[b16.index(b19)]
    return b20
with open(b2, b6 = 'utf-8') as f:
    b21 = f.readlines()
with open(b3, 'w', b6 = "utf-8") as answer_file:
    for i in range(a2):
        b22 = Counter(b21[i].split())
        b23 = fonk5(b22)
        answer_file.write(b23 + '\n')
print("Classification completed and results written to", b3)