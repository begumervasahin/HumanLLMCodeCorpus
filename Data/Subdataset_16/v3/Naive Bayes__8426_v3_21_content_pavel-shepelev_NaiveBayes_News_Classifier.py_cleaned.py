from collections import Counter
a1 = 6000
a2 = 15000
b1 = "news_train.txt"
b2 = "news_test.txt"
b3 = "answer.txt"
def fonk1(file_path):
    b4 = []
    b5 = []
    with open(file_path, b6 = 'utf-8') as file:
        b7 = file.readlines()
        for article in b7:
            category, b8 = article.split("\t", 1)
            b4.append(category)
            b5.append(b8.strip())
    return b4, b5
b4, b5 = fonk1(b1)
b9 = list(set(b4))
def fonk2(category_name):
    return [i for i in range(a1) if b4[i] == category_name]
def fonk3(category_name, b22):
    b10 = {word: 0 for word in b22}
    for i in fonk2(category_name):
        b11 = Counter(b5[i].split())
        for word in b11:
            if word in b22:
                b10[word] += b11[word]
    return b10
def fonk4(category_name):
    return len(fonk2(category_name)) / len(b4)
def fonk5(category_name):
    a3 = 0
    b12 = set()
    for i in fonk2(category_name):
        b11 = Counter(b5[i].split())
        a3 += len(b11)
        b12.update(b11.keys())
    return a3, b12
def fonk6():
    b13 = set()
    b14 = []
    for category_name in b9:
        a3, b15 = fonk5(category_name)
        b13.update(b15)
        b14.append(a3)
    return b13, dict(zip(b9, b14))
b13, b16 = fonk6()
b17 = len(b13)
def fonk7(b22):
    b18 = []
    for category_name in b9:
        b10 = fonk3(category_name, b22)
        b19 = fonk4(category_name)
        for word in b22:
            b20 = (b10.get(word, 0) + 1) / (b16[category_name] + b17)
            b19 *= b20
        b18.append(b19)
    return b9[b18.index(max(b18))]
def fonk8():
    with open(b2, b6 = 'utf-8') as file:
        b21 = file.readlines()
    with open(b3, 'w', b6 = "utf-8") as answer_file:
        for i in range(a2):
            b22 = Counter(b21[i].split())
            b23 = fonk7(b22)
            answer_file.write(b23 + '\n')
    print(f"Classification completed. Results written to {b3}")
if b24 = = '__main__':
    fonk8()