from collections import Counter
a1 = 6000
a2 = 15000
b1 = "news_train.txt"
b2 = []
b3 = []
with open(b1, b4 = 'utf-8') as f:
    b5 = f.readlines()
    for article in b5:
        b2.append(article.split("\t", 1)[0])
        b3.append(article.split("\t", 1)[1])
b3 = [x.strip() for x in b3]
b6 = list(set(b2))
def fonk1(name):
    b7 = []
    for i in range(a1):
        if b2[i] == name:
            b7.append(i)
    return b7
def fonk2(categ, testdic):
    b8 = dict.fromkeys(testdic, 0)
    for i in fonk1(categ):
        b9 = dict(Counter(b3[i].split()))
        for key in b9:
            if key in testdic:
                b8[key] += b9[key]
    return b8
def fonk3(categ):
    return len(fonk1(categ)) / len(b2)
def fonk4(categ):
    a3 = 0
    b10 = []
    for i in fonk1(categ):
        b9 = dict(Counter(b3[i].split()))
        a3 += len(b9.keys())
        b10 = list(set(b10 + list(b9.keys())))
    return a3, b10
b11 = []
b10 = []
for categ in b6:
    b10 = list(set(fonk4(categ)[1] + b10))
    b11.append(fonk4(categ)[0])
a3 = dict(zip(b6, b11))
b12 = len(b10)
print(b12)
print(a3)
def fonk5(testdic):
    b13 = []
    for categ in b6:
        b8 = fonk2(categ, testdic)
        b14 = dict.fromkeys(b8, 0)
        a4 = 1
        for word in b8:
            b14[word] = 10000 * (b8[word] + 1) / (a3[categ] + b12)
            a4 *= b14[word]
        a4 *= fonk3(categ)
        b13.append(a4)
    val, b15 = max((val, b15) for (b15, val) in enumerate(b13))
    return b6[b15]
b16 = "news_test.txt"
b17 = []
with open(b16, b4 = 'utf-8') as f:
    b18 = f.readlines()
b19 = open('b20.txt', 'w', b4="utf8")
b20 = ''
for i in range(a2):
    b21 = dict(Counter(b18[i].split()))
    b20 = fonk5(b21)
    b19.write(b20 + '\n')