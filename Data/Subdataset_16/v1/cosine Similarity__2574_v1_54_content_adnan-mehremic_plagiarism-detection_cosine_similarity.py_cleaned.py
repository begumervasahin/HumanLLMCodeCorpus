import re
from collections import Counter
import math
b1 = 'AI is our friend and it has been friendly'
b2 = 'AI and humans have always been friendly'
def fonk1(document):
    b3 = re.compile(r'\w+')
    b4 = b3.findall(document.lower())
    return Counter(b4)
def fonk2(vector1, vector2):
    b5 = set(vector1.keys()) & set(vector2.keys())
    b6 = sum(vector1[word] * vector2[word] for word in b5)
    b7 = sum(vector1[word]**2 for word in vector1.keys())
    b8 = sum(vector2[word]**2 for word in vector2.keys())
    b9 = math.sqrt(b7) * math.sqrt(b8)
    if b9 = = 0:
        return 0.0
    return b6 / b9
def fonk3():
    b10 = fonk1(b1)
    b11 = fonk1(b2)
    b12 = fonk2(b10, b11)
    print('Plagiarism factor:', b12)
    if b12 > 0.40:
        print('Your document is a plagiarism.')
    else:
        print('Your document is not a plagiarism.')
if b13 = = '__main__':
    fonk3()