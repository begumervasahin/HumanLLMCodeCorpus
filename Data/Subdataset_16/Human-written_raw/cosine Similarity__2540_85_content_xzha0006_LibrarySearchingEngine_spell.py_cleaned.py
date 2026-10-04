import re
from collections import Counter
b1 = re.findall(r'\w+', open('LargeTextFile.txt').read().lower())
b2 = Counter(b1)
def fonk1(word, b3 = sum(b2.values())):
    return b2[word] / b3
def fonk2(word):
    return max(fonk3(word), b4 = probability)
def fonk3(word):
    if len(fonk4([word])) != 0:
        return fonk4([word])
    elif len(fonk4(fonk5(word))) != 0:
        return fonk4(fonk5(word))
    elif len(fonk4(fonk6(word))) != 0:
        return fonk4(fonk6(word))
    else:
        return [word]
def fonk4(words):
    return set(w for w in words if w in b2)
def fonk5(word):
    b5 = 'abcdefghijklmnopqrstuvwxyz'
    b6 = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    b7 = [Left + Right[1:] for Left, Right in b6 if Right]
    b8 = [Left + Right[1] + Right[0] + Right[2:] for Left, Right in b6 if len(Right)>1]
    b9 = [Left + char + Right[1:] for Left, Right in b6 if Right for char in b5]
    b10 = [Left + char + Right for Left, Right in b6 for char in b5]
    return set(b7 + b8 + b9 + b10)
def fonk6(word):
    return (j for i in fonk5(word) for j in fonk5(i))