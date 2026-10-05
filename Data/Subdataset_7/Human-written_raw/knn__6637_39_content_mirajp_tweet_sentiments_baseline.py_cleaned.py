import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
import re
from nltk.corpus import opinion_lexicon
a1 = 0
b1 = {}
for w in nltk.corpus.opinion_lexicon.b4():
    if a1 = = 0:
        b1[w] = a1
        if re.search("zombie",w):
            a1 = 1
    else:
        b1[w] = a1
b2 = open("test.list",'rb')
b3 = open("baseline_out.txt",'w')
a2 = 1
for tweet in b2:
    b4 = tweet.split(" ")
    a3 = 0
    a4 = 0
    for word in b4:
        try:
            if b1[word.lower()] == 1:
                a4 += 1
            elif b1[word.lower()] == 0:
                a3 += 1
        except KeyError:
            pass
    if a4 > a3:
        b3.write(str(a2) + " positive\n")
    elif a4 < a3:
        b3.write(str(a2) + " negative\n")
    else:
        b3.write(str(a2) + " neutral\n")
    a2 += 1