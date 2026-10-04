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
    return max(fonk4(word), b3 = lambda w: fonk2(w, b12))
def fonk4(word):
    return (fonk5([word]) or
            fonk5(fonk6(word)) or
            fonk5(fonk7(word)) or
            {word})
def fonk5(words):
    return {w for w in words if w in b11}
def fonk6(word):
    b4 = 'abcdefghijklmnopqrstuvwxyz'
    b5 = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    b6 = [L + R[1:] for L, R in b5 if R]
    b7 = [L + R[1] + R[0] + R[2:] for L, R in b5 if len(R) > 1]
    b8 = [L + c + R[1:] for L, R in b5 if R for c in b4]
    b9 = [L + c + R for L, R in b5 for c in b4]
    return set(b6 + b7 + b8 + b9)
def fonk7(word):
    return {e2 for e1 in fonk6(word) for e2 in fonk6(e1)}
if b10 = = '__main__':
    b11 = fonk1('LargeTextFile.txt')
    b12 = sum(b11.values())
    b13 = 'speling'
    print(f'Corrected word: {fonk3(b13)}')