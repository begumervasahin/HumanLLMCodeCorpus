from collections import Counter
a1 = 6000
a2 = 15000
b1 = "news_train.txt"
b2 = "news_test.txt"
b3 = "b20.txt"
b4 = []
b5 = []
with open(b1, b6 = 'utf-8') as f:
    b7 = f.readlines()
    for article in b7:
        b4.append(article.split("\t", 1)[0])
        b5.append(article.split("\t", 1)[1].strip())
b8 = list(set(b4))
def fonk1(name):
    return [i for i in range(a1) if b4[i] == name]
def fonk2(categ, testdic):
    b9 = dict.fromkeys(testdic, 0)
    for i in fonk1(categ):
        b10 = dict(Counter(b5[i].split()))
        for key in b10:
            if key in testdic:
                b9[key] += b10[key]
    return b9
def fonk3(categ):
    return len(fonk1(categ)) / len(b4)
def fonk4(categ):
    a3 = 0
    b11 = set()
    for i in fonk1(categ):
        b10 = dict(Counter(b5[i].split()))
        a3 += len(b10.keys())
        b11.update(b10.keys())
    return a3, b11
b11 = set()
b12 = []
for categ in b8:
    a3, b13 = fonk4(categ)
    b11.update(b13)
    b12.append(a3)
a3 = dict(zip(b8, b12))
b14 = len(b11)
def fonk5(testdic):
    b15 = []
    for categ in b8:
        b9 = fonk2(categ, testdic)
        b16 = dict.fromkeys(b9, 0)
        a4 = 1
        for word in b9:
            b16[word] = 10000 * (b9[word] + 1) / (a3[categ] + b14)
            a4 *= b16[word]
        a4 *= fonk3(categ)
        b15.append(a4)
    return b8[b15.index(max(b15))]
b17 = []
with open(b2, b6 = 'utf-8') as f:
    b18 = f.readlines()
with open(b3, 'w', b6 = "utf-8") as answerfile:
    for i in range(a2):
        b19 = dict(Counter(b18[i].split()))
        b20 = fonk5(b19)
        answerfile.write(b20 + '\n')
print("Classification completed. Results written to", b3)