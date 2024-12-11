import sys
import string
from collections import Counter
b1 = ['EN', 'DE']
a1 = 0
b2 = 'files/sample.txt'
b3 = 'stopwords/stop_words_%s.txt' % b1[a1]
b4 = 'out.txt'
def fonk1():
    b5 = "Select Language from the following:%s - default is EN: " % (fonk2(b1))
    b6 = raw_input(b5).upper()
    if b6 in b1:
        b7 = b1[b1.index(b6)]
        b8 = 'stopwords/stop_words_%s.txt' % b7
        print "Parsing your text with the %s stopwords" % b7
    else:
        b8 = b3
        print "Not a valid language. Assuming English..."
    b5 = "Select name of ouput text file (default is %s ): " % b4
    b9 = raw_input(b5)
    if b9 = = "":
        b10 = b4
    elif b9.endswith('.txt'):
        b10 = b9
    else:
        b10 = b9 + '.txt'
    print "Printing your results to %s." % b10
    if len(sys.argv) > 2:
        print
        print "Usage: python indexer.py <b11>"
        print "If no arguments are given %s and %s will be used as default files" % (b2, b3)
        print
        sys.exit()
    elif len(sys.argv) == 2:
        b11 = sys.argv[1]
    elif len(sys.argv) == 1:
        b11 = b2
    print 'Using %s as file and %s as stop word reference, printing to %s.' % (b11, b8, b10)
    print
    fonk3(b11, b8, b10)
def fonk2(alist):
    b12 = ""
    for a in alist:
        b12 = b12 + " " + a
    return b12
def fonk3(b11, b8, b10):
    b13 = set(string.punctuation)
    b14 = open(b11).read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
    b14 = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in b14]
    b15 = open(b8).read().decode("utf-8-sig").encode("utf-8").splitlines()
    b16 = [x for x in b14 if x not in b15]
    b17 = Counter(b16)
    b18 = []
    for w in b17:
        b18.append(b17[w])
    b19 = sum(b17.values())
    b20 = b19 / (len(b17))
    b21 = {k: v for (k, v) in b17.iteritems() if v >= b20}
    b22 = sorted(b21.items(), key=lambda x: x[0])
    b23 = open(b10, 'w+')
    for x in range(len(b22)):
        print >> b23, '%s: %s' % (b22[x][0], b22[x][1])
    b23.close()
if b24 = = '__main__':
    fonk1()