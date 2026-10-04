import os
import json
import operator
def fonk1(b8):
    b1 = []
    for subdir, _, files in os.walk(b8):
        for file in files:
            b1.append(os.path.join(subdir, file))
    return b1
def fonk2(b9):
    b2 = {}
    b3 = {}
    a1 = 0
    for file in b9:
        with open(file) as f:
            for line in f:
                b4 = json.loads(line)
                b5 = b4.get('desc')
                if b5:
                    a1 += 1
                    b6 = {}
                    for word in b5.split():
                        if "," not in word and "-" not in word:
                            b2[word] = b2.get(word, 0) + 1
                            b6[word] = b6.get(word, 0) + 1
                    for word in b6:
                        b3[word] = b3.get(word, 0) + 1
    return b2, b3
def fonk3(b2, b3):
    b7 = {}
    for word in b3:
        b7[word] = b2[word] * b3[word] ** 2
    return b7
def fonk4():
    b8 = 'extracted'
    b9 = fonk1(b8)
    b9 = ['out.txt']
    b2, b3 = fonk2(b9)
    b7 = fonk3(b2, b3)
    b10 = sorted(b7.items(), key=operator.itemgetter(1), reverse=True)
    for i, (word, score) in enumerate(b10[:50]):
        print(word)
if b11 = = "__main__":
    fonk4()