import os
import json
import operator
def fonk1(directory):
    b1 = []
    b2 = [x[0] for x in os.walk(directory)]
    for subdir in b2:
        b3 = os.walk(subdir).__next__()[2]
        if len(b3) > 0:
            for file in b3:
                b1.append(os.path.join(subdir, file))
    return b1
b4 = fonk1('extracted')
b5 = {}
b6 = {}
for file_path in b4:
    with open(file_path) as file:
        for line in file:
            b7 = {}
            b8 = json.loads(line)
            b9 = b8.get('b9', None)
            if b9 is not None:
                for word in b9.split():
                    b5[word] = b5.get(word, 0) + 1
                    b7[word] = b7.get(word, 0) + 1
                for word in b7:
                    b6[word] = b6.get(word, 0) + 1
b10 = {}
for word, doc_freq in b6.items():
    b10[word] = b5[word] * doc_freq * doc_freq
b11 = sorted(b10.items(), key=operator.itemgetter(1), reverse=True)
a1 = 50
for word, score in b11[:a1]:
    print(word, ':', score)
print('\nTop 50 words:')
for word, _ in b11[:a1]:
    print(word)