import re
from collections import Counter
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = file.read().lower()
    b2 = re.findall(r'\w+', b1)
    return Counter(b2)
def fonk2(word, b12):
    return b11[word] / b12
def fonk3(word):
    return max(fonk4(word), b3 = probability)
def fonk4(word):
    b4 = fonk5([word])
    if b4:
        return b4
    b4 = fonk5(fonk6(word))
    if b4:
        return b4
    b4 = fonk5(fonk7(word))
    if b4:
        return b4
    return {word}
def fonk5(words):
    return {w for w in words if w in b11}
def fonk6(word):
    b5 = 'abcdefghijklmnopqrstuvwxyz'
    b6 = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    b7 = [L + R[1:] for L, R in b6 if R]
    b8 = [L + R[1] + R[0] + R[2:] for L, R in b6 if len(R) > 1]
    b9 = [L + c + R[1:] for L, R in b6 if R for c in b5]
    b10 = [L + c + R for L, R in b6 for c in b5]
    return set(b7 + b8 + b9 + b10)
def fonk7(word):
    return {e2 for e1 in fonk6(word) for e2 in fonk6(e1)}
b11 = fonk1('LargeTextFile.txt')
b12 = sum(b11.values())
if b13 = = '__main__':
    b14 = 'speling'
    print(f'Corrected word: {fonk3(b14)}')