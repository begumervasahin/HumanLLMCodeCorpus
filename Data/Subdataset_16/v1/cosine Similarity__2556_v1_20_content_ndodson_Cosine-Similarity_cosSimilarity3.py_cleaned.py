import re
import math
from collections import Counter
b1 = re.compile(r'\w+')
def fonk1(vec1, vec2):
    b2 = set(vec1.keys()) & set(vec2.keys())
    b3 = sum([vec1[x] * vec2[x] for x in b2])
    b4 = sum([vec1[x]**2 for x in vec1.keys()])
    b5 = sum([vec2[x]**2 for x in vec2.keys()])
    b6 = math.sqrt(b4) * math.sqrt(b5)
    if not b6:
        return 0.0
    return float(b3) / b6
def fonk2(text):
    b7 = b1.findall(text)
    return Counter(b7)
def fonk3(cosine):
    b8 = math.acos(cosine)
    return math.degrees(b8)
def fonk4():
    b9 = 'This is a foo bar sentence.'
    b10 = 'This sentence is similar to a foo bar sentence.'
    b11 = 'A string that should not be close to the others!'
    b12 = fonk2(b9)
    b13 = fonk2(b10)
    b14 = fonk2(b11)
    b15 = fonk1(b12, b13)
    b16 = fonk1(b12, b14)
    b17 = fonk3(b15)
    b18 = fonk3(b16)
    print("String 1 is:   " + b9)
    print("String 2 is:   " + b10)
    print("String 3 is:   " + b11)
    print("The cosine similarity angle between string 1 and 2 is {:.2f} degrees".format(b17))
    print("The cosine similarity angle between string 1 and 3 is {:.2f} degrees".format(b18))
if b19 = = "__main__":
    fonk4()