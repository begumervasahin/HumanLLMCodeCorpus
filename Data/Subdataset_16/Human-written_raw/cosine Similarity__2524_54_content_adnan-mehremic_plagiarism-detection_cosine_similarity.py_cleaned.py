import re
from collections import Counter
import math
b1 = 'AI is our friend and it has been friendly'
b2 = 'AI and humans have always been friendly'
def fonk1(document):
    b3 = re.compile(r'\w+')
    b4 = b3.findall(document)
    return Counter(b4)
b5 = fonk1(b1.lower())
b6 = fonk1(b2.lower())
def fonk2(vector1, vector2):
    b7 = set(vector1.keys()) & set(vector2.keys())
    b8 = sum([vector1[x] * vector2[x] for x in b7])
    b9 = sum([vector1[x]**2 for x in vector1.keys()])
    b10 = sum([vector2[x]**2 for x in vector2.keys()])
    b11 = math.sqrt(b9) * math.sqrt(b10)
    return b8/ b11
b12 = fonk2(b5, b6)
print('Plagiarism factor: ', b12)
if b12 > 0.40:
    print('Your document is a plagiarism.')
else:
    print('Your document is not a plagiarism.')