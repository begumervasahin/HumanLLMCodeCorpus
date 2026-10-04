import re
from collections import Counter
import math
b1 = 'AI is our friend and it has been friendly'
b2 = 'AI and humans have always been friendly'
def fonk1(document):
    b3 = re.findall(r'\w+', document.lower())
    return Counter(b3)
def fonk2(vector1, vector2):
    b4 = set(vector1.keys()) & set(vector2.keys())
    b5 = sum(vector1[word] * vector2[word] for word in b4)
    b6 = sum(vector1[word]**2 for word in vector1.keys())
    b7 = sum(vector2[word]**2 for word in vector2.keys())
    b8 = math.sqrt(b6) * math.sqrt(b7)
    if b8 = = 0:
        return 0.0
    return b5 / b8
def fonk3():
    b9 = fonk1(b1)
    b10 = fonk1(b2)
    b11 = fonk2(b9, b10)
    print(f'Plagiarism factor: {b11:.2f}')
    if b11 > 0.40:
        print('Your document is a plagiarism.')
    else:
        print('Your document is not a plagiarism.')
if b12 = = '__main__':
    fonk3()