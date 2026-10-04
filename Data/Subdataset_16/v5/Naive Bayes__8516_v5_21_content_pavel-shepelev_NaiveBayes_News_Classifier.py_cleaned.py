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
def fonk1(category):
    return [i for i in range(a1) if b4[i] == category]
def fonk2(category, b21):
    b10 = dict.fromkeys(b21, 0)
    for i in fonk1(category):
        b11 = Counter(b5[i].split())
        for word, count in b11.items():
            if word in b21:
                b10[word] += count
    return b10
def fonk3(category):
    return len(fonk1(category)) / len(b4)
def fonk4(category):
    a3 = 0
    b12 = set()
    for i in fonk1(category):
        b11 = Counter(b5[i].split())
        a3 += sum(b11.values())
        b12.update(b11.keys())
    return a3, b12
a3 = {}
b12 = set()
for category in b9:
    words, b13 = fonk4(category)
    b12.update(b13)
    a3[category] = words
b14 = len(b12)
print(f"Vocabulary length: {b14}")
print(f"Total words per category: {a3}")
def fonk5(b21):
    b15 = []
    for category in b9:
        b10 = fonk2(category, b21)
        b16 = {
            word: (b10[word] + 1) / (a3[category] + b14)
            for word in b10
        }
        b17 = fonk3(category)
        for word in b16:
            b17 *= b16[word]
        b15.append(b17)
    b18 = max(b15)
    b19 = b9[b15.index(b18)]
    return b19
with open(b2, b6 = 'utf-8') as f:
    b20 = f.readlines()
with open(b3, 'w', b6 = "utf-8") as answer_file:
    for i in range(a2):
        b21 = Counter(b20[i].split())
        b22 = fonk5(b21)
        answer_file.write(b22 + '\n')
print("Classification completed and results written to", b3)