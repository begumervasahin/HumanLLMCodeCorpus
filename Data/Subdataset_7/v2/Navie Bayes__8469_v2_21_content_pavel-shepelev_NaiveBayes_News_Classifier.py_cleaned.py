from collections import Counter
a1 = 6000
a2 = 15000
b1 = "news_train.txt"
b2 = "news_test.txt"
b3 = []
b4 = []
with open(b1, b5 = 'utf-8') as file:
    b6 = file.readlines()
    for article in b6:
        category, b7 = article.split("\t", 1)
        b3.append(category)
        b4.append(b7.strip())
b8 = list(set(b3))
def fonk1(category_name):
    b9 = []
    for i in range(a1):
        if b3[i] == category_name:
            b9.append(i)
    return b9
def fonk2(category, b22):
    b10 = dict.fromkeys(b22, 0)
    for i in fonk1(category):
        b11 = dict(Counter(b4[i].split()))
        for key in b11:
            if key in b22:
                b10[key] += b11[key]
    return b10
def fonk3(category):
    return len(fonk1(category)) / len(b3)
def fonk4(category):
    a3 = 0
    b12 = []
    for i in fonk1(category):
        b11 = dict(Counter(b4[i].split()))
        a3 += len(b11.keys())
        b12 = list(set(b12 + list(b11.keys())))
    return a3, b12
b12 = []
b13 = []
for category_name in b8:
    a3, b14 = fonk4(category_name)
    b12 = list(set(b14 + b12))
    b13.append(a3)
b15 = dict(zip(b8, b13))
b16 = len(b12)
def fonk5(b22):
    b17 = []
    for category_name in b8:
        b10 = fonk2(category_name, b22)
        b18 = dict.fromkeys(b10, 0)
        a4 = 1
        for word in b10:
            b18[word] = 10000 * (b10[word] + 1) / (b15[category_name] + b16)
            a4 *= b18[word]
        a4 *= fonk3(category_name)
        b17.append(a4)
    max_probability, b19 = max((prob, idx) for (idx, prob) in enumerate(b17))
    return b8[b19]
b20 = []
with open(b2, b5 = 'utf-8') as file:
    b21 = file.readlines()
with open('answer.txt', 'w', b5 = "utf8") as answer_file:
    for article in b21:
        b22 = dict(Counter(article.split()))
        b23 = fonk5(b22)
        answer_file.write(b23 + '\n')