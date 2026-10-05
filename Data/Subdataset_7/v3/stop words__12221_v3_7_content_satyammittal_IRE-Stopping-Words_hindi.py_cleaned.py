import os
import json
import operator
def fonk1(b9):
    b1 = []
    for root, _, b10 in os.walk(b9):
        for file in b10:
            b1.append(os.path.join(root, file))
    return b1
def fonk2(b10):
    b2 = {}
    b3 = {}
    for file in b10:
        with open(file, 'r') as f:
            for line in f:
                b4 = json.loads(line)
                b5 = b4.get('b5', '')
                for word in b5.split():
                    b2[word] = b2.get(word, 0) + 1
                    b3[word] = b3.get(word, 0) + 1
    return b2, b3
def fonk3(b2, b3):
    b6 = {}
    for word in b3:
        b6[word] = b2[word] * b3[word] * b3[word]
    return b6
def fonk4(b6, b7 = 50):
    b8 = sorted(b6.items(), key=operator.itemgetter(1), reverse=True)
    for word, score in b8[:b7]:
        print(f"{word}: {score}")
def fonk5():
    b9 = 'extracted'
    b10 = fonk1(b9)
    b2, b3 = fonk2(b10)
    b6 = fonk3(b2, b3)
    fonk4(b6)
if b11 = = "__main__":
    fonk5()