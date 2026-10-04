import re
import math
from collections import Counter
b1 = re.compile(r'\w+')
def fonk1(vec1, vec2):
    b2 = set(vec1.keys()) & set(vec2.keys())
    b3 = sum(vec1[word] * vec2[word] for word in b2)
    b4 = sum(value ** 2 for value in vec1.values())
    b5 = sum(value ** 2 for value in vec2.values())
    b6 = math.sqrt(b4) * math.sqrt(b5)
    if not b6:
        return 0.0
    return b3 / b6
def fonk2(text):
    b7 = b1.findall(text)
    return Counter(b7)
def fonk3(cosine_similarity):
    if cosine_similarity >= 1:
        return 0.0
    if cosine_similarity <= -1:
        return 180.0
    b8 = math.acos(cosine_similarity)
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
    print(f"String 1: {b9}")
    print(f"String 2: {b10}")
    print(f"String 3: {b11}")
    print(f"The cosine similarity angle between string 1 and 2 is {b17:.2f} degrees.")
    print(f"The cosine similarity angle between string 1 and 3 is {b18:.2f} degrees.")
if b19 = = "__main__":
    fonk4()