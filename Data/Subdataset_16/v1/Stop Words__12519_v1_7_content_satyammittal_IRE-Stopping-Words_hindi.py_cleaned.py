import os
import json
import operator
def fonk1(dir):
    b1 = []
    b2 = [x[0] for x in os.walk(dir)]
    for subdir in b2:
        for _, _, files in os.walk(subdir):
            if files:
                for file in files:
                    b1.append(os.path.join(subdir, file))
    return b1
b3 = fonk1('extracted')
b4 = {}
a1 = 0
b5 = {}
b6 = {}
for file in b3:
    with open(file, 'b1', b7 = 'utf-8') as f:
        for line in f:
            b5 = {}
            b8 = json.loads(line)
            b9 = b8.get('b9')
            a1 += 1
            if b9:
                for word in b9.split():
                    if word in b4:
                        b4[word] += 1
                    else:
                        b4[word] = 1
                    if word in b5:
                        b5[word] += 1
                    else:
                        b5[word] = 1
        for word in b5:
            if word in b6:
                b6[word] += 1
            else:
                b6[word] = 1
b10 = {}
for word in b6:
    b10[word] = b4[word] * b6[word] * b6[word]
b11 = sorted(b10.items(), key=operator.itemgetter(1), reverse=True)
a1 = 50
for word, value in b11:
    if a1 <= 0:
        break
    print(f"{word} : {value}")
    a1 -= 1
a1 = 50
for word, _ in b11:
    if a1 <= 0:
        break
    print(word)
    a1 -= 1