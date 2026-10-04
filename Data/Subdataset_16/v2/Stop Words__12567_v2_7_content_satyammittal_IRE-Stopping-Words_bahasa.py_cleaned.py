import os
import json
import operator
def fonk1(b9):
    b1 = []
    for subdir, _, files in os.walk(b9):
        for file in files:
            b1.append(os.path.join(subdir, file))
    return b1
def fonk2(b1):
    b2 = {}
    b3 = {}
    for file in b1:
        with open(file, 'r') as f:
            for line in f:
                try:
                    b4 = json.loads(line)
                    b5 = b4.get('desc', None)
                    if b5:
                        b6 = set()
                        for word in b5.split():
                            if "," not in word and "-" not in word:
                                b2[word] = b2.get(word, 0) + 1
                                b6.add(word)
                        for word in b6:
                            b3[word] = b3.get(word, 0) + 1
                except json.JSONDecodeError:
                    continue
    return b2, b3
def fonk3(b2, b3):
    b7 = {word: count * (doc_count ** 2)
              for word, count in b2.items()
              for doc_count in [b3[word]]}
    b8 = sorted(b7.items(), key=operator.itemgetter(1), reverse=True)
    return b8
def fonk4():
    b9 = 'extracted'
    b1 = fonk1(b9)
    b1 = ['out.txt']
    b2, b3 = fonk2(b1)
    b8 = fonk3(b2, b3)
    a1 = 50
    for i, (word, score) in enumerate(b8):
        if i >= a1:
            break
        print(word)
if b10 = = "__main__":
    fonk4()