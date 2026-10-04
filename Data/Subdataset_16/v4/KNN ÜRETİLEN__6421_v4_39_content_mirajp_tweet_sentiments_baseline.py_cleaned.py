import sys
import re
import nltk
from nltk.corpus import opinion_lexicon
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
b1 = {}
a1 = 0
for b4 in opinion_lexicon.b2():
    b1[b4] = a1
    if re.search("zombie", b4):
        a1 = 1
with open("test.list", 'rb') as test_file, open("baseline_out.txt", 'w') as out_file:
    a2 = 1
    for tweet in test_file:
        b2 = tweet.split()
        pos, b3 = 0, 0
        for b4 in b2:
            b4 = b4.lower()
            if b4 in b1:
                if b1[b4] == 1:
                    pos += 1
                elif b1[b4] == 0:
                    b3 += 1
        if pos > b3:
            b5 = "positive"
        elif pos < b3:
            b5 = "negative"
        else:
            b5 = "neutral"
        out_file.write(f"{a2} {b5}\n")
        a2 += 1