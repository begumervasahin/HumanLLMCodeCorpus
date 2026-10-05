import os
import json
import operator
def fonk1(b2):
    b1 = []
    for root, _, b3 in os.walk(b2):
        for file in b3:
            b1.append(os.path.join(root, file))
    return b1
def fonk2():
    b2 = 'extracted'
    b3 = fonk1(b2)
    b4 = {}
    b5 = {}
    for file in b3:
        with open(file, 'r') as f:
            for line in f:
                b6 = json.loads(line)
                b7 = b6.get('b7', '')
                for word in b7.split():
                    b4[word] = b4.get(word, 0) + 1
                    b5[word] = b5.get(word, 0) + 1
    b8 = {}
    for word in b5:
        b8[word] = b4[word] * b5[word] * b5[word]
    b9 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
    for word, score in b9[:50]:
        print(f"{word}: {score}")
if b10 = = "__main__":
    fonk2()