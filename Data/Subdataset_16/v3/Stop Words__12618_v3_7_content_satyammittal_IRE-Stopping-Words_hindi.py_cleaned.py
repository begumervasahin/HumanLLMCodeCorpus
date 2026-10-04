import os
import json
import operator
def fonk1(b10):
    b1 = []
    for root, _, b11 in os.walk(b10):
        for file in b11:
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
def fonk4(b12, b9 = 50):
    print("Top 50 words and their b8:")
    for word, score in b12[:b9]:
        print(f"{word} : {score}")
    print("\nTop 50 words:")
    for word, _ in b12[:b9]:
        print(word)
def fonk5():
    b10 = 'extracted'
    b11 = fonk1(b10)
    b2, b3 = fonk2(b11)
    b8 = fonk3(b2, b3)
    b12 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
    fonk4(b12)
if b13 = = "__main__":
    fonk5()