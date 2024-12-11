import os
import json
import operator
def fonk1(directory):
    b1 = []
    for root, _, files in os.walk(directory):
        for file in files:
            b1.append(os.path.join(root, file))
    return b1
def fonk2(b8):
    b2 = {}
    b3 = {}
    for file_path in b8:
        with open(file_path) as file:
            for line in file:
                b4 = json.loads(line)
                b5 = b4.get('b5', None)
                if b5 is not None:
                    b6 = {}
                    for word in b5.split():
                        b2[word] = b2.get(word, 0) + 1
                        b6[word] = b6.get(word, 0) + 1
                    for word in b6:
                        b3[word] = b3.get(word, 0) + 1
    return b2, b3
def fonk3(b2, b3):
    b7 = {}
    for word, doc_freq in b3.items():
        b7[word] = b2[word] * doc_freq * doc_freq
    return b7
def fonk4(b9, a1):
    print("Top 50 words with their scores:")
    for word, score in b9[:a1]:
        print(f"{word}: {score}")
    print("\nTop 50 words without their scores:")
    for word, _ in b9[:a1]:
        print(word)
def fonk5():
    b8 = fonk1('extracted')
    b2, b3 = fonk2(b8)
    b7 = fonk3(b2, b3)
    b9 = sorted(b7.items(), key=operator.itemgetter(1), reverse=True)
    a1 = 50
    fonk4(b9, a1)
if b10 = = "__main__":
    fonk5()