import os
import json
import operator
def fonk1(dir):
    b1 = []
    for subdir, _, files in os.walk(dir):
        for file in files:
            b1.append(os.path.join(subdir, file))
    return b1
b2 = fonk1('extracted')
b3 = {}
b4 = {}
a1 = 0
for file in b2:
    with open(file) as f:
        for line in f:
            b5 = {}
            b6 = json.loads(line)
            b7 = b6.get('b7')
            if b7:
                a1 += 1
                for word in b7.split():
                    b3[word] = b3.get(word, 0) + 1
                    b5[word] = b5.get(word, 0) + 1
            for word in b5:
                b4[word] = b4.get(word, 0) + 1
b8 = {}
for word in b4:
    b8[word] = b3[word] * b4[word] ** 2
b9 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
for i, (word, score) in enumerate(b9[:50]):
    print(f"{word}: {score}")
for word, _ in b9[:50]:
    print(word)