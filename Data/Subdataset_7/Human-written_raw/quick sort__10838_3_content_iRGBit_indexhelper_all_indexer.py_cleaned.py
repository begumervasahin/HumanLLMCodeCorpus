import sys
import string
b1 = 'files/sample.txt'
b2 = 'stop_words.txt'
def fonk1():
    if len(sys.argv) > 3:
        print
        print "Usage: python indexer.py <b4> <b7>"
        print "If no arguments are given %s and %s will be used as default files" % (b1, b2)
        print
        sys.exit()
    elif len(sys.argv) == 3:
        b3 = sys.argv[2]
        b4 = sys.argv[1]
    elif len(sys.argv) == 2:
        b3 = b2
        b4 = sys.argv[1]
    elif len(sys.argv) == 1:
        b3 = b2
        b4 = b1
    print 'Using %s as file and %s as stop word reference.' % (b4, b3)
    print
    fonk2(b4, b3)
def fonk2(b4, b3):
    b5 = set(string.punctuation)
    b6 = open(b4).read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
    b6 = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in b6]
    b7 = open(b3).read().decode("utf-8-sig").encode("utf-8").splitlines()
    b8 = [x for x in b6 if x not in b7]
    from collections import Counter
    b9 = Counter(b8)
    b10 = {k:v for (k,v) in b9.iteritems()}
    b11 = sorted(b10.items(), key=lambda x: x[0])
    for x in range(len(b11)):
        print '%s: %s' % (b11[x][0], b11[x][1])
if b12 = = '__main__':
  fonk1()