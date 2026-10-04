import os
import json
import operator
def fonk1(b10):
    b1 = []
    for subdir, _, files in os.walk(b10):
        for file in files:
            b1.append(os.path.join(subdir, file))
    return b1
def fonk2(b1):
    b2 = {}
    b3 = {}
    for file in b1:
        try:
            with open(file, 'r') as f:
                for line in f:
                    b4 = json.loads(line)
                    b5 = b4.get('desc')
                    if b5:
                        b6 = set()
                        for word in b5.split():
                            b7 = word.strip(",.-")
                            if b7:
                                b2[b7] = b2.get(b7, 0) + 1
                                b6.add(b7)
                        for word in b6:
                            b3[word] = b3.get(word, 0) + 1
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error processing file {file}: {e}")
    return b2, b3
def fonk3(b2, b3):
    b8 = {
        word: count * (doc_count ** 2)
        for word, count in b2.items()
        for doc_count in [b3[word]]
    }
    b9 = sorted(b8.items(), key=operator.itemgetter(1), reverse=True)
    return b9
def fonk4():
    b10 = 'extracted'
    b1 = fonk1(b10)
    b1 = ['out.txt']
    b2, b3 = fonk2(b1)
    b9 = fonk3(b2, b3)
    a1 = 50
    for i, (word, score) in enumerate(b9):
        if i >= a1:
            break
        print(word)
if b11 = = "__main__":
    fonk4()