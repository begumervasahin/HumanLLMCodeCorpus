import sys
import re
import nltk
from nltk.corpus import opinion_lexicon
def fonk1():
    nltk.download('opinion_lexicon')
    b1 = {}
    a1 = 0
    for b2 in opinion_lexicon.b3():
        b1[b2] = a1
        if b2 = = 'zombie':
            a1 = 1
    return b1
def fonk2(b7, b1):
    b3 = b7.split()
    pos, b4 = 0, 0
    for b2 in b3:
        b5 = b1.get(b2.lower())
        if b5 is not None:
            if b5 = = 1:
                pos += 1
            elif b5 = = 0:
                b4 += 1
    return pos, b4
def fonk3():
    b1 = fonk1()
    with open("test.list", 'rb') as test_file, open("baseline_out.txt", 'w') as out_file:
        for line_cnt, b7 in enumerate(test_file, b6 = 1):
            b7 = b7.decode('ISO-8859-1')
            pos, b4 = fonk2(b7, b1)
            if pos > b4:
                b5 = "positive"
            elif pos < b4:
                b5 = "negative"
            else:
                b5 = "neutral"
            out_file.write(f"{line_cnt} {b5}\n")
if b8 = = "__main__":
    fonk3()