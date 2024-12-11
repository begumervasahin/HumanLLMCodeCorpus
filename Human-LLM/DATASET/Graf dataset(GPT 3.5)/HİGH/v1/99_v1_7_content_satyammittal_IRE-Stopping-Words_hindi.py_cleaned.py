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
                b6 = {}
                b7 = json.loads(line)
                b8 = b7.get('b8', '')
                for word in b8.split():
                    b4[word] = b4.get(word, 0) + 1
                    b6[word] = b6.get(word, 0) + 1
                for word in b6:
                    b5[word] = b5.get(word, 0) + 1
    b9 = {}
    for word in b5:
        b9[word] = b4[word] * b5[word] * b5[word]
    b10 = sorted(b9.items(), key=operator.itemgetter(1), reverse=True)
    for word, count in b10[:50]:
        print(f"{word}: {count}")
if b11 = = "__main__":
    fonk2()