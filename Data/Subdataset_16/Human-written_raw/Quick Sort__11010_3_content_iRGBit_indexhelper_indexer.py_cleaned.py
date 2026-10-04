import sys
import string
import numpy
b1 = ['EN', 'DE']
b2 = 0;
b3 = 'files/sample.txt'
b4 = 'stopwords/stop_words_%s.txt' % b1[b2]
b5 = 'out.txt'
def fonk1():
    b6 = "Select Language from the following:%s - default is EN: " % (fonk2(b1))
    b7 = raw_input(b6).upper()
    if b7 in b1:
        b8 = b1[b1.index(b7)]
        b9 = 'stopwords/stop_words_%s.txt' % b8
        print "Parsing your text with the %s stopwords" % b8
    else:
        b9 = b4
        print "Not a valid language. Assuming English..."
    b6 = "Select name of ouput text file (default is %s ): " % b5
    b10 = raw_input(b6)
    if b10 = ="":
        b11 = b5
    elif b10.endswith('.txt'):
        b11 = b10
    else:
        b11 = b10 + '.txt'
    print "Printing your results to %s." % b11
    if len(sys.argv) > 2:
        print
        print "Usage: python indexer.py <b12>"
        print "If no arguments are given %s and %s will be used as default files" % (b3, b4)
        print
        sys.exit()
    elif len(sys.argv) == 2:
        b12 = sys.argv[1]
    elif len(sys.argv) == 1:
        b12 = b3
    print 'Using %s as file and %s as stop word reference, printing to %s.' % (b12, b9, b11)
    print
    fonk3(b12, b9, b11)
def fonk2(alist):
    b13 = ""
    for a in alist:
        b13 = b13 + " " + a
    return b13
def fonk3(b12, b9, b11):
    b14 = set(string.punctuation)
    b15 = open(b12).read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
    b15 = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in b15]
    b16 = open(b9).read().decode("utf-8-sig").encode("utf-8").splitlines()
    b17 = [x for x in b15 if x not in b16]
    from collections import Counter
    b18 = Counter(b17)
    b19 = []
    for w in b18:
        b19.append(b18[w])
    a1 = 0
    for w in b18:
        a1 += b18[w]
    b20 = a1/(len(b18))
    b21 = {k:v for (k,v) in b18.iteritems() if v >= b20}
    b22 = sorted(b21.items(), key=lambda x: x[0])
    b23 = open(b11, 'w+')
    for x in range(len(b22)):
        print >> b23, '%s: %s' % (b22[x][0], b22[x][1])
    b23.close()
if b24 = = '__main__':
  fonk1()