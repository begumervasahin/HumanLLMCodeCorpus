from collections import Counter
a1 = 6000
a2 = 15000
b1 = "news_train.txt"
b2 = "news_test.txt"
b3 = []
b4 = []
b5 = []
with open(b1, b6 = 'utf-8') as f:
    b7 = f.readlines()
    for article in b7:
        b3.append(article.split("\t", 1)[0])
        b4.append(article.split("\t", 1)[1].strip())
b5 = list(set(b3))
def fonk1(name):
    b8 = []
    for i in range(a1):
        if b3[i] == name:
            b8.append(i)
    return b8
def fonk2(categ, testdic):
    b9 = dict.fromkeys(testdic, 0)
    for i in fonk1(categ):
        b10 = dict(Counter(b4[i].split()))
        for key in b10:
            if key in testdic:
                b9[key] += b10[key]
    return b9
def fonk3(categ):
    return len(fonk1(categ)) / len(b3)
def fonk4(categ):
    a3 = 0
    b11 = []
    for i in fonk1(categ):
        b10 = dict(Counter(b4[i].split()))
        a3 += len(b10.keys())
        b11 = list(set(b11 + list(b10.keys())))
    return a3, b11
b12 = []
b11 = []
for categ in b5:
    b11 = list(set(fonk4(categ)[1] + b11))
    b12.append(fonk4(categ)[0])
a3 = dict(zip(b5, b12))
b13 = len(b11)
def fonk5(testdic):
    b14 = []
    for categ in b5:
        b9 = fonk2(categ, testdic)
        b15 = dict.fromkeys(b9, 0)
        a4 = 1
        for word in b9:
            b15[word] = 10000 * (b9[word] + 1) / (a3[categ] + b13)
            a4 *= b15[word]
        a4 *= fonk3(categ)
        b14.append(a4)
    val, b16 = max((val, b16) for (b16, val) in enumerate(b14))
    return b5[b16]
b17 = []
with open(b2, b6 = 'utf-8') as f:
    b18 = f.readlines()
with open('b20.txt', 'w', b6 = "utf8") as answerfile:
    for i in range(a2):
        b19 = dict(Counter(b18[i].split()))
        b20 = fonk5(b19)
        answerfile.write(b20 + '\n')