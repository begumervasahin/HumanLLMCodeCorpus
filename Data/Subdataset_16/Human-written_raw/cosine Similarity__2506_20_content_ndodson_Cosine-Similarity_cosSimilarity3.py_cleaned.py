import re, math
from collections import Counter
import math
b1 = re.compile(r'\w+')
def fonk1(vec1, vec2):
     b2 = set(vec1.keys()) & set(vec2.keys())
     b3 = sum([vec1[x] * vec2[x] for x in b2])
     b4 = sum([vec1[x]**2 for x in vec1.keys()])
     b5 = sum([vec2[x]**2 for x in vec2.keys()])
     b6 = math.sqrt(b4) * math.sqrt(b5)
     if not b6:
        return 0.0
     else:
        return float(b3) / b6
def fonk2(text):
     b7 = b1.findall(text)
     return Counter(b7)
b8 = 'This is a foo bar sentence .'
b9 = 'This sentence is similar to a foo bar sentence .'
b10 = 'A string that should not be close to the others!'
b11 = fonk2(b8)
b12 = fonk2(b9)
b13 = fonk2(b10)
b14 = fonk1(b11, b12)
b15 = fonk1(b11, b13)
b16 = math.acos(b14)
b17 = math.degrees(b16)
b16 = math.acos(b15)
b18 = math.degrees(b16)
print "String 1 is:   " + b8
print "String 2 is:  " + b9
print "String 3 is:  " + b10
print "the cosine similarity percentage of string 1 and 2 is " + str(b17)
print "the cosine similarity percentage of string 1 and 3 is " + str(b18)