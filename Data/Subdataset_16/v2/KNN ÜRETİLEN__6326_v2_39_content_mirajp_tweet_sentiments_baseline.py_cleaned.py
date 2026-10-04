import sys
import re
import nltk
from nltk.corpus import opinion_lexicon
def fonk1():
    b1 = {}
    a1 = 0
    for word in opinion_lexicon.b2():
        b1[word] = a1
        if re.search("zombie", word):
            a1 = 1
    return b1
def fonk2(b6, b1):
    b2 = b6.split()
    pos, b3 = 0, 0
    for word in b2:
        b4 = b1.get(word.lower())
        if b4 is not None:
            if b4 = = 1:
                pos += 1
            elif b4 = = 0:
                b3 += 1
    return pos, b3
def fonk3():
    nltk.download('opinion_lexicon')
    b1 = fonk1()
    with open("test.list", 'rb') as test_file, open("baseline_out.txt", 'w') as out_file:
        for line_cnt, b6 in enumerate(test_file, b5 = 1):
            b6 = b6.decode('ISO-8859-1')
            pos, b3 = fonk2(b6, b1)
            if pos > b3:
                b4 = "positive"
            elif pos < b3:
                b4 = "negative"
            else:
                b4 = "neutral"
            out_file.write(f"{line_cnt} {b4}\n")
if b7 = = "__main__":
    fonk3()