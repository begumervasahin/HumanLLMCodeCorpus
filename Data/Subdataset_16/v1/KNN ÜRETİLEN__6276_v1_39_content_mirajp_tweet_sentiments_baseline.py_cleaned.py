import sys
import re
import nltk
from nltk.corpus import opinion_lexicon
def fonk1():
    b1 = {}
    a1 = 0
    for w in opinion_lexicon.b2():
        if a1 = = 0:
            b1[w] = a1
            if re.search("zombie", w):
                a1 = 1
        else:
            b1[w] = a1
    return b1
def fonk2(b3, b1):
    b2 = b3.split(" ")
    a2 = 0
    a3 = 0
    for word in b2:
        try:
            if b1[word.lower()] == 1:
                a3 += 1
            elif b1[word.lower()] == 0:
                a2 += 1
        except KeyError:
            pass
    return a3, a2
def fonk3():
    nltk.download('opinion_lexicon')
    b1 = fonk1()
    with open("test.list", 'rb') as test_file, open("baseline_out.txt", 'w') as out_file:
        a4 = 1
        for b3 in test_file:
            b3 = b3.decode('ISO-8859-1')
            a3, a2 = fonk2(b3, b1)
            if a3 > a2:
                out_file.write(f"{a4} positive\n")
            elif a3 < a2:
                out_file.write(f"{a4} negative\n")
            else:
                out_file.write(f"{a4} neutral\n")
            a4 += 1
if b4 = = "__main__":
    fonk3()