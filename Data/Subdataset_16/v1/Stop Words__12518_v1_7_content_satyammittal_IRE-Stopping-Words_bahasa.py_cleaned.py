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
b2 = ['out.txt']
b3 = {}
b4 = {}
b5 = {}
b6 = {}
a1 = 0
a2 = 0
for file in b2:
    with open(file) as f:
        for line in f:
            b7 = json.loads(line)
            b8 = b7['desc']
            b4 = {}
            a1 += 1
            a2 = 0
            b6 = {}
            if b8 is not None:
                for word in b8.split():
                    a2 += 1.0
                    if "," not in word and "-" not in word:
                        if word in b3:
                            b3[word] += 1
                        else:
                            b3[word] = 1
                        if word in b4:
                            b4[word] += 1
                        else:
                            b4[word] = 1
                for a in b4:
                    if a in b5:
                        b5[a] += 1
                    else:
                        b5[a] = 1
b9 = {}
for a in b5:
    b9[a] = b3[a] * b5[a] * b5[a]
b10 = sorted(b9.items(), key=operator.itemgetter(1), reverse=True)
a1 = 50
for d in b10:
    a1 -= 1
    if a1 < 0:
        break
    print(d[0])