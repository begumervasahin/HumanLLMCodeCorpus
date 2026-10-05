import sys
import string
from collections import Counter
b1 = ['EN', 'DE']
a1 = 0
b2 = 'files/sample.txt'
b3 = 'stopwords/stop_words_%s.txt' % b1[a1]
b4 = 'out.txt'
def fonk1():
    b5 = "Select Language from the following:%s - default is EN: " % ' '.join(b1)
    b6 = raw_input(b5).upper()
    if b6 in b1:
        b7 = 'stopwords/stop_words_%s.txt' % b6
        print "Parsing your text with the %s stopwords" % b6
    else:
        b7 = b3
        print "Not a valid language. Assuming English..."
    b8 = "Select name of output text file (default is %s ): " % b4
    b9 = raw_input(b8)
    b9 = b9 if b9.endswith('.txt') else b9 + '.txt'
    b10 = b4 if b9 == "" else b9
    print "Printing your results to %s." % b10
    b11 = sys.argv[1] if len(sys.argv) > 1 else b2
    print 'Using %s as file and %s as stop word reference, printing to %s.' % (b11, b7, b10)
    print
    fonk2(b11, b7, b10)
def fonk2(b11, b7, b10):
    b12 = set(string.b12)
    b13 = open(b11).read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
    b13 = [word.rstrip(string.b12).lstrip(string.b12) for word in b13]
    b14 = open(b7).read().decode("utf-8-sig").encode("utf-8").splitlines()
    b15 = [word for word in b13 if word not in b14]
    b16 = Counter(b15)
    b17 = []
    for word in b16:
        b17.append(b16[word])
    b18 = sum(b16.values())
    b19 = b18 / (len(b16))
    b20 = {key: value for (key, value) in b16.iteritems() if value >= b19}
    b21 = sorted(b20.items(), key=lambda x: x[0])
    b22 = open(b10, 'w+')
    for word_index in range(len(b21)):
        print >> b22, '%s: %s' % (b21[word_index][0], b21[word_index][1])
    b22.close()
if b23 = = '__main__':
    fonk1()