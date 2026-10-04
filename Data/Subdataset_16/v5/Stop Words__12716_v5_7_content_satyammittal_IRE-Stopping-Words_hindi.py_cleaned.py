import os
import json
import operator
def fonk1(directory):
    b1 = []
    for subdir, _, files in os.walk(directory):
        for file in files:
            b1.append(os.path.join(subdir, file))
    return b1
def fonk2(b8):
    b2 = {}
    b3 = {}
    a1 = 0
    for file in b8:
        with open(file) as f:
            for line in f:
                b4 = {}
                b5 = json.loads(line)
                b6 = b5.get('b6')
                if b6:
                    a1 += 1
                    for word in b6.split():
                        b2[word] = b2.get(word, 0) + 1
                        b4[word] = b4.get(word, 0) + 1
                for word in b4:
                    b3[word] = b3.get(word, 0) + 1
    return b2, b3
def fonk3(b2, b3):
    b7 = {}
    for word in b3:
        b7[word] = b2[word] * (b3[word] ** 2)
    return b7
def fonk4():
    b8 = fonk1('extracted')
    b2, b3 = fonk2(b8)
    b7 = fonk3(b2, b3)
    b9 = sorted(b7.items(), key=operator.itemgetter(1), reverse=True)
    print("Top 50 words with their scores:")
    for word, score in b9[:50]:
        print(f"{word}: {score}")
    print("\nTop 50 words:")
    for word, _ in b9[:50]:
        print(word)
if b10 = = "__main__":
    fonk4()