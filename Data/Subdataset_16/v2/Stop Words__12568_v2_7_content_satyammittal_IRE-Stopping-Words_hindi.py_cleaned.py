import os
import json
import operator
def fonk1(b9):
    b1 = []
    for root, _, b10 in os.walk(b9):
        for file in b10:
            b1.append(os.path.join(root, file))
    return b1
def fonk2(file_paths):
    b2 = {}
    b3 = {}
    a1 = 0
    for file_path in file_paths:
        with open(file_path, 'r', b4 = 'utf-8') as file:
            for line in file:
                b5 = {}
                b6 = json.loads(line)
                b7 = b6.get('b7')
                a1 += 1
                if b7:
                    for word in b7.split():
                        b2[word] = b2.get(word, 0) + 1
                        b5[word] = b5.get(word, 0) + 1
                for word in b5:
                    b3[word] = b3.get(word, 0) + 1
    return b2, b3
def fonk3(b2, b3):
    b8 = {}
    for word in b3:
        b8[word] = b2[word] * (b3[word] ** 2)
    return b8
def fonk4():
    b9 = 'extracted'
    b10 = fonk1(b9)
    b2, b3 = fonk2(b10)
    b8 = fonk3(b2, b3)
    b11 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
    print("Top 50 words and their b8:")
    for word, score in b11[:50]:
        print(f"{word} : {score}")
    print("\nTop 50 words:")
    for word, _ in b11[:50]:
        print(word)
if b12 = = "__main__":
    fonk4()